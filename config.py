import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7127264663:AAHa4GxnZamOfSOZbLHvHOIzdarLJiYXWoY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29529959"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1f48164aeaf9ce697b01caf1eabe39f2")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1959020300"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://nxlanil12:Q15sJnlKGwDSAbgb@cluster0.cdzal.mongodb.net/") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
