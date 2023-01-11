import json
import logging
import os
import aiohttp
from urllib.parse import quote

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
# Configure logging

logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def get_cat_url(text:str=None, gif:bool=None) -> str:
    if text:  
        text = f'/s/{quote(text)}'
    gif = '/gif' if gif else ''
    query_url = f'https://cataas.com/c{gif}{text}?json=true'
    async with aiohttp.ClientSession() as session:
        async with session.get(query_url) as resp:
            if resp.status == 200:
                data = await resp.read()
                data = json.loads(data)
    return f"https://cataas.com{data['url']}"
       
@dp.message_handler(commands=['кот', 'cat'])
async def send_cat(message: types.Message) -> None:
    url = await get_cat_url(text=message.get_args())
    await bot.send_photo(photo=url, chat_id=message.chat.id)

@dp.message_handler(commands=['котгиф', 'catgif'])
async def send_cat(message: types.Message):
    url = await get_cat_url(text=message.get_args(), gif=True)
    await bot.send_animation(animation=url, chat_id=message.chat.id)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)