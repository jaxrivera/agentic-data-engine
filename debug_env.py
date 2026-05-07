import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('GOOGLE_API_KEY')
if key:
    print(f"Key Found! Starts with: {key[:5]}...")
else:
    print("Key NOT found. Check your .env file formatting.")

# Check for hidden characters or export issues
print(f"Current Directory: {os.getcwd()}")
