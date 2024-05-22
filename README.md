# BattleDot Game

## Description
BattleDot is an unpopular networked spinoff of the popular Battleship game. In this game, players are arranged in a ring where each player bombs the next player in the ring. Each player has a 10x10 grid with a single randomly positioned ship. The game continues until only one player remains alive.

### Requirements
Python 3.x

### How to Compile and Run
#### Ensure Python is installed:
- Make sure you have Python 3.x installed on your machine. You can download it from python.org.

#### Download the BattleDot Code:
- Save the BattleDot Python script as battledot.py.

#### Run the BattleDot Game:
- Open a terminal or command prompt, navigate to the directory where you saved battledot.py, and run the following command:

````python BattleDot.py````


## How to Interpret the Results
### Log File:

- The game events and results are logged to a file named battledot.log in the same directory where you run the script.

### Player Actions:

- Each player takes turns bombing the next player in the ring. The coordinates of the bombing attempt and the result (hit or miss) are recorded in the log file.

### Player Hits and Deaths:

- If a player's bomb hits the ship of the next player, a log entry indicates that the player has been hit and is dead. The attacking player will then target the next alive player in the ring.

### Game End:

- The game continues until only one player remains. A log entry will announce the last player standing and the winner of the game.

### No of Players:
- No of players can be adjusted in the main function line 91, default is 3
