import asyncio
import logging
import sys
from Bard import AsyncChatbot
from aiogram import Bot, types, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart 
from environs import Env

env = Env()
env.read_env()

secure_1PSID = env('SECURE_1PSID')
secure_1PSIDTS = env('SECURE_1PSIDTS')
TOKEN = env('BOT_TOKEN')

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Привет, {message.from_user.full_name} меня зовут Google Bard — я являюсь большой языковой моделью, которая может генерировать текст, переводить языки, писать разные виды творческого контента и отвечать на ваши вопросы информативным образом.")


@dp.message()
async def send(message: types.Message) -> None:
    try:
        chatbot = await AsyncChatbot.create(secure_1PSID, secure_1PSIDTS)
        await message.answer('Google Bard думает...🧠')
        answer = await chatbot.ask(message.text)
        await message.answer(answer.get('content'), parse_mode=ParseMode.MARKDOWN)
    except:
        await message.answer('Ой что-то пошло не так!')


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
