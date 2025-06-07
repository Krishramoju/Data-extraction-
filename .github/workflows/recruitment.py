import csv
import os

FILE = "candidates.csv"

# Read existing candidates
def load_candidates():
    if not os.path.exists(FILE):
        return []
    with open(FILE, newline='') as f:
        return list(csv.DictReader(f))

# Add a new candidate
def add_candidate(name, email, position, status):
    is_new = not os.path.exists(FILE)
    with open(FILE, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Email", "Position", "Status"])
        if is_new:
            writer.writeheader()
        writer.writerow({
            "Name": name,
            "Email": email,
            "Position": position,
            "Status": status
        })

# Example usage
if __name__ == "__main__":
    print("Current candidates:", load_candidates())
    add_candidate("New Candidate", "new@example.com", "Data Analyst", "Interviewed")
