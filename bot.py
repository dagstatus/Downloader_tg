import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
import base
import os
import config
import stats

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!\nДанный бот умеет скачить видео /help, '
                        'с Youtube и instagram!')


@dp.message_handler(commands=['numb'])
async def process_start_command(message: types.Message):
    dict_stats = stats.read_stats()
    await message.reply(f'Count of downloads - {str(dict_stats)}')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = 'Просто вставьте ссылку'
    await message.reply(msg)


@dp.message_handler()
async def echo(message: types.Message):
    try:
        await base.delete_local_file(message.chat.id)
    except:
        pass
    await message.reply('Видео скачивается...')
    await asyncio.sleep(1)
    res_msg = await base.dwld(message.text, message.chat.id)
    await message.reply(res_msg)
    await message.reply_video(video=open(f'temp/{message.chat.id}.mp4', 'rb'), caption='dagstatusbot')
    await asyncio.sleep(5)
    await base.delete_local_file(message.chat.id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
