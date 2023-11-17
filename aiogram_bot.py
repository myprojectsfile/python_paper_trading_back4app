from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode

class AiogramBot:
    def __init__(self, token, chat_id):
        self.bot = Bot(token=token)
        self.dp = Dispatcher(self.bot)
        self.chat_id = chat_id

    async def send_message(self, message):
        await self.bot.send_message(self.chat_id, message, parse_mode=ParseMode.MARKDOWN)

    def start_polling(self):
        executor.start_polling(self.dp, skip_updates=True)

    def register_message_handler(self, handler):
        self.dp.message_handler(handler)

# Define a handler function for text messages
async def echo(message: types.Message):
    # Reply to the message with the chat_id
    await message.reply(f"Your chat_id is {message.chat.id}")

# Example usage in another module:
if __name__ == "__main__":
    print("Starting Aiogram Bot")
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    TOKEN = '6545309020:AAFF0LPsrhSQyKVloSqjLx_C_Rw6NI39c6o'
    CHAT_ID = 173975362

    # Create an instance of AiogramBot
    my_bot = AiogramBot(token=TOKEN, chat_id=CHAT_ID)

    # Register the message handler
    my_bot.register_message_handler(echo)

    my_bot.send_message('Hi')
    # Start the bot
    my_bot.start_polling()
