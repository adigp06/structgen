"""Build a DFA for the regular expression [0-9]{n}."""


def build_dfa_for_digits(n):
    """Return a DFA that accepts exactly n decimal digits."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    digits = "0123456789"
    dfa = []

    for state in range(n):
        dfa.append({digit: state + 1 for digit in digits})

    dfa.append({})  # State n is the accepting state.
    return dfa


if __name__ == "__main__":
    print(build_dfa_for_digits(3))
