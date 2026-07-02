# File Integrity Checker

A simple Python tool that calculates the SHA-256 hash of a file and detects whether it has been modified since the last scan.

## Features

- Calculate SHA-256 hashes
- Store hashes in a local JSON database
- Detect new files
- Detect modified files
- Detect unchanged files
- No external dependencies required

## Project Structure

```
file-integrity-checker/
│
├── main.py
├── hash_utils.py
├── database.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer

No external Python packages are required.

## Usage

Run the program:

```bash
python main.py
```

Enter the path to the file when prompted.

Example:

```File path: C:\Users\User\Documents\report.pdf

SHA-256:
0ff53170dabbe1fd113a7793d674517a3a57eaa3ec8a8afe7be3e61acf3cba69

File size: 240 bytes
Scan time: 2026-07-02 23:11:48

Status: File unchanged

Database updated.
```

## Output

The program stores hashes in `database.json`.

Example:

```json
{
    "C:\\Users\\User\\Desktop\\example.txt": "3dc9aae309078c4cb7681132f7565b141aa1f91e64da206de1f3305def74bfcf"
}
```

## Disclaimer

This project is intended for educational purposes and local file integrity verification.
