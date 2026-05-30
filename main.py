import logging
import wikipedia
from aiogram import Dispatcher, Bot, types
from aiogram.filters import Command
import asyncio

wikipedia.set_lang('uz')

API_TOKEN = 'your_telegram_bot_token_here'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start', 'help'))
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nThis project was created and developed by Muhammadbilol.@IT_MENTOR_UZ")


@dp.message()
async def send_wiki(message: types.Message):
    try:
        response = wikipedia.summary(message.text)
        if len(response) > 4095:
            for x in range(0, len(response), 4095):
                await message.answer(response[x:x+4095])
        else:
            await message.answer(response)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi!')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
