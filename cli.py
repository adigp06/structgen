"""Simple OpenRouter prompt client."""

import argparse
import os

import dotenv
import openai


dotenv.load_dotenv()

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def main():
    parser = argparse.ArgumentParser(description="Send a prompt to OpenRouter.")
    parser.add_argument("prompt", help="The prompt to send to the model")
    args = parser.parse_args()

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": args.prompt}],
        max_tokens=10,
        temperature=0.0,
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
