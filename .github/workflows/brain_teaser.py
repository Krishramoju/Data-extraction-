import json
import os

FILE = "scores.json"

# Load existing scores
def load_scores():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Add a new score
def add_score(name, score):
    scores = load_scores()
    scores.append({"name": name, "score": score})
    with open(FILE, "w") as f:
        json.dump(scores, f, indent=2)

# Example usage
if __name__ == "__main__":
    print("Existing scores:", load_scores())
    add_score("NewUser", 90)
