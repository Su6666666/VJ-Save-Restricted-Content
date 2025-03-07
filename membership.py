from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from database import db
from info import OWNER, BOT_NAME, BOT_USERNAME

@Client.on_message(filters.command("subscribe") & filters.private)
async def subscribe(bot, message):
    user_id = message.from_user.id
    if db.is_subscribed(user_id):
        await message.reply("You are already subscribed!")
    else:
        db.subscribe(user_id)
        await message.reply("You have successfully subscribed!")

@Client.on_message(filters.command("unsubscribe") & filters.private)
async def unsubscribe(bot, message):
    user_id = message.from_user.id
    if db.is_subscribed(user_id):
        db.unsubscribe(user_id)
        await message.reply("You have successfully unsubscribed!")
    else:
        await message.reply("You are not subscribed!")

@Client.on_message(filters.command("premium") & filters.private)
async def premium(bot, message):
    user_id = message.from_user.id
    if db.is_premium(user_id):
        await message.reply("You are already a premium member!")
    else:
        await message.reply("You are not a premium member. Subscribe to our premium plan to access exclusive features!")

def get_premium_buttons():
    buttons = [
        [InlineKeyboardButton("Subscribe", callback_data="subscribe")],
        [InlineKeyboardButton("Unsubscribe", callback_data="unsubscribe")]
    ]
    return InlineKeyboardMarkup(buttons)

@Client.on_callback_query(filters.regex(r"^subscribe$"))
async def subscribe_callback(bot, query):
    user_id = query.from_user.id
    if db.is_subscribed(user_id):
        await query.answer("You are already subscribed!")
    else:
        db.subscribe(user_id)
        await query.answer("You have successfully subscribed!")

@Client.on_callback_query(filters.regex(r"^unsubscribe$"))
async def unsubscribe_callback(bot, query):
    user_id = query.from_user.id
    if db.is_subscribed(user_id):
        db.unsubscribe(user_id)
        await query.answer("You have successfully unsubscribed!")
    else:
        await query.answer("You are not subscribed!")
