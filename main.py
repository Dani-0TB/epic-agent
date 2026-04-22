import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai.errors import APIError
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY not found, add it to your .env file.\n\
                    Example: echo GEMINI_API_KEY=[key] >> .env")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true",
                    help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(
    role="user", parts=[types.Part(text=args.user_prompt)])]


def main():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=messages)
    except APIError as e:
        print(f"Error with API Request: {e.message}")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

    if response.usage_metadata is None:
        raise RuntimeError("Error in the request, try again later...")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {
              response.usage_metadata.candidates_token_count}")

    print(f"Response\n{response.text}")

    exit(0)


if __name__ == "__main__":
    main()
