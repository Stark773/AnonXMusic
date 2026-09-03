from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("34766709", 0))
        self.API_HASH = getenv("c70063901bc81555174389982a394f95")

        self.BOT_TOKEN = getenv("8564248095:AAFiWork440KzNNQA9-9D3GdVOIl7lpruIU")
        self.MONGO_URL = getenv("mongodb+srv://deidaraasui12_db_user:lFMu0uvvRI5Kv86r@stark.yrjtl3r.mongodb.net/?appName=Stark")

        self.LOGGER_ID = int(getenv("-1002488365579", 0))
        self.OWNER_ID = int(getenv("7732395523", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "AQISf3UAHxJ2ld_srxRWoB9XD7IPGHoqUvpkiNllSexSx06WtSlc_OzqhEC3dtumFwmekChIv_Nhz4pT4uCLLvdq0PW6fOyTw2-nl5J6tyOXwYyTWm6D6gxIO_1i9CXsHFwJMGH90kqwTR_kW44izEBd2UF2M9urNsAcW3ncKo7qWweOsDQzOA_64DY6H-OLQhVcsddX5pArwA1q9KvwKOOQ6NX2Eu3NiG7z8eVxFS7pQpffu5hpK4nkJ_9hRf3yLKh427OXWfxLWJhSm7v_3YR7SrrPm97Mt6l4P9sFzZPfUqDf8bApZU7CPsX558vMHoItvzpopkNuQQdj5OJVlq9B2bMBzAAAAAHfzIkMAA)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fallenx")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
