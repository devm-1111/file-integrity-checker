import json
import os

from hash_utils import calculate_sha256


DATABASE_FILE = "database.json"


def load_database():
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


def save_database(database):
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)


def main():
    file_path = input("File path: ").strip()

    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return

    database = load_database()

    current_hash = calculate_sha256(file_path)

    print(f"\nSHA-256:\n{current_hash}")

    if file_path not in database:
        print("\nStatus: New file")
    else:
        if database[file_path] == current_hash:
            print("\nStatus: File unchanged")
        else:
            print("\nStatus: File modified")

    database[file_path] = current_hash
    save_database(database)

    print("Database updated.")


if __name__ == "__main__":
    main()