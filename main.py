import os
import argparse

from dotenv import load_dotenv

from google import genai
from google.genai import types
from google.genai.errors import APIError

from prompts import system_prompt
from functions.call_function import available_functions, call_function

MODEL = "gemini-2.5-flash-lite"

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY not found, add it to your .env file.\n"
        "Example: echo GEMINI_API_KEY=[key] >> .env"
    )

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true",
                    help="Enable verbose output")
args = parser.parse_args()


def main():
    messages = [types.Content(
        role="user", parts=[types.Part(text=args.user_prompt)])]

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=messages,
            config=types.GenerateContentConfig(
                temperature=0,
                tools=[available_functions],
                system_instruction=system_prompt),
        )
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
        candidate_tokens = response.usage_metadata.candidates_token_count
        print(f"Response tokens: {candidate_tokens}")

    function_results = []

    if response.function_calls:

        for function_call in response.function_calls:

            function_call_result = call_function(function_call, args.verbose)

            if not function_call_result.parts:
                raise Exception("Error: No parts in function call result")

            part = function_call.parts[0]
            if part.function_respone is None:
                raise Exception(
                    "Error: function_respone is None.")

            if part.function_response.response is None:
                raise Exception("Error: Response is None")

            function_results.append(function_call_result.parts[0])

            if args.verbose:
                print(
                    f"-> {part.function_response.response}")

    else:
        print(f"Response\n{response.text}")


if __name__ == "__main__":
    main()
