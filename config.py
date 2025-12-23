import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE = os.getenv("PHONE")
SESSION_NAME = "session_user"

if not API_ID or not API_HASH:
    print("Error: API_ID and API_HASH must be set in .env file")
    sys.exit(1)

# Ensure session directory exists
SESSION_DIR = "sessions"
if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

SESSION_PATH = os.path.join(SESSION_DIR, SESSION_NAME)
