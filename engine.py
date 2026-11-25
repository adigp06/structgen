"""Utilities for masking logits using valid token IDs."""


def mask_logits(logits, valid_token_ids):
    """Return logits with invalid token IDs masked to negative infinity."""
    valid_token_ids = set(valid_token_ids)
    return [
        logit if token_id in valid_token_ids else float("-inf")
        for token_id, logit in enumerate(logits)
    ]


if __name__ == "__main__":
    logits = [0.1, 0.2, 0.3, 0.4, 0.5]
    valid = [0, 2, 4]
    print(mask_logits(logits, valid))
