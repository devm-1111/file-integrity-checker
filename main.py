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


def main():
    file_path = input("File path: ").strip()

    if not os.path.isfile(file_path):
        print("Error: File not found.")
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


if __name__ == "__main__":
    main()