import os
import argparse

from dotenv import load_dotenv

from google import genai
from google.genai import types
from google.genai.errors import APIError

from prompts import system_prompt
from functions.call_function import available_functions, call_function


MODEL = "gemini-2.5-flash"


def main():
    args = get_args()
    client = get_client()

    messages = [types.Content(
        role="user", parts=[types.Part(text=args.user_prompt)])]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    for _ in range(20):
        response = get_response(client, messages, args.verbose)

        candidates = response.candidates

        if candidates:
            for candidate in candidates:
                messages.append(candidate.content)

        if response.function_calls:
            function_responses = handle_function_calls(response, args.verbose)
            messages.append(types.Content(
                role="user", parts=function_responses))
        else:
            print(f"Response:\n{response.text}")
            exit(0)

    if response.function_calls:
        print(
            "Error: I could not come up with an answer qucik enough, I'm sowy sempai uwu")
        exit(1)


def handle_function_calls(response, verbose):
    function_results = []

    for function_call in response.function_calls:

        function_call_result = call_function(function_call, verbose)

        if not function_call_result.parts:
            raise Exception("Error: No parts in function call result")

        part = function_call_result.parts[0]
        if part.function_response is None:
            raise Exception(
                "Error: function_response is None.")

        if part.function_response.response is None:
            raise Exception("Error: Response is None")

        function_results.append(part)

        if verbose:
            print(
                f"-> {part.function_response.response}")

    return function_results


def get_response(client, messages, verbose):
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

    if response.usage_metadata is None:
        raise RuntimeError("Error in the request, try again later...")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        candidate_tokens = response.usage_metadata.candidates_token_count
        print(f"Response tokens: {candidate_tokens}")

    return response


def get_client():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY not found, add it to your .env file.\n"
            "Example: echo GEMINI_API_KEY=[key] >> .env"
        )

    return genai.Client(api_key=api_key)


def get_args():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose output")
    return parser.parse_args()


if __name__ == "__main__":
    main()
