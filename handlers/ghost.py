from time import time
from sys import version_info
from datetime import datetime
from config import ALIVE_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

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

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    delta_ping = time() - start
    await message.reply_photo(
    photo=f"{ALIVE_IMG}",
    caption=f"**`〘 ♕ ᑭσɳց! ♕ 〙`\n" f"〘🔥`{delta_ping * 1000:.3f} ms`〙**"
     
    )

@Client.on_message(filters.command(["uptime", f"uptime@{BOT_USERNAME}"]))
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**༎⃝💜𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐔𝐒༎⃝➤ ✘\n**
 **༎⃝🔥𝐔𝐏𝐓𝐈𝐌𝐄༎⃝➤ ✘** `{uptime}`\n**
 **༎⃝🌺𝐒𝐓𝐀𝐑𝐓 𝐓𝐈𝐌𝐄༎⃝➤ ✘** `{START_TIME_ISO}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "༎⃝🌺𝐒𝐔𝐏𝐏𝐎𝐑𝐓༎⃝➤", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "༎⃝🥀𝐔𝐏𝐃𝐀𝐓𝐄𝐒༎⃝➤", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**༎⃝💜 𝐇𝐈 𝐈,𝐌  [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
 **༎⃝💔𝐆𝐇𝐎𝐒𝐓 𝐌𝐔𝐒𝐈𝐂 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐅𝐈𝐍𝐄
**
 **༎⃝🥀𝐆𝐇𝐎𝐒𝐓 𝐌𝐔𝐒𝐈𝐂 𝐕𝐄𝐑𝐒𝐈𝐎𝐍༎⃝➤ 𝟶.𝟽.𝟶 𝐋𝐄𝐓𝐄𝐒𝐓**
 **༎⃝🔥𝐎𝐖𝐍𝐄𝐑༎⃝➤ [{OWNER_NAME}](https://t.me/{OWNER_NAME})**
 **༎⃝🌸𝐔𝐏𝐓𝐈𝐌𝐄༎⃝➤ `{uptime}`**
**༎⃝🔥𝐓𝐇𝐍𝐗 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐆𝐇𝐎𝐒𝐓 𝐌𝐔𝐒𝐈𝐂༎⃝➤**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "༎⃝🌺𝐒𝐔𝐏𝐏𝐎𝐑𝐓༎⃝➤", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "༎⃝🥀𝐔𝐏𝐃𝐀𝐓𝐄𝐒༎⃝➤", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )
