import subprocess
from lib import execGet, findExec, pidOf


name = 'Clipman'
server = "wl-paste"
client = 'clipman'

def canStart():
    return bool(findExec(server)) and bool(findExec(client))

def isRunning():
    return bool(pidOf(server))

def isEnabled():
    return canStart() and isRunning()

def start():
    if not isRunning():
        subprocess.call([server, '-t', 'text', '--watch', client, 'store'])

def add(text):
    subprocess.call(['wl-copy', text])

def getHistory():
    return execGet(client, 'pick', '--tool=STDOUT', '--max-items=25', '--print0').split('\x00')
