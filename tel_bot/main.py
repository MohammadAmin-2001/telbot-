from telegram.ext import Application, CommandHandler
from telegram_.telegram_bot import  Telegram


def main() -> None:
    tel_instance = Telegram()
    app = Application.builder().token(tel_instance.token).build()

    app.add_handlers(
        [
            CommandHandler("start", tel_instance.start_command)
        ]
    )
    # bot.add_error_handler(tel_instance.error_handler)
    app.run_polling()


if __name__ == "__main__":
    main()
