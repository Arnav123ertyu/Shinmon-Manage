from pyrogram.types import Message
from config import ADMINS
from pymongo import MongoClient
from config import MONGO_URI

db = MongoClient(MONGO_URI).bot_data

def is_admin(user_id):
    return user_id in ADMINS or db.admins.find_one({"user_id": user_id}) is not None

async def admin_commands(client, message: Message):
    if message.command[0] == "addadmin":
        try:
            uid = int(message.text.split()[1])
            db.admins.insert_one({"user_id": uid})
            await message.reply(f"Added user {uid} as admin.")
        except:
            await message.reply("Usage: /addadmin <user_id>")
    elif message.command[0] == "removeadmin":
        try:
            uid = int(message.text.split()[1])
            db.admins.delete_one({"user_id": uid})
            await message.reply(f"Removed user {uid} from admin.")
        except:
            await message.reply("Usage: /removeadmin <user_id>")
