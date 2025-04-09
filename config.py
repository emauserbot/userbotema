import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))
DEVS = list(map(int, os.getenv("DEVS", "7884451584").split()))
API_ID = int(os.getenv("API_ID", "19117304"))
API_HASH = os.getenv("API_HASH", "8357f87acf32c5bc92f0dda9235582c1")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8069297897:AAG9rl5VPj97etYaSeoch5uN7JswuU-hoqk")
OWNER_ID = int(os.getenv("OWNER_ID", "7884451584"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))
RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://lifive5703:1@cluster0.qtfcx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))
API_KEY = os.getenv("API_KEY", "Fieyzzz")
USER_GROUP = os.getenv("USER_GROUP", "@userbotpremusd")
