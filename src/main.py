import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['кот'])
async def send_cat(message: types.Message):
    await message.answer("I Send cat there!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)