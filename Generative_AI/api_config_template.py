import os
from google import genai

def get_client():
    """
    Returns a Gemini client.
    The API key should be set as an environment variable.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY as an environment variable")

    client = genai.Client(api_key=api_key)
    return client