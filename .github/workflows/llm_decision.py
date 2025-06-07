import json
import os

FILE = "scenarios.json"

# Load decision scenarios
def load_scenarios():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Add a new scenario
def add_scenario(question, answer):
    scenarios = load_scenarios()
    scenarios.append({"question": question, "answer": answer})
    with open(FILE, "w") as f:
        json.dump(scenarios, f, indent=2)

# Example usage
if __name__ == "__main__":
    print("Loaded scenarios:", load_scenarios())
    add_scenario("Can AI predict hiring outcomes?", "Yes, but only as a recommendation.")
