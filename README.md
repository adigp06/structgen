# structgen

A lightweight, dependency-free implementation of **constrained decoding** for Large Language Models (LLMs). 

`structgen` forces LLMs to output strictly valid formats (like JSON, regex, or specific grammars) by directly masking logits during the generation loop. No retries. No prompt engineering. 

## How it works

Instead of asking an LLM to "please output JSON" and hoping it complies, `structgen` compiles a grammar into a Deterministic Finite Automaton (DFA). At every step of generation, it checks the DFA state and masks out any token that would violate the grammar by setting its logit to `-inf`.

This repository contains the core, from-scratch engine:
1. `dfa.py`: Compiles a regex into a DFA.
2. `mask.py`: Maps a tokenizer's vocabulary to the valid transitions of the DFA.
3. `engine.py`: Applies the logit mask to the raw model outputs.
4. `simulate.py`: A working proof-of-concept showing an AI attempting to break a rule, and the mask physically preventing it.

## Quick Start

Clone the repo and run the simulation to see the engine in action:

```bash
git clone https://github.com/adityp06/structgen.git
cd structgen
python3 simulate.py
