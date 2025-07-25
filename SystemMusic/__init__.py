from SystemMusic.core.bot import SHUKLA
from SystemMusic.core.dir import dirr
from SystemMusic.core.git import git
from SystemMusic.core.userbot import Userbot
from SystemMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SHUKLA()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "ll_DRAGON_MUSIC_BOT"  # connect music api key "Dont change it"