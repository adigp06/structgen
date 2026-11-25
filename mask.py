"""Find tokenizer tokens that follow a digit-matching DFA path."""

from dfa import build_dfa_for_digits


def get_valid_token_ids(dfa, current_state, tokenizer_vocab):
    """Return token IDs whose strings follow valid DFA transitions."""
    valid_token_ids = []

    for token_id, token in tokenizer_vocab.items():
        state = current_state
        is_valid = True

        for character in token:
            next_state = dfa[state].get(character)
            if next_state is None:
                is_valid = False
                break
            state = next_state

        if is_valid:
            valid_token_ids.append(token_id)

    return valid_token_ids


if __name__ == "__main__":
    dfa = build_dfa_for_digits(3)
    tokenizer_vocab = {0: "1", 1: "12", 2: "x", 3: "123", 4: "a"}
    print(get_valid_token_ids(dfa, 0, tokenizer_vocab))
