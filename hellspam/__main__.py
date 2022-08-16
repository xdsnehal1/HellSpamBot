import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5

def load_plugs(plugname):
    modules = Path(f"spambot/plugins/{plugname}.py")
    myfiles = f"spambot.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["spambot.plugins." + plugname] = load
    print("MafiaSpamBot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "spambot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import hellspam
import hellspam.userNeeds
import hellspam.help
import hellspam.helpers.callbackQuery

print("\n\nHell Spam Bot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        SpamBot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot5.disconnect()
    except Exception as e:
        print(e)
        pass
   try:
        SpamBot6.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot7.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot8.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot9.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot10.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        SpamBot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
     try:
        SpamBot6.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot7.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot8.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot9.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        SpamBot10.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
