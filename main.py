import json
import os
from datetime import datetime

from hash_utils import calculate_sha256

DATABASE_FILE = "database.json"


def load_database():
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


def save_database(database):
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)


def pause():
    input("\nPress Enter to continue...")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def scan_file():
    file_path = input("\nFile path: ").strip()

    if not os.path.isfile(file_path):
        print("\nError: File not found.")
        pause()
        return

    database = load_database()

    current_hash = calculate_sha256(file_path)
    file_size = os.path.getsize(file_path)
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\nSHA-256:\n{current_hash}")
    print(f"File size: {file_size} bytes")
    print(f"Scan time: {scan_time}")

    if file_path not in database:
        print("\nStatus: New file")
    else:
        if database[file_path]["hash"] == current_hash:
            print("\nStatus: File unchanged")
        else:
            print("\nStatus: File modified")

    database[file_path] = {
        "hash": current_hash,
        "size": file_size,
        "last_scan": scan_time,
        "algorithm": "SHA-256"
    }

    save_database(database)

    print("Database updated.")
    pause()


def view_database():
    database = load_database()

    if not database:
        print("\nDatabase is empty.")
        pause()
        return

    print("\n===== DATABASE =====")

    for file_path, data in database.items():
        print(f"\nFile: {file_path}")
        print(f"Hash: {data['hash']}")
        print(f"Size: {data['size']} bytes")
        print(f"Last scan: {data['last_scan']}")
        print(f"Algorithm: {data['algorithm']}")

    pause()


def clear_database():
    confirmation = input("\nAre you sure? (y/n): ").lower()

    if confirmation == "y":
        save_database({})
        print("\nDatabase cleared successfully.")
    else:
        print("\nOperation cancelled.")

    pause()


def menu():
    while True:
        clear_screen()

        print("==============================")
        print(" File Integrity Checker v1.2")
        print("==============================")
        print("1. Scan file")
        print("2. View database")
        print("3. Clear database")
        print("4. Exit")

        option = input("\nSelect an option: ")

        if option == "1":
            scan_file()
        elif option == "2":
            view_database()
        elif option == "3":
            clear_database()
        elif option == "4":
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid option.")
            pause()


def main():
    menu()


if __name__ == "__main__":
    main()