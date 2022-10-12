import os 
from os import getenv

#----Sudo Configuration----#
# que = {}
SUDO_ID = list(map(int, getenv("SUDO_ID").split()))
#----Configuration----#
DURATION_LIMIT = os.environ.get("DURATION_LIMIT", 200)
COMMAND_PREFIXES = (os.environ.get("COMMAND_PREFIXES", "/ !").split())
ARQ_API_KEY = getenv("ARQ_API_KEY", "VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ")
BOT_NAME = os.environ.get("BOT_NAME", "")
UPDATES_CHANNEL = os.environ.get("UPDATE_CHANNEL", "@TeamAlexus")
