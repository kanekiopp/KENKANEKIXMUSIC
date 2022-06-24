from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["hmmm", f"hmm@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
        await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""✨ **𝐈 𝐂𝐀𝐍 𝐏𝐋𝐀𝐘 𝐌𝐔𝐒𝐈𝐂 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐎𝐏 𝐆𝐑𝐎𝐔𝐏 𝐕𝐎𝐈𝐂𝐄 𝐂𝐇𝐀𝐓 💖.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫𝗦𝗨𝗠𝗠𝗢𝗡 𝗠𝗘💫",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("✨𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦", callback_data="cbcmds"),
                    InlineKeyboardButton("🌈𝗕𝗔𝗦𝗜𝗖 𝗚𝗨𝗜𝗗𝗘", callback_data="cbhowtouse"),
                ],
                [
                    InlineKeyboardButton(
                        "👅𝗖𝗛𝗜𝗧 𝗖𝗛𝗔𝗧", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🗯️𝗡𝗘𝗧 𝗪𝗢𝗥𝗞", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "❤️𝗧𝗥𝗢𝗝𝗔𝗡𝗦 𝗙𝗘𝗗❤️", url="https://t.me/TROJANS_FED"
                    )
                ],
            ]
        ),
     )


@Client.on_message(
    command(["uhmmm", f"uhmm@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **𝗛𝗘𝗟𝗟𝗢** {message.from_user.mention()} !
» **press the button below to read the explanation and see the list of available commands !**
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="𝐇𝐄𝐋𝐏", callback_data="cbguide")]]
        ),
    )

@Client.on_message(command(["hmmm", f"hmmm@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    delta_ping = time() - start
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"`〘 ♕ ᑭσɳց! ♕ 〙`\n" f"〘🔥`{delta_ping * 1000:.3f} ms`〙")


@Client.on_message(filters.command(["uptime", f"uptime@{BOT_USERNAME}"]))
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**✨𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦✨\n**
 **𝗨𝗣𝗧𝗜𝗠𝗘** `{uptime}`\n**
 **𝗦𝗧𝗔𝗥𝗧 𝗧𝗜𝗠𝗘** `{START_TIME_ISO}`**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥𝗡𝗘𝗧𝗪𝗢𝗥𝗞🔥", url=f"https://t.me/{UPDATES_CHANNEL}"
                   )
                ]
            ]
        )
    ) 
