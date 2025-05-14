# Delta1 Save Restricted Bot

*A powerful Telegram Bot that lets you save and forward restricted content using post links with login functionality.*

![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)

## 🌟 Features

- **Login System**: Use your Telegram account to access restricted content
- **Support for Multiple Sources**: Public chats, private chats, and bot chats
- **Batch Processing**: Download multiple posts at once
- **Custom Thumbnails**: Set your own thumbnail for forwarded media
- **Word Filtering**: Block messages containing specific words/phrases
- **Smart Delay System**: Prevents rate limiting with intelligent delays

---

## 📋 Environment Variables

- `API_HASH` : Your API Hash from [Telegram Website](https://my.telegram.org)
- `API_ID` : Your API ID from [Telegram Website](https://my.telegram.org)
- `BOT_TOKEN` : Your Bot Token from [BotFather](https://telegram.me/BotFather)
- `ADMINS` : Your Admin ID for Broadcasting Message
- `DB_URI` : Your MongoDB Database URL (Warning: set in deploy environment, not in repo)
- `DB_NAME` : Your MongoDB Database Name
- `ERROR_MESSAGE` : Set True or False to enable/disable error messages
- `BLOCKED_WORDS` : Comma-separated list of words/phrases to block (optional)

---

## 🤖 Commands

- `/start` : Check if the bot is active
- `/help` : View instructions on how to use the bot
- `/login` : Login with your Telegram account
- `/logout` : Logout your current session
- `/cancel` : Cancel any ongoing task
- `/setthumb` : Set custom thumbnail (reply to an image)
- `/delthumb` : Remove your custom thumbnail
- `/broadcast` : Send message to all users (Admin only)

---

## 📝 Usage Guide

### For Public Chats
Simply send the post link:
```
https://t.me/channel_name/123
```

### For Private Chats
1. First send the invite link of the chat (not needed if your account is already a member)
2. Then send the post link:
```
https://t.me/c/1234567890/123
```

### For Bot Chats
Send link with '/b/', bot's username and message ID:
```
https://t.me/b/botusername/4321
```

### For Multiple Posts
Send links with "from - to" format:
```
https://t.me/xxxx/1001-1010
```
or
```
https://t.me/c/xxxx/101-120
```
*Note: Spaces between numbers don't matter*

---

## ⚙️ Deployment

### Using Render
1. Fork this repository
2. Create a new Web Service on Render pointing to your fork
3. Add all required environment variables
4. Deploy with the following settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python3 bot.py`

---

## 💡 Credits

- Thanks to [BipinKrish](https://github.com/bipinkrish) for the base repository
- Thanks to [Tech VJ](https://youtube.com/@tech_vj?feature=shared) for the original implementation and features
- Modified and enhanced by Delta1
