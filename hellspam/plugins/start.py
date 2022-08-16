from hellspam import *
from hellspam import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5
from telethon import events, Button


data  = [
    Button.url("Channel", url="t.me/HellSpamBot"),
    Button.url("Repo", url="https://GitHub.com/TeamHell/HellSpamBot"),
    Button.url("Group", url="t.me/HellSpam_SupportChat")
]


@SpamBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot6.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot7.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot8.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot9.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot10.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[Akhil](t.me/akhilprs)"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hey {mention},
This Is Hell Spam Bot!
A Powerful Telegram Spam Bot, fast and stable !

✪ Master:- {myOwner}
✪ Sudo:- {sudo_user}
✪ Creator:- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)
