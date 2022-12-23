from aiogram import types, Dispatcher
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
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


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не указ мне!")
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer(
                f"Ваш ID: {user[0]},\n Ваше имя: {user[1]},\n "
                                 f"Вам: {user[3]} лет,\n Ваше направление: {user[2]}\n"
                                 f"Ваша группа: {user[4]}",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f"delete {user[1]}",
                                                          callback_data=f"delete {user[0]}")
                                 ))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Удалено", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(game, commands=['game'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))