import json
import logging
import os
import aiohttp

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
    data = dict()
    text = message.get_args()
    async with aiohttp.ClientSession() as session:
        if text:
            async with session.get(f'https://cataas.com/c/s/{text}?json=true') as resp:
                if resp.status == 200:
                    data = await resp.read()
        else:
            async with session.get('https://cataas.com/cat?json=true') as resp:
                if resp.status == 200:
                    data = await resp.read()
    j = json.loads(data)
    url = f"https://cataas.com{j['url']}"
    await bot.send_photo(photo=url, chat_id=message.chat.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)