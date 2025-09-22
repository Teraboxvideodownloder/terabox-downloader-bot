import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

BOT_TOKEN = os.getenv("8402287406:AAF2JK0vZgLHzCMggkXl9PH_KXiTnoShFQM")

# Dummy TeraBox API (example) – नंतर याला actual API/logic ने replace करायचं
def get_terabox_download_link(url: str) -> str:
    # येथे तुझं API logic टाक
    return f"✅ Here is your TeraBox download link:\n{url.replace('1024terabox.com', 'download.terabox.com')}"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! Send me any TeraBox link and I’ll give you the download link.")

# Handle terabox links
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "terabox.com" in text:
        link = get_terabox_download_link(text)
        await update.message.reply_text(link)
    else:
        await update.message.reply_text("❌ Please send a valid TeraBox link.")

def main():
    app = Application.builder().token(8402287406:AAF2JK0vZgLHzCMggkXl9PH_KXiTnoShFQM).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
