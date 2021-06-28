import logging


from dotenv import load_dotenv
from os import getenv

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor

from aiogram.types import Message
from aiogram.types import InputFile

from util import putTextOnImage

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
    await message.reply("Hi, I'm PictureBot!\nBelow, you can send me your text :)\nPowered by @Yoshlik_media.")


@dp.message_handler()
async def cont_type_photo(message: Message):
    await message.reply(text='Please wait 15 seconds 💬')
    putTextOnImage(message=message)
    photo_bytes = InputFile(path_or_bytesio='upld_photos/Done.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_bytes,
                         caption=f'Success "{message.text}" 🎉')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
