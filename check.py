import os
import sys
import subprocess
from color import *
from userUtils import *

def entries(console,commands):

    cmd = {

       "check": lambda path,args:log("ok"),
       "ping": lambda path, args: subprocess.call(["ping", "-c", "4", args[0]] if len(args) > 0 else warn("Please provide a hostname or IP")),
        "ifconfig": lambda path, args: subprocess.call("ipconfig" if os.name == "nt" else "ifconfig", shell=True),
       }
    return [cmd,{}]