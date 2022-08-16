import asyncio
import logging
from telethon import TelegramClient
from hellspam.config import Config
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN1 = Config.BOT_TOKEN1
BOT_TOKEN2 = Config.BOT_TOKEN2
BOT_TOKEN3 = Config.BOT_TOKEN3
BOT_TOKEN4 = Config.BOT_TOKEN4
BOT_TOKEN5 = Config.BOT_TOKEN5
BOT_TOKEN6 = Config.BOT_TOKEN6
BOT_TOKEN7 = Config.BOT_TOKEN7
BOT_TOKEN8 = Config.BOT_TOKEN8
BOT_TOKEN9 = Config.BOT_TOKEN9
BOT_TOKEN10 = Config.BOT_TOKEN10

OWNER_ID = Config.OWNER_ID
OWNER_NAME = str(Config.OWNER_NAME) if Config.OWNER_NAME else "MafiaSpamBot"
OWNER_USERNAME = str(Config.OWNER_USERNAME) if Config.OWNER_USERNAME else "akhilprs"
CO_OWNER_ID = Config.CO_OWNER_ID
SUDO_USERS = Config.SUDO_USERS
DISPLAY_PIC = str(Config.DISPLAY_PIC) if Config.DISPLAY_PIC else "https://telegra.ph/file/0db6ef22ae3b481c3891c.jpg"
BIO_MSG = str(Config.BIO_MSG) if Config.BIO_MSG else "Hell Spam Bot is Alive !"


BOT_VERSION = 1.0

GOD_USERS = [2102783671]
DEV_USERS = [2102783671]
MY_USERS = [2102783671]
LIMIT = [2102783671]

MY_USERS.append(OWNER_ID)
MY_USERS.extend(CO_OWNER_ID)
MY_USERS.extend(SUDO_USERS)

LIMIT.append(OWNER_ID)
LIMIT.extend(CO_OWNER_ID)

GOD_USERS.append(OWNER_ID)

async def main():
    global SpamBot1
    global SpamBot2
    global SpamBot3
    global SpamBot4
    global SpamBot5
    global SpamBot6
    global SpamBot7
    global SpamBot8
    global SpamBot9
    global SpamBot10

    if BOT_TOKEN1:
        print("Working On Bot Token 1!")
        try:
            SpamBot1 = TelegramClient("HellSpamBot1", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 1 OK!")
            await SpamBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 1 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot1"
            SpamBot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass

    if BOT_TOKEN2:
        print("Working On Bot Token 2!")
        try:
            SpamBot2 = TelegramClient("HellSpamBot2", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 2 OK!")
            await SpamBot2.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 2 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot2"
            SpamBot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot2.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass

    
    if BOT_TOKEN3:
        print("Working On Bot Token 3!")
        try:
            SpamBot3 = TelegramClient("HellSpamBot3", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 3 OK!")
            await SpamBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 3 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot3"
            SpamBot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            pass

    if BOT_TOKEN4:
        print("Working On Bot Token 4!")
        try:
            SpamBot4 = TelegramClient("HellSpamBot4", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 4 OK!")
            await SpamBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 4 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot4"
            SpamBot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            pass
    
    if BOT_TOKEN5:
        print("Working On Bot Token 5!")
        try:
            SpamBot5 = TelegramClient("HellSpamBot5", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 5 OK!")
            await SpamBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 5 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot5"
            SpamBot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            pass

       
     if BOT_TOKEN6:
       print("Working On Bot Token 6!")
        try:
            SpamBot6 = TelegramClient("HellSpamBot6", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 6 OK!")
            await SpamBot6.start(bot_token=BOT_TOKEN6)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 6 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot6"
            SpamBot6 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot6.start(bot_token=BOT_TOKEN6)
        except Exception as e:
            pass

   
       if BOT_TOKEN7:
        print("Working On Bot Token 7!")
        try:
            SpamBot7 = TelegramClient("HellSpamBot7", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 7 OK!")
            await SpamBot7.start(bot_token=BOT_TOKEN7)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 7 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot7"
            SpamBot7 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot7.start(bot_token=BOT_TOKEN7)
        except Exception as e:
            pass


     
       if BOT_TOKEN8:
        print("Working On Bot Token 8!")
        try:
            SpamBot8 = TelegramClient("HellSpamBot8", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 8 OK!")
            await SpamBot8.start(bot_token=BOT_TOKEN8)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 8 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot8"
            SpamBot8 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot8.start(bot_token=BOT_TOKEN8)
        except Exception as e:
            pass


   
       if BOT_TOKEN9:
        print("Working On Bot Token 9!")
        try:
            SpamBot9 = TelegramClient("HellSpamBot9", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 9 OK!")
            await SpamBot9.start(bot_token=BOT_TOKEN9)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 9 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot9"
            SpamBot9 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot9.start(bot_token=BOT_TOKEN9)
        except Exception as e:
            pass




       if BOT_TOKEN10:
        print("Working On Bot Token 10!")
        try:
            SpamBot10 = TelegramClient("HellSpamBot10", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 10 OK!")
            await SpamBot10.start(bot_token=BOT_TOKEN10)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 10 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "HellSpamBot10"
            SpamBot10 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await SpamBot10.start(bot_token=BOT_TOKEN10)
        except Exception as e:
            pass


            
loop = asyncio.get_event_loop()

loop.run_until_complete(main())
