import threading
import random
import time
import logging
import string
import sys

# Setup logging
logging.basicConfig(filename='battledot.log', level=logging.INFO, format='%(asctime)s - %(message)s', filemode='w')

class Player(threading.Thread):
    alive_players = []
    alive_players_lock = threading.Lock()
    game_over = False

    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name
        self.next_player = None
        self.grid_size = 10
        self.ship_position = (random.randint(0, 9), random.randint(0, 9))
        self.is_alive = True
        self.lock = threading.Lock()
        Player.alive_players.append(self)

    def run(self):
        while self.is_alive and not Player.game_over:
            time.sleep(random.uniform(0.5, 1.5))  # simulate thinking time
            self.bomb_next_player()

    def bomb_next_player(self):
        if not self.is_alive or Player.game_over:
            return
        
        with Player.alive_players_lock:
            if not self.next_player.is_alive:
                return

        bomb_position = (random.randint(0, 9), random.randint(0, 9))
        logging.info(f"Player {self.player_name} bombing Player {self.next_player.player_name} at {bomb_position}")
        print(f"Player {self.player_name} bombing Player {self.next_player.player_name} at {bomb_position}")
        self.next_player.receive_bomb(bomb_position, self)

    def receive_bomb(self, position, attacker):
        with self.lock:
            if not self.is_alive or Player.game_over:
                return

            if position == self.ship_position:
                logging.info(f"Player {self.player_name} got hit by Player {attacker.player_name}. Player {self.player_name} is dead.")
                print(f"Player {self.player_name} got hit by Player {attacker.player_name}. Player {self.player_name} is dead.")
                self.is_alive = False
                with Player.alive_players_lock:
                    Player.alive_players.remove(self)
                attacker.update_target()
                self.check_game_over(attacker)

            else:
                logging.info(f"Player {self.player_name} was missed at {position} by Player {attacker.player_name}")
                print(f"Player {self.player_name} was missed at {position} by Player {attacker.player_name}")

    def update_target(self):
        with Player.alive_players_lock:
            if len(Player.alive_players) == 1:
                return

            current_index = Player.alive_players.index(self)
            self.next_player = Player.alive_players[(current_index + 1) % len(Player.alive_players)]
            logging.info(f"Player {self.player_name} now targets Player {self.next_player.player_name}")
            print(f"Player {self.player_name} now targets Player {self.next_player.player_name}")

    def check_game_over(self, attacker):
        with Player.alive_players_lock:
            if len(Player.alive_players) == 1 and not Player.game_over:
                Player.game_over = True
                logging.info(f"Player {attacker.player_name} is the last one standing and wins the game!")
                print(f"Player {attacker.player_name} is the last one standing and wins the game!")
                print("Log file created")
                sys.exit()  # Terminate the program

def create_players(n):
    player_names = string.ascii_uppercase[:n]
    players = [Player(player_names[i]) for i in range(n)]
    for i in range(n):
        players[i].next_player = players[(i + 1) % n]

    return players

def start_game(players):
    for player in players:
        player.start()

def wait_for_game_end(players):
    for player in players:
        player.join()

if __name__ == "__main__":
    num_players = 2  # number of players
    players = create_players(num_players)
    start_game(players)
    wait_for_game_end(players)
