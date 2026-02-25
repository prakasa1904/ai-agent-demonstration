import os
from dotenv import load_dotenv

from agent.openai import run
from openai import RateLimitError

load_dotenv() # Load environment variables from .env file

# exit program if OPENAI_API_KEY is not set
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY is not set.")
    exit(1)

def main():
    try:
        # 1. question for CPU usage: Berapa CPU usage saat ini?
        # 2. question for memory usage: Berapa memory usage saat ini?
        output = run("Cari user dengan email prakasa@devetek.com")
        print(output.output_text)
    except Exception as e:
        # Error handler by error type
        if isinstance(e, RateLimitError):
            # Quota exceed error, get message from response
            dict = e.response.json()
            print(f"Error: Quota exceed error. {dict['error']['message']}")
        else:
            print(f"Error: Unknown error type {type(e)}.")
    
if __name__ == "__main__":
    main()