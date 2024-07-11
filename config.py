import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6848088729:AAHPHOlgLuJ1iYOpagm0_5-Ij2vTujc9raU")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24337419"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "88d260f06c2be30b5360e61a428c9c8f")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://cexifal284:cexifal284@cluster0.anea5dg.mongodb.net/?retryWrites=true&w=majority")
