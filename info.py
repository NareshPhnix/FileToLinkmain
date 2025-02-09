import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Scorp')
API_ID = int(environ.get('API_ID', '28192191'))
API_HASH = environ.get('API_HASH', '663164abd732848a90e76e25cb9cf54a')
BOT_TOKEN = environ.get('BOT_TOKEN', "7146585357:AAHLUThDLRlAVtuGFg6g_28lgsv3Z41I7MU")
PICS = (environ.get('PICS', 'TechVJ/6145711370507764896.jpg')).split()
# Bot settings
PORT = environ.get("PORT", "8080")

# Online Stream and Download
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Admins, Channels & Users
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002231458694'))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://files1:q!gY3A$3fRCC#8W@file1.2sok7.mongodb.net/?retryWrites=true&w=majority&appName=File1")
DATABASE_NAME = environ.get('DATABASE_NAME', "files1")

# Shortlink Info
SHORTLINK = bool(environ.get('SHORTLINK', False)) # Set True Or False
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
