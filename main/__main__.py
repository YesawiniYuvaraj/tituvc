

from main.client import bot, asst
from pyrogram.errors import AccessTokenInvalid, ApiIdInvalid, ApiIdPublishedFlood
from services.callsmusic import pytgcalls
from pytgcalls import idle



if __name__ == "__main__":
    try:
        asst.start()  # Not using run as wanna print 
        print("•×•Yeahhhh boi Assistant bot Started•×•")
       # bot.run() # using run for session client
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your TOKEN is not valid.")
pytgcalls.start()
idle()
