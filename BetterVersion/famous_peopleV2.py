import wikipedia
import sqlite3

conn = sqlite3.connect('famous_people.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS famous_people
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   summary TEXT NOT NULL);''')


def search_wikipedia(name):
    search_results = wikipedia.search(name)

    if not search_results:
        print("I don't know this person.")
        return None, None

    if name in search_results:
        summary = wikipedia.summary(name, sentences=1)
        return name, summary

    page = 0
    while True:
        print("Did you mean one of these?")
        start_idx = page * 5
        end_idx = start_idx + 5
        for i, option in enumerate(search_results[start_idx:end_idx]):
            print(f"{i+1}. {option}")

        print("6. Show next 5 suggestions")
        print("7. None of the above")

        choice = int(input("Enter the number of your choice: "))

        if choice >= 1 and choice <= 5:
            chosen_name = search_results[start_idx + choice - 1]
            break
        elif choice == 6:
            page += 1
            if start_idx + 5 >= len(search_results):
                print("No more suggestions.")
                return None, None
            continue
        elif choice == 7:
            print("No suitable option chosen.")
            return None, None

    summary = wikipedia.summary(chosen_name, sentences=1)
    return chosen_name, summary


def insert_into_db(name, summary):
    cursor.execute(
        "INSERT INTO famous_people (name, summary) VALUES (?, ?)", (name, summary))
    conn.commit()


def main():
    name = input("Enter the name of a famous person: ")
    name, summary = search_wikipedia(name)

    if summary:
        insert_into_db(name, summary)
        print(f"Added {name} to the database.")
        print(f"Name: {name}")
        print(f"Summary: {summary}")


if __name__ == "__main__":
    main()

conn.close()
