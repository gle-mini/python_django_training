import sys

def find_state_by_capital_city(capital):
    # Dictionaries provided
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

    # Reverse the capital_cities dictionary to map from capitals to states
    capitals_to_states = {v: k for k, v in capital_cities.items()}

    # Get state abbreviation using the capital city
    state_abbreviation = capitals_to_states.get(capital)

    # Find state name using state abbreviation
    if state_abbreviation:
        for state, abbreviation in states.items():
            if abbreviation == state_abbreviation:
                return state
    return "Unknown capital city"

if __name__ == "__main__":
    # Ensure exactly one argument is provided
    if len(sys.argv) == 2:
        # Fetch the capital city from command line argument
        capital = sys.argv[1]
        # Get the state or appropriate message
        result = find_state_by_capital_city(capital)
        print(result)
