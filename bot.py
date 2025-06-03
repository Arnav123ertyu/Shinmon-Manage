from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, API_ID, API_HASH, SHORTENER_API, ADMINS
from admin import is_admin, admin_commands
from utils import generate_short_link, get_custom_buttons
import asyncio

bot = Client("invite_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    buttons = get_custom_buttons()
    await message.reply("Choose what you want:", reply_markup=InlineKeyboardMarkup(buttons))

@bot.on_callback_query()
async def handle_button(client, callback_query):
    data = callback_query.data
    short_link = generate_short_link(f"https://t.me/{data}")
    await callback_query.message.reply(f"Join the channel:\n{short_link}")

@bot.on_message(filters.command(["addadmin", "removeadmin"]) & filters.user(ADMINS))
async def admin_manage(client, message):
    await admin_commands(client, message)

# Run the bot
bot.run()
