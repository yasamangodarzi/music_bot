from telegram.ext import *
import Responses as rep
from Constant import API_KEY


print("bot started...")
def start_command(update, context):
    update.message.reply_text("Hello,Welcome to the Bot.Please write\
/help to see the commands available.")


def help_command(update, context):
    update.message.reply_text("please enter your request in this format:\nجدید+اسم خواننده +بانام+اسم اهنگ")


def handle_command(update, context):
    text = str(update.message.text).lower()
    respon = rep.work(text)
    update.message.reply_text(respon)


def error_condition(update, context):
    print(f"{update} have a error {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start_command))
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_command))
    updater.dispatcher.add_error_handler(error_condition)
    updater.start_polling(timeout=3000)
    updater.idle()



main()
