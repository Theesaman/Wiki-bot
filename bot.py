import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from wiki import wiki

TOKEN = ""

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Assalomu aleykum  {full_name}, Botimizga xush kelibsiz 👋🏻, Bu bot xoxlagan Savolingizga javob beradi. Ishonmasangiz sinab ko'ring"
    await message.reply(text)

@dp.message(F.text)
async def wikipedia(message : Message):
    await message.reply(wiki(message.text))

async def main():
    global bot
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
