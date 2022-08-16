import random
from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5, SpamBot6, SpamBot7, SpamBot8, SpamBot9, SpamBot10 
from hellspam.helpers.plinks import PLINKS
from telethon import events

a = False

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot6.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot7.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot8.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot9.on(events.NewMessage(incoming=True, pattern='/pspam'))
@SpamBot10.on(events.NewMessage(incoming=True, pattern='/pspam'))
async def pspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        elif e.raw_text[6:] == "":
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p)
            except Exception as er: 
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        
@SpamBot1.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot2.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot3.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot4.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot5.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot6on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot7.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot8.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot9.on(events.NewMessage(incoming=True, pattern="/pstop"))
@SpamBot10.on(events.NewMessage(incoming=True, pattern="/pstop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "Porn Spam Stopped Successfully")
