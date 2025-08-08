import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Required credentials
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# Bot and owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "Its_ydv_vikky")
BOT_USERNAME = getenv("BOT_USERNAME", "RadhaaMusicBot")
BOT_NAME = getenv("BOT_NAME", "RADHA")
ASSUSERNAME = getenv("ASSUSERNAME", "Exampurrs")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# API URL - here
API_URL = getenv("API_URL", "https://tgmusic.fallenapi.fun")

# API KEY - here
API_KEY = getenv("API_KEY", "ef4e80_qtqagWb9uWwn07HeeUsOFNeTqU2RN_Ej")

# For - downloads
DOWNLOADS_DIR = "downloads"

# API URL - here
YTPROXY_URL = getenv("API_URL", "https://tgapi.xbitcode.com")

# API KEY - here
YT_API_KEY = getenv("API_KEY", "xbit_VES4CLV6PZLICZ9CKLVZ71")


# Limits and IDs
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1002018556839))
OWNER_ID = int(getenv("OWNER_ID", 7548614955))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/OWNERSYSTUMM/Radha")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FONT_CHANNEL_01")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Exampurrs")

# Assistant settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Song download limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Session strings
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# Miscellaneous
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/b61227af05544deb76a34.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/7bb907999ea7156227283.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/13afb9ee5c5da17930f1e.png"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/13afb9ee5c5da17930f1e.png"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# Helper function
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

# Calculate total duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHANNEL url is invalid. It must start with https://"
    )

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHAT url is invalid. It must start with https://"
    )
