from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5, SpamBot6, SpamBot7, SpamBot8, SpamBot9, SpamBot10 
from telethon import events
from datetime import datetime

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot6.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot7.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot8.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot9.on(events.NewMessage(incoming=True, pattern='/ping'))
@SpamBot10.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"Pong!\n\nHell Spam Bot\n\nMy Master:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\nSpeed :- {ms} ms\n\nHell Spam Bot On Fire 🔥")
