# NBA Performance CLI Data Entry

This command line interface (CLI) app made in Python allows users to enter NBA game performance data and save it to a CSV file.

The script uses **Rich** Python library to display tables and text in terminal.

## What the Script Does

1. Displays example NBA player performances using a formatted Rich table.
2. Asks the user to enter information about an NBA performance.
3. Asks the user to confirm that the entered data is correct.
4. Allows the user to add multiple entries.
5. Saves the confirmed data to a CSV file.
6. Prints the full file path so the user can locate the saved file.

## Data Fields Collected

The script collects the following information:

- Player Name
- Team
- Opponent
- Points Scored
- Game Date

## How to Run the Script

1. Navigate to the `python-libraries` folder in the terminal.

2. Run the script.

3. Follow the prompts in the terminal to enter data.

4. Once finished, the script will save the entries to a file called nba_performances.csv

The terminal will display the full path to the saved file.

## Requirements

- Python 3
- Rich Python library

Install Rich with: pip3 install rich



