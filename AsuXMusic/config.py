from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", "20865323"))
API_HASH = getenv("API_HASH", "3dce0c91cda24747656e704808a684e8")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Grab_Your_WH_Group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "WOFBotsUpdates")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5332414680").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1103636187").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/77d94f66f1aa463271275.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/2a91f50d54e57b4a7c7f6.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/3a3c0b8e2b09b1dd45967.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/f4ad53346acfe3f334a55.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/69a4a8c4407981fcb3f3d.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/f589ebcdae6f2f294dd2e.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
