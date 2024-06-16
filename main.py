import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import kb
import volume
import os

TOKEN = ""
dp = Dispatcher()


@dp.message(Command('start'))
async def command_start(message: Message) -> None:
    await message.answer('Выберите что необходимо сделать с пк', reply_markup=kb.start)


@dp.callback_query(F.data == 'off')
async def command_off(callback: CallbackQuery) -> None:
    await callback.answer(f"Windows выключится через минуту!")
    os.system("shutdown /s /t 60")


@dp.callback_query(F.data == 'reboot')
async def command_start_handler(callback: CallbackQuery) -> None:
    await callback.answer(f"Windows reboot")
    os.system("shutdown /r /t 60")


@dp.callback_query(F.data == 'cancel')
async def command_start_handler(callback: CallbackQuery) -> None:
    await callback.answer(f"Cancel off or reboot Windows")
    os.system("shutdown /a")
    await callback.message.delete()


@dp.callback_query(F.data == 'volume')
async def command_volume(callback: CallbackQuery) -> None:
    await callback.message.edit_text(f"Текущий уровень громкости: {int(100*volume.volume_remove())}%", reply_markup=kb.volume)


@dp.callback_query(F.data == 'volume_plus')
async def command_volume_plus(callback: CallbackQuery):

    level = volume.volume_remove()
    if level + 0.1 < 1:
        await callback.answer('Громкость прибавлена')
        level = volume.volume_remove(level + 0.1)
        await callback.message.edit_text(f'Текущий уровень громкости: {int(100 * level)}%', reply_markup=kb.volume)
    else:
        await callback.answer('Достигнута максимальная громкость')


@dp.callback_query(F.data == 'volume_minus')
async def command_volume_minus(callback: CallbackQuery):

    level = volume.volume_remove()
    if level - 0.1 > 0:
        await callback.answer('Громкость убавлена')
        level = volume.volume_remove(level - 0.1)
        await callback.message.edit_text(f'Текущий уровень громкости: {int(100 * level)}%', reply_markup=kb.volume)
    else:
        await callback.answer('Без звука!')


@dp.callback_query(F.data == 'volume_exit')
async def command_volume_minus(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберите что необходимо сделать с пк', reply_markup=kb.start)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stop!')
