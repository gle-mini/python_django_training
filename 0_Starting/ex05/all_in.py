import sys

def analyze_inputs(input_string):

    if not input_string or input_string.replace(',', '').strip() == '':
        return None

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

    # Create reverse lookup for capital cities to states
    capital_to_state_lower = {v.lower(): k for k, v in capital_cities.items()}
    state_to_capital_lower = {k.lower(): v for k, v in states.items()}
    
    state_to_capital_upper = {v: k for k, v in states.items()}

    # Normalize input by trimming extra spaces and setting to lower case
    expressions = [expr.strip() for expr in input_string.split(',')]

    results = []
    for expr in expressions:
        if (expr == ""):
            continue
        if expr.lower() in state_to_capital_lower:
            # It's a recognized capital city
            results.append(f"{capital_cities.get(state_to_capital_lower.get(expr.lower()))} is the capital of {state_to_capital_upper.get(state_to_capital_lower.get(expr.lower()))}")
        elif expr.lower() in capital_to_state_lower:
            # It's a recognized state
            results.append(f"{capital_cities.get(capital_to_state_lower.get(expr.lower()))} is the capital of {state_to_capital_upper.get(capital_to_state_lower.get(expr.lower()))}")
        else:
            # Neither a recognized state nor capital
            results.append(f"{expr} is neither a capital city nor a state")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) == 2:  # Check for exactly one argument
        input_string = sys.argv[1]
        results = analyze_inputs(input_string)
        if results:  # If results list is not empty
            for result in results:
                print(result)
 
