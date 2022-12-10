# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/Prmoviesrequestsbot'>Pr Movie Request Bot</a> is an open source project.

    Devs: 
        <a href='https://t.me/TheKunalSiingh'>❤️ Kunal Singh ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Prmoviesrequestsbot'>Link Search BOT</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/TheKunalSiingh'>Kunal Singh</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello! {}

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

"""


    START_MSG = """
<b>Hello! {}

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

"""

