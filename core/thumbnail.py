from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import db

@Client.on_message(filters.command(["setthumb"]) & filters.private)
async def set_thumbnail_cmd(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply_text("Please reply to an image with /setthumb to set it as your custom thumbnail.")
        return

    thumbnail_file_id = message.reply_to_message.photo.file_id
    try:
        await db.set_thumbnail(message.from_user.id, thumbnail_file_id)
        await message.reply_text("Custom thumbnail saved successfully! It will be used for future forwards where applicable.")
    except Exception as e:
        await message.reply_text(f"Error saving thumbnail: {e}")

@Client.on_message(filters.command(["delthumb"]) & filters.private)
async def delete_thumbnail_cmd(client: Client, message: Message):
    try:
        await db.set_thumbnail(message.from_user.id, None) # Set to None to delete
        await message.reply_text("Custom thumbnail removed. Default thumbnails will be used.")
    except Exception as e:
        await message.reply_text(f"Error deleting thumbnail: {e}") 