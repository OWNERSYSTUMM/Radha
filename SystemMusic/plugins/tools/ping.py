from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from SystemMusic import app
from SystemMusic.core.call import SHUKLA
from SystemMusic.utils import bot_sys_stats
from SystemMusic.utils.decorators.language import language
from SystemMusic.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_video(
        video="https://graph.org/file/5690109178f081adf464d.mp4",
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await SHUKLA.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
