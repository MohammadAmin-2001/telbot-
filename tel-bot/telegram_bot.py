from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv
from os import getenv
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


class Telegram:

    def __init__(self):
        load_dotenv()
        self.__token = getenv("TELEGRAM_TOKEN")
        self.__tel_username = getenv("TELEGRAM_USERNAME")

    @property
    def token(self):
        return self.__token

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        keys = [
            [
                KeyboardButton(text="show my jobs"),
                KeyboardButton(text="insert my jobs"),
                 ]
                ]
        markup = ReplyKeyboardMarkup(
            keyboard=keys,
            resize_keyboard=True,
            one_time_keyboard=True,
            input_field_placeholder="Please selecet your order :)"
        )
        await (
            context.bot.send_message
            (
              chat_id=update.effective_chat.id,
              text=f"hello {update.effective_user.full_name} how can i do for you?",
              reply_to_message_id=update.effective_message.id,
              reply_markup=markup
            )
        )


def main() -> None:
    tel_instance = Telegram()
    app = Application.builder().token(tel_instance.token).build()

    app.add_handlers(
        [
            CommandHandler("start", tel_instance.start_command)
        ]
    )
    app.run_polling()


if __name__ == "__main__":
    main()
