"""Simulate constrained token selection using a digit DFA."""

from dfa import build_dfa_for_digits
from mask import get_valid_token_ids
from engine import mask_logits


if __name__ == "__main__":
    dfa = build_dfa_for_digits(2)
    tokenizer_vocab = {0: "1", 1: "2", 2: "x", 3: "9"}
    current_state = 0
    generated_text = ""

    for _ in range(2):
        logits = [0.1, 0.2, 0.99, 0.4]
        valid_token_ids = get_valid_token_ids(
            dfa, current_state, tokenizer_vocab
        )

        print("Valid IDs:", valid_token_ids)
        print("Raw logits:", logits)

        masked_logits = mask_logits(logits, valid_token_ids)
        print("Masked logits:", masked_logits)

        chosen_token_id = max(
            range(len(masked_logits)), key=masked_logits.__getitem__
        )
        chosen_token = tokenizer_vocab[chosen_token_id]
        print("Chosen token:", chosen_token)

        generated_text += chosen_token
        for character in chosen_token:
            current_state = dfa[current_state][character]

    print("Final generated text:", generated_text)
