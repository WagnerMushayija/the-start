import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():
        # Load environment variables from .env file
        load_dotenv()
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API key not found. Please set the API_KEY environment variable.")
        print(f"Loaded API Key: {api_key[:4]}...{api_key[-4:]}")  
        # Print part of the API key to verify it's loaded

                                        # Configure the API key
        genai.configure(api_key=api_key)

                                                # Test a simple query
        query = "Explain how AI works"
        try:
            response = genai.generate_text(
                    model='models/text-bison-001',
                    prompt=query
            )
            print("API Call Successful!")
            print("Response Object:", response)
            if hasattr(response, 'candidate'):
                print("Generated Text:", response.candidates[0].text)
            else:
                print("No candidates found in the response.")

        except Exception as e:
            print("API Call Failed.")
            print(e)
if __name__ == "__main__":
    main()

