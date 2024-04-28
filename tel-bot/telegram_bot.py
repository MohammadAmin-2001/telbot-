from telegram import Update
from telegram.ext import MessageHandler, Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
from os import getenv


class Telegram:

    def __init__(self):
        load_dotenv()
        self.__token = getenv("TELEGRAM_TOKEN")
        self.__tel_username = getenv("TELEGRAM_USERNAME")

    @property
    def token(self):
        return self.__token

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await (
            context.bot.send_message
            (
              chat_id=update.effective_chat.id,
              text=f"hello {update.effective_user.full_name}",
              reply_to_message_id=update.effective_message.id)
        )


def main() -> None:
    tel_instance = Telegram()
    app = Application.builder().token(tel_instance.token).build()
    start_command = CommandHandler("start", tel_instance.start)
    app.add_handler(start_command)
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()

