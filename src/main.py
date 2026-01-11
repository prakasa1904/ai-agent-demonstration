import os
from dotenv import load_dotenv

from agent.openai import run

load_dotenv() # Load environment variables from .env file

# exit program if OPENAI_API_KEY is not set
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY is not set.")
    exit(1)

def main():
    # 1. question for CPU usage: Berapa CPU usage saat ini?
    # 2. question for memory usage: Berapa memory usage saat ini?
    output = run("Cari user dengan email prakasa@devetek.com")
    print(output.output_text)
    
if __name__ == "__main__":
    main()