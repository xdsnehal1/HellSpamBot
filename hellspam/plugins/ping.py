from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5
from telethon import events
from datetime import datetime

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f" 𝐏𝐨𝐧𝐆 ✘ 𝐒𝐧𝐞𝐇𝐚𝐋 🎉\n\n 𝐒𝐧𝐞𝐇𝐚𝐋 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭🗿\n\n My Master:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\n 𝐒𝐩𝐄𝐄𝐝 :- {ms} 𝙢𝙎")
