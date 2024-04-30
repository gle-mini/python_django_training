import sys

def find_capital_city(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    state_abbreviation = states.get(state)

    if state_abbreviation:
        return capital_cities.get(state_abbreviation, "Unknown state")
    else:
        return "Unknown state"

if __name__ == "__main__":
    # Ensure exactly one argument is provided
    if len(sys.argv) == 2:
        # Fetch the state from command line argument
        state = sys.argv[1]
        result = find_capital_city(state)
        print(result)

