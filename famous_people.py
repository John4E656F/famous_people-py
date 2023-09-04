import wikipedia
import sqlite3

con = sqlite3.connect("famous_people.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS famous_people
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            summary TEXT NOT NULL)""")


def search_wikipedia(name):
    search_results = wikipedia.search(name)

    if not search_results:
        print("I don’t not know this person.")
        return None

    if name not in search_results:
        print(f"Did you mean {search_results[0]}")
        return None

    summary = wikipedia.summary(name, sentences=1, auto_suggest=False)
    return summary


def insert_into_db(name, summary):
    cur.execute(
        "INSERT INTO famous_people (name, summary) VALUES(?, ?)", (name, summary))
    con.commit()


def main():
    name = input("Enter a name of a famous person: ")
    summary = search_wikipedia(name)

    if summary:
        insert_into_db(name, summary)
        print(f"Added {name} to the database")
        print(summary)

        con.close()


main()
