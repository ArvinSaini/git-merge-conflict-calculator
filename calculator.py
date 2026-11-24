"""Simple command-line calculator.

UCS745 Cloud and DevOps - Lab Assignment Q1.
The project itself is intentionally small; its purpose is to demonstrate a
Git / GitHub workflow (branching, committing, merging and conflict resolution).
"""

VERSION = "1.1.0-advanced-ops"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error"
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        return "Error"
    return a % b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
    "%": modulo,
}


def calculate(a, op, b):
    """Apply the operator `op` to the numbers a and b."""
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    return OPERATIONS[op](a, b)


def main():
    print(f"CLI Calculator v{VERSION}")
    print("Supported operators: " + " ".join(OPERATIONS))
    print("Type 'q' to quit.")
    while True:
        expr = input("calc> ").strip()
        if expr.lower() in ("q", "quit", "exit"):
            break
        try:
            a, op, b = expr.split()
            print(calculate(float(a), op, float(b)))
        except ValueError as exc:
            print(f"Invalid input ({exc}). Use the form: <number> <operator> <number>")


if __name__ == "__main__":
    main()
