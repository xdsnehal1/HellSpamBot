import random
from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5, SpamBot6, SpamBot7, SpamBot8, SpamBot9, SpamBot10 
from hellspam.helpers.gspam import GSPAM
from telethon import events

enemy = []

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot6.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot7.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot8.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot9.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot10.on(events.NewMessage(incoming=True, pattern='/replyraid'))
async def replyraid(e):
    if e.sender_id in MY_USERS:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        me = await SpamBot1.get_me()
        global enemy
        if e.is_reply is True:
            replied = await e.get_reply_message()
            get_name = replied.sender.first_name
            get_id = replied.sender.id
            tag = f"[{get_name}](tg://user?id={get_id})"
            try:
                if get_id in DEV_USERS:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Kid!` {tag} `Is You're Daddy! You Cant Abuse Him!`")
                elif get_id == OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Master!`")
                elif get_id in CO_OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Co-Owner!`")
                elif get_id  in SUDO_USERS:
                    await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Sudo User!`")
                elif get_id == me.id:
                    await e.client.send_message(e.chat_id, "`I'm Not Going To Take Action's on Myself!`")
                else:
                    message = await e.client.send_message(e.chat_id, f"`Reply Raid Activating.....!`")
                    if get_id in enemy:
                        await e.client.edit_message(message, f"`Reply Raid Already Activated On` {tag}!")
                    else:
                        enemy.append(get_id)
                        await e.client.edit_message(message, f"`Reply Raid Activated On` {tag}!")
                        print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "`Something Went Wrong!`")
        else:
            text = e.raw_text[11:]
            try:
                if text == "":
                    await e.client.send_message(e.chat_id, "`Please Mention Someone To Activate Reply Raid!`")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    if get_id in DEV_USERS:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Kid!` {tag} `Is You're Daddy! You Cant Abuse Him!`")
                    elif get_id == OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Master!`")
                    elif get_id in CO_OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Co-Owner!`")
                    elif get_id  in SUDO_USERS:
                        await e.client.send_message(e.chat_id, f"`Hey` {mention} `Nigga! I'm Not Going To Abuse My Sudo User!`")
                    elif get_id == me.id:
                        await e.client.send_message(e.chat_id, "`I'm Not Going To Take Action's on Myself!`")
                    else:
                        message = await e.client.send_message(e.chat_id, f"`Reply Raid Activating.....!`")
                        if get_id in enemy:
                            await e.client.edit_message(message, f"`Reply Raid Already Activated On` {tag}!")
                        else:
                            enemy.append(get_id)
                            await e.client.edit_message(message, f"`Reply Raid Activated On` {tag}!")
                            print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")


@SpamBot1.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot6.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot7.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot8.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot9.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot10.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
async def dreplyraid(e):
    if e.sender_id in MY_USERS:
        global enemy
        if e.is_reply is True:
            try:
                replied = await e.get_reply_message()
                get_name = replied.sender.first_name
                get_id = replied.sender.id
                tag = f"[{get_name}](tg://user?id={get_id})"
                message = await e.client.send_message(e.chat_id, f"`Reply Raid Dectivating.....!`")
                if get_id not in enemy:
                    await e.client.edit_message(message, f"`Reply Raid Already Not Activated On` {tag}!")
                else:
                    enemy.remove(get_id)
                    await e.client.edit_message(message, f"`Reply Raid Dectivated On` {tag}!")
                    print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong!")
        else:
            try:
                text = e.raw_text[11:]
                if text == "":
                    await e.client.send_message(e.chat_id, "`Please Mention Someone To Deactivate Reply Raid!`")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    message = await e.client.send_message(e.chat_id, f"`Reply Raid Dectivating.....!`")
                    if get_id not in enemy:
                        await e.client.edit_message(message, f"`Reply Raid Already Not Activated On` {tag}!")
                    else:
                        enemy.remove(get_id)
                        await e.client.edit_message(message, f"`Reply Raid Dectivated On` {tag}!")
                        print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "`Something Went Wrong!`")

@SpamBot1.on(events.NewMessage(incoming=True))
@SpamBot2.on(events.NewMessage(incoming=True))
@SpamBot3.on(events.NewMessage(incoming=True))
@SpamBot4.on(events.NewMessage(incoming=True))
@SpamBot5.on(events.NewMessage(incoming=True))
@SpamBot6.on(events.NewMessage(incoming=True))
@SpamBot7.on(events.NewMessage(incoming=True))
@SpamBot8.on(events.NewMessage(incoming=True))
@SpamBot9.on(events.NewMessage(incoming=True))
@SpamBot10.on(events.NewMessage(incoming=True))
async def fuck(e):
    global enemy
    message1 = random.choice(GSPAM)
    message2 = random.choice(GSPAM)
    message3 = random.choice(GSPAM)
    message4 = random.choice(GSPAM)
    victim = e.message.id
    if e.sender_id in enemy:
        await e.client.send_message(e.chat_id, message1, reply_to=victim)
        await e.client.send_message(e.chat_id, message2, reply_to=victim)
        await e.client.send_message(e.chat_id, message3, reply_to=victim)
        await e.client.send_message(e.chat_id, message4, reply_to=victim)
