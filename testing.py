from dotenv import load_dotenv
import os
print("this is the first line")
print("this is the second line")
print("this is the third line")

load_dotenv()

API_KEY = os.getenv("API_KEY")
print(f"Your api_key is : {API_KEY}")