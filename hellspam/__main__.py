import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from hellspam import *
from hellspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5, SpamBot6, SpamBot7, SpamBot8, SpamBot9, SpamBot10

def load_plugs(plugname):
    modules = Path(f"hellspam.plugins/{plugname}.py")
    myfiles = f"hellspam.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["hellspam.plugins." + plugname] = load
    print("Hell SpamBot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "hellspam/plugins/*.py"
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
