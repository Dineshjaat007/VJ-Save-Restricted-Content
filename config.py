import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27022010"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b274c3bd0155821cee4f33025f0b4584")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://TejalSarkar:Tejalgovt2003@atlascluster.2b87a.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")
