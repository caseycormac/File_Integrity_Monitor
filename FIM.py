import hashlib
import os
from time import sleep, strftime
from getpass import getuser

def calculate_file_hash(filepath):
    """Calculate the SHA512 hash of a file."""
    hash_sha512 = hashlib.sha512()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha512.update(chunk)
    return hash_sha512.hexdigest()

def erase_baseline_if_already_exists():
    """Delete baseline.txt if it exists."""
    if os.path.exists('baseline.txt'):
        print("Removing old baseline.txt file...")
        os.remove('baseline.txt')
    else:
        print("No existing baseline.txt to remove.")

def collect_new_baseline():
    """Collect a new baseline of file hashes, ignoring certain file types."""
    erase_baseline_if_already_exists()

    # WSL uses Linux-style paths. Ensure './Files' directory exists.
    files_directory = './Files'
    if not os.path.exists(files_directory):
        print("Creating './Files' directory...")
        os.makedirs(files_directory)
    else:
        print("Found './Files' directory.")

    # Get all files in the directory, excluding hidden ones (starting with '.')
    files = [f for f in os.listdir(files_directory) if os.path.isfile(os.path.join(files_directory, f)) and not f.startswith('.')]
    print(f"Files to baseline: {files}")

    with open('baseline.txt', 'a') as baseline_file:
        for f in files:
            file_path = os.path.join(files_directory, f)
            file_hash = calculate_file_hash(file_path)
            baseline_file.write(f"{file_path}|{file_hash}\n")
            print(f"Hashed {file_path}: {file_hash}")

    print("Baseline collection complete.")

def begin_monitoring():
    """Monitor files for changes, deletions, and new copies based on the saved baseline."""
    print("Starting file monitoring based on the baseline...")

    # Check if the baseline exists
    if not os.path.exists('baseline.txt'):
        print("No baseline.txt found! Please collect a baseline first.")
        return

    # Read the baseline
    with open('baseline.txt', 'r') as baseline_file:
        baseline_data = [line.strip().split('|') for line in baseline_file.readlines()]

    # Monitor files
    for file_path, old_hash in baseline_data:
        if os.path.exists(file_path):
            current_hash = calculate_file_hash(file_path)
            if current_hash != old_hash:
                print(f"File modified: {file_path}")
            else:
                print(f"No changes detected for: {file_path}")
        else:
            print(f"File deleted: {file_path}")

    print("Monitoring complete.")


def main():
    print("\nWhat would you like to do?\n")
    print("    A) Collect new Baseline?")
    print("    B) Begin monitoring files with saved Baseline?\n")

    response = input("Please enter 'A' or 'B': ").upper()
    print(f"You entered: {response}")

    if response == 'A':
        print("Collecting new baseline...")
        collect_new_baseline()
    elif response == 'B':
        print("Beginning monitoring...")
        begin_monitoring()
    else:
        print("Invalid input! Please enter 'A' or 'B'.")

# Run the script
print("Running the File Integrity Monitor...")
main()
