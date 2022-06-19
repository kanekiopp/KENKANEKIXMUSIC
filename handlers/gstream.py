# Copyright (C) 2021 GHOST Music-Project

from os import path
import converter
from callsmusic import callsmusic, queues
from config import (
    ALIVE_IMG,
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
from pytgcalls.types.input_stream import InputStream
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(command(["kaneki", f"kaneki@{BOT_USERNAME}"]) & other_filters)
async def ghost(_, message: Message):
    costumer = message.from_user.mention
    lel = await message.reply_text("**Cᴏɴɴᴇᴄᴛɪɴɢ Tᴏ Kᴀɴᴇᴋɪ Sᴇʀᴠᴇʀ🔥**")

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"
                ),
                InlineKeyboardButton(
                    text="Uᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    audio = message.reply_to_message.audio if message.reply_to_message else None
    if not audio:
        return await lel.edit("💭 **please reply to a telegram audio file**")
    if round(audio.duration / 30) > DURATION_LIMIT:
        return await lel.edit(
            f"❌ **music with duration more than** `{DURATION_LIMIT}` **minutes, can't play !**"
        )

    title = audio.title
    file_name = get_file_name(audio)
    duration = convert_seconds(audio.duration)
    file_path = await converter.convert(
        (await message.reply_to_message.download(file_name))
        if not path.isfile(path.join("downloads", file_name))
        else file_name
    )
    chat_id = message.chat.id
    ACTV_CALLS = []
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))    
    if chat_id in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="https://telegra.ph/file/822494e7e9746743d2f07.jpg",
            caption=f"💡 **Tʀᴀᴄᴋ Aᴅᴅᴇᴅ Tᴏ Qᴜᴇᴜᴇ »** `{position}`\n\n🏷 **Nᴀᴍᴇ ✘** {title[:50]}\n⏱ **Dᴜʀᴀᴛɪᴏɴ ✘** `{duration}`\n🎧 **Rᴇǫᴜᴇsᴛ Bʏ ✘** {costumer}",
            reply_markup=keyboard,
        )
    else:
        await callsmusic.pytgcalls.join_group_call(
            chat_id, 
            InputStream(
                InputAudioStream(
                    file_path,
                ),
            ),
        )
        await message.reply_photo(
            photo="https://telegra.ph/file/822494e7e9746743d2f07.jpg",
            caption=f"🏷 **Nᴀᴍᴇ ✘** {title[:50]}\n⏱ **Dᴜʀᴀᴛɪᴏɴ ✘** `{duration}`\n💡 **Sᴛᴀᴛᴜs ✘** `𝙿𝙻𝙰𝚈𝙸𝙽𝙶`\n"
            + f"🎧 **Rᴇǫᴜᴇsᴛ Bʏ✘** {costumer}",
            reply_markup=keyboard,
        )

    return await lel.delete() 
