



@app.on_message(filters.command(["ping", "ping@MentosMusicBot"]))
async def ping(_, message):
    uptime = await bot_sys_stats()
    start = datetime.now()
    response = await message.reply_photo(
        photo="cache/Query.png",
        caption=">> Pong!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit_text(f"**༎⃝💔𝐆𝐇𝐎𝐒𝐓༎⃝➤**\n`{resp} ms`\n\n<b><u>༎⃝✨𝐆𝐇𝐎𝐒𝐓 𝐔𝐏𝐓𝐈𝐌𝐄༎⃝➤ ✘</u></b>{uptime}")
