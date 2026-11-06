import itertools
import re
def parse_and_evaluate(expression, var_assignments):
    for var, val in var_assignments.items():
        expression = re.sub(rf'\b{var}\b', str(val), expression)
    while '-->' in expression:
        expression = re.sub(r'([\w\(\)\s\bTrue\bFalse]+)\s*-->\s*([\w\(\)\s\bTrue\bFalse]+)', r'(not (\1) or (\2))', expression)
    while '==>' in expression:
        expression = re.sub(r'([\w\(\)\s\bTrue\bFalse]+)\s*==>\s*([\w\(\)\s\bTrue\bFalse]+)', r'((\1) == (\2))', expression)
    try:
        return eval(expression, {"__builtins__": None}, {})
    except Exception as e:
        return f"Error: Invalid syntax ({e})"
def generate_truth_table(expression_str):
    variables = sorted(list(set(re.findall(r'\b[A-Z]\b', expression_str))))
    if not variables:
        print("No variables found. Please use capital letters like P, Q, or R.")
        return
    header = " | ".join(f" {v} " for v in variables) + f" |  Output for: {expression_str}"
    print(header)
    print("-" * len(header))
    to_tf = lambda b: "T" if b is True else ("F" if b is False else b)
    for combos in itertools.product([True, False], repeat=len(variables)):
        var_assignments = dict(zip(variables, combos))
        result = parse_and_evaluate(expression_str, var_assignments)
        row_vars = " | ".join(f" {to_tf(var_assignments[v])} " for v in variables)
        print(f"{row_vars} |  {to_tf(result)}")
if __name__ == "__main__":
    print("Example 1: XNOR using '==>' (T when both are identical)")
    expr1 = "P ==> Q"
    generate_truth_table(expr1)
    
    print("\nExample 2: Standard Conjunction using 'and'")
    expr2 = "P and Q"
    generate_truth_table(expr2)
    
    print("\nExample 3: Complex Expression with Implication (-->) and XNOR (==>)")
    expr3 = "(not P or Q) --> (P ==> R)"
    generate_truth_table(expr3)
