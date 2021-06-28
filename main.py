import logging

import cv2

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor

from aiogram.types import Message
from aiogram.types import InputFile


load_dotenv()


API_TOKEN = getenv('BOT_API_TOKEN')

# print(getenv('API_TOKEN'))

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply("Hi!\nI'm PictureBot!\nPowered by @Yoshlik_media.")


@dp.message_handler()
async def cont_type_photo(message: Message):
    img = cv2.imread('down_photos/5415106.jpg')
    cv2.putText(img, message.text, (590, 1050), 7, 8, (255, 206, 92), 3)
    cv2.imwrite("upld_photos/Done.jpg", img)
    photo_bytes = InputFile(path_or_bytesio='upld_photos/Done.jpg')

    await bot.send_photo(chat_id=message.from_user.id, photo=photo_bytes, caption=message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
