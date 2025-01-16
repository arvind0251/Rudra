import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

try:
    DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "60"))
except ValueError:
    DURATION_LIMIT_MIN = 60

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))
OWNER_ID = int(getenv("OWNER_ID", 0))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/arvind0251/Rudra")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", "")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NexGenBots")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/NexGenSpam")

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    print("[WARNING] - SUPPORT_CHANNEL URL is wrong. Please ensure that it starts with https://")

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    print("[WARNING] - SUPPORT_GROUP URL is wrong. Please ensure that it starts with https://")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "False"))

PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "2145386496"))

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org//file/25115719697ed91ef5672.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org//file/389a372e8ae039320ca6c.png")
PLAYLIST_IMG_URL = "https://graph.org//file/3dfcffd0c218ead96b102.png"
STATS_IMG_URL = "https://graph.org//file/99a8a9c13bb01f9ac7d98.png"

# Fixing ImportError
SOUNDCLOUD_IMG_URL = getenv("SOUNDCLOUD_IMG_URL", "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg")

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
