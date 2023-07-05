"""
This is a echo bot.
It echoes any incoming text messages.
"""

# import logging

from aiogram import Bot, Dispatcher, types
# for run as module
from bot.src.settings import BOT_TOKEN
# for run as script
# from src.settings import BOT_TOKEN

# API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
# logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
