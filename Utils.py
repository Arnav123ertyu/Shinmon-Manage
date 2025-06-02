import requests
from config import SHORTENER_API
from pymongo import MongoClient
from config import MONGO_URI

db = MongoClient(MONGO_URI).bot_data

def generate_short_link(long_url):
    try:
        api_url = f"{SHORTENER_API}{long_url}"
        response = requests.get(api_url).json()
        return response.get("shortenedUrl", long_url)
    except Exception:
        return long_url

def get_custom_buttons():
    data = db.buttons.find()
    buttons = [[InlineKeyboardButton(d["label"], callback_data=d["channel"])] for d in data]
    return buttons or [[InlineKeyboardButton("Demo Channel", callback_data="demochannel")]]
