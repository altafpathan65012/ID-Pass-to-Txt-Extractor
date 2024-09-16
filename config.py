import os

api_id = 23031620
api_hash = os.environ.get("API_HASH", "31cb00c1cbe580394778b43105864bca")
bot_token = os.environ.get("BOT_TOKEN", "6865731231:AAEDdXn48VOzOf0jRo0CvxkU0VxIFsikTvg")
auth_users = os.environ.get("AUTH_USERS", "502980590")
sudo_users = [int(num) for num in auth_users.split("502980590")]
osowner_users = os.environ.get("OWNER_USERS", "502980590")
owner_users = [int(num) for num in osowner_users.split("502980590")]
