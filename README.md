# Famous People Info Fetcher

## Overview

This Python application fetches information about famous people from Wikipedia and stores it in a SQLite database. The user inputs the name of a famous person, and the program checks if the name exists on Wikipedia. If it does, the program fetches a summary of the person's Wikipedia page and stores it in a SQLite database.

## Application Description

The application is a simple command-line Python program with the following functionalities:

1. The program prompts the user to input the full name of a famous person (e.g., Donald Trump).

2. It checks if the name exists on Wikipedia.

   - If the name is not found, it prints the message "I don't know this person" and suggests a similar name if possible.
   - If the name is found, it creates a new entry in a SQLite database table called famous_people.

   - On [Better Version](https://github.com/John4E656F/famous_people-py/tree/main/BetterVersion)/famous_peopleV2: If the user input is to ambiguous (e.g., Obama) the script will suggestion 5 options (e.g;, Barack Obama, Michelle Obama, etc...) and if the desired choice is not in the options user can check 5 more options or Exit with the option: "None of the above"

The famous_people table has three columns:

- **ID**: An auto-incrementing identifier starting at 1.
- **name**: The full name of the person.
- **summary**: A summary of the person's Wikipedia page.

## Requirements

- [Python 3.x](https://www.python.org/)
- [Wikipedia Python package](https://wikipedia.readthedocs.io/en/latest/code.html#module-wikipedia.exceptions).
- [SQLite database](https://docs.python.org/3/library/sqlite3.html#tutorial).

## Installation

### Command Line

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Install the required Python packages:
   `pip install wikipedia`

### Jupyter Notebook

1. Install [Jupyter Notebook](https://jupyter.org/install)

## Usage

### Command Line

1. Run the Python script: `python famous_people.py`
2. Follow the on-screen instructions to input the name of a famous person.

### Jupyter Notebook

1. Open the famous_people.ipynb
2. Install the required Python packages by running the following cell:
   `!pip install wikipedia`
3. Run it famous_people cell.

## Important Note

The famous_people python script is just a basic script following the Technical Test Instruction.<br><br>
In the folder [Better Version](https://github.com/John4E656F/famous_people-py/tree/main/BetterVersion), there is a improved script which the script suggest a famous people name or when 'DisambiguationError' appear user can choose one of the suggested names.<br><br>
It will suggest 5 names and if its not in those five new name suggestions, user can check the next 5 or Select 'None of the above' to exit.
