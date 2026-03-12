from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()

console.print("Here are some example NBA performances:", style="bold cyan")

table = Table(title="Top NBA Performances")
table.add_column("Player", style="magenta")
table.add_column("Team", style="cyan")
table.add_column("Opponent", style="cyan")
table.add_column("Points", justify="right")
table.add_column("Date")

table.add_row("Kobe Bryant", "LAL", "TOR", "81", "2006")
table.add_row("LeBron James", "CLE", "DET", "48", "2007")
table.add_row("Michael Jordan", "CHI", "UTA", "45", "1998")

console.print(table)

console.print("\n[bold cyan]Enter a great NBA performance:[/bold cyan]\n")

entries = []

while True:

    player = input("Enter player name: ")
    team = input("Enter team: ")
    opponent = input("Enter opponent: ")
    points = input("Enter points scored: ")
    date = input("Enter year: ")

    console.print("\nYou entered:", style="bold yellow")
    console.print(f"Player: {player}")
    console.print(f"Team: {team}")
    console.print(f"Opponent: {opponent}")
    console.print(f"Points: {points}")
    console.print(f"Date: {date}")

    confirm = input("Is this correct? (y/n): ")

    if confirm.lower() == "y":
        entries.append([player, team, opponent, points, date])
        console.print("Entry saved.\n", style="green")
    else:
        console.print("Let's try again.\n", style="red")
        continue

    more = input("Add another performance? (y/n): ")

    if more.lower() != "y":
        break


filename = "nba_performances.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Player", "Team", "Opponent", "Points", "Date"])
    writer.writerows(entries)

filepath = os.path.abspath(filename)

console.print("\nData saved successfully!", style="bold green")
console.print(f"File location: {filepath}")