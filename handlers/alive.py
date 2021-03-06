#ππ°πΈπ³ πΏππΎπΉπ΄π²π 
#ππ πΌπΎππ·π΄ππ΅ππ²πΊπ΄π πΈπ΅ π πΊπ°π½πΆ π°π½π³ π³πΎπ½'π πΆπΈππ΄ π²ππ΄π³πΈππ π‘
#πΌπΎπ³πΈπ΅π΄π³ π΅πΎπ π°π»π΄ππ° πΌπππΈπ² 

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import ALIVE_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
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


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0644af761ab849220707a.jpg",
        caption=f"""**HΙͺ I'α΄ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

 **π₯Kα΄Ι΄Kα΄Ι΄α΄α΄Ιͺ Mα΄sΙͺα΄ Wα΄Κα΄ΙͺΙ΄Ι’ FΙͺΙ΄α΄**


 **π₯Kα΄Ι΄ Kα΄Ι΄α΄α΄Ιͺ GΚα΄ Mα΄Ι΄α΄Ι’α΄α΄α΄Ι΄α΄ + Mα΄sΙͺα΄ Bα΄α΄**

 **π₯Oα΄‘Ι΄α΄Κ [Kα΄Ι΄ Kα΄Ι΄α΄α΄Ιͺ](https://t.me/KENKANEKI_XD)**

 **π₯Uα΄α΄Ιͺα΄α΄ `{uptime}`**

 **π₯TΚα΄Ι΄α΄s Fα΄Κ UsΙͺΙ΄Ι’ Mα΄**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sα΄α΄α΄α΄Κα΄", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "Uα΄α΄α΄α΄α΄s", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )
