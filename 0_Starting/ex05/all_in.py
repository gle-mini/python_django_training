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

    capital_to_state_lower = {v.lower(): k for k, v in capital_cities.items()}
    state_to_capital_lower = {k.lower(): v for k, v in states.items()} 
    state_to_capital_upper = {v: k for k, v in states.items()}

    expressions = [expr.strip() for expr in input_string.split(',')]

    results = []
    for expr in expressions:
        if (expr == ""):
            continue
        if expr.lower() in state_to_capital_lower:
            results.append(f"{capital_cities.get(state_to_capital_lower.get(expr.lower()))} is the capital of {state_to_capital_upper.get(state_to_capital_lower.get(expr.lower()))}")
        elif expr.lower() in capital_to_state_lower:
            results.append(f"{capital_cities.get(capital_to_state_lower.get(expr.lower()))} is the capital of {state_to_capital_upper.get(capital_to_state_lower.get(expr.lower()))}")
        else:
            results.append(f"{expr} is neither a capital city nor a state")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
        results = analyze_inputs(input_string)
        if results:
            for result in results:
                print(result)
 
