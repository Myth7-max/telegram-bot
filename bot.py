from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Bot is running 24/7 ✅")

TOKEN = "8126503625:AAF-3XtqEFXnANDzhSp4LbQNgWbYPhHp99Y"

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
