from telegram.ext import Updater, CommandHandler

TOKEN = "8126503625:AAFFadnlbCfF2nCnUylor27DM0CxU0Es26I"

def start(update, context):
    update.message.reply_text("Hello 👋 Bot is working!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
