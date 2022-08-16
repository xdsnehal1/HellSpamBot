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

       
 

            
loop = asyncio.get_event_loop()

loop.run_until_complete(main())
