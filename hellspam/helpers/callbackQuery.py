from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5, SpamBot6, SpamBot7, SpamBot8, SpamBot9, SpamBot10 
from hellspam.help import *
from hellspam.helpers.commands import *
from telethon import events


@SpamBot1.on(events.CallbackQuery(data=b'alive'))
@SpamBot2.on(events.CallbackQuery(data=b'alive'))
@SpamBot3.on(events.CallbackQuery(data=b'alive'))
@SpamBot4.on(events.CallbackQuery(data=b'alive'))
@SpamBot5.on(events.CallbackQuery(data=b'alive'))
@SpamBot6.on(events.CallbackQuery(data=b'alive'))
@SpamBot7.on(events.CallbackQuery(data=b'alive'))
@SpamBot8.on(events.CallbackQuery(data=b'alive'))
@SpamBot9.on(events.CallbackQuery(data=b'alive'))
@SpamBot10.on(events.CallbackQuery(data=b'alive'))



async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)



@SpamBot1.on(events.CallbackQuery(data=b'ping'))
@SpamBot2.on(events.CallbackQuery(data=b'ping'))
@SpamBot3.on(events.CallbackQuery(data=b'ping'))
@SpamBot4.on(events.CallbackQuery(data=b'ping'))
@SpamBot5.on(events.CallbackQuery(data=b'ping'))
@SpamBot6.on(events.CallbackQuery(data=b'ping'))
@SpamBot7.on(events.CallbackQuery(data=b'ping'))
@SpamBot8.on(events.CallbackQuery(data=b'ping'))
@SpamBot9.on(events.CallbackQuery(data=b'ping'))
@SpamBot10.on(events.CallbackQuery(data=b'ping'))




async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)
