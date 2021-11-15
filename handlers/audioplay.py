from os import path
import converter
from callsmusic import callsmusic, queues
from config import (
    AUD_IMG,
    BOT_USERNAME,
    DURATION_LIMIT,
    GROUP_SUPPORT,
    QUE_IMG,
    UPDATES_CHANNEL,
)
from handlers.play import convert_seconds
from helpers.filters import command, other_filters
from helpers.gets import get_file_name
from pyrogram import Client
from pytgcalls.types.input_stream import InputAudioStream
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(_, message: Message):

    lel = await message.reply("🔁 **processing** sound...")
    costumer = message.from_user.mention

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="〘 ♕ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ♕ 〙",
                        url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton(
                        text="✘‿✘",
                        url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        )

    audio = message.reply_to_message.audio if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            return await lel.edit(f"❌ **music with duration more than** `{DURATION_LIMIT}` **minutes, can't play !**")

        file_name = get_file_name(audio)
        title = audio.title
        duration = convert_seconds(audio.duration)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        return await lel.edit("❗ **reply to a telegram audio file.**")
    else:
        return await lel.edit("❗ **reply to a telegram audio file.**")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
            photo="https://telegra.ph/file/36343b9d4742efe0b09cd.jpg",
            caption=f"🏷 **𝙽𝙰𝙼𝙴 ✘** [{title[:40]}](https://t.me/{GROUP_SUPPORT})\n⏱ **𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 ✘** `{duration}`\n🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈 ✘** {costumer}\n\n🌸 𝚃𝚁𝙰𝙲𝙺 𝙿𝙾𝚂𝙸𝚃𝙸𝙾𝙽 ✘** `{position}`",
            reply_markup=keyboard,
        )
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
            photo="https://telegra.ph/file/224178328de996a82507f.jpg",
            caption=f"🏷 **𝙽𝙰𝙼𝙴 ✘** [{title[:40]}](https://t.me/{GROUP_SUPPORT})\n⏱ **𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 ✘** `{duration}`\n💡 **𝚂𝚃𝙰𝚃𝚄𝚂:** `𝙿𝙻𝙰𝚈𝙸𝙽𝙶`\n" \
                   +f"🎧 **𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝚈 ✘** {costumer}",
            reply_markup=keyboard,
        )
        return await lel.delete()
