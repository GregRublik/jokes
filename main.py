import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
import os

TOKEN = ""
dp = Dispatcher()


@dp.message(Command('off'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Windows off")
    os.system("shutdown /s /t 60")


@dp.message(Command('reboot'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Windows reboot")
    os.system("shutdown /r /t 60")


@dp.message(Command('cancel'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Windows reboot")
    os.system("shutdown /a")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stop!')
