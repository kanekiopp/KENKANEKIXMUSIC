from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
)
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    delta_ping = time() - start
    await message.reply_photo(
    photo=f"{ALIVE_IMG}",
    caption=f"**`〘 ♕ ᑭσɳց! ♕ 〙`\n" f"〘🔥`{delta_ping * 1000:.3f} ms`〙**"


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "༎⃝💜𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐔𝐒༎⃝➤ ✘\n"
        f"• **༎⃝🔥𝐔𝐏𝐓𝐈𝐌𝐄༎⃝➤ ✘** `{uptime}`\n"
        f"• **༎⃝🌺𝐒𝐓𝐀𝐑𝐓 𝐓𝐈𝐌𝐄༎⃝➤ ✘** `{START_TIME_ISO}`"
    )
