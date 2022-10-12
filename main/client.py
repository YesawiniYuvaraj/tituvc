from pyrogram import Client
import os
API_ID = int(os.environ.get("API_ID", 6))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SESSION = os.environ.get("SESSION", "")

bot = Client(
    session_name=SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={'root': 'modules.bot'}
)

asst = Client(
  "alexus",
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN,
  plugins={'root': "modules.assistant"}
)
