from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20931062")
    API_HASH = environ.get("API_HASH", "3e9182704531b9dd6c91745cc2965a97")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7180910345") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '525792934').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
