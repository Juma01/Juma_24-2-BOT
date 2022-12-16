from aiogram import types, Dispatcher
from config import bot, ADMINS
import random


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не мой начальник!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} ты забанен"
                                 f"{message.reply_to_message.from_user.first_name}")
    else:
        await message.answer("Пиши в группе!")


async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не имеешь права.')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} ты забанен"
                                 f"{message.reply_to_message.from_user.first_name}")
    else:
        await message.answer("Пиши в группе!")


async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        g = ['🎲', '🎯', '🏀', '⚽', '🎳', '🎰']
        r = random.choice(g)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message('Не возможно!')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(game, commands=['game'], commands_prefix='!/')