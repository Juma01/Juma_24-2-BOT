from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам алейкум {message.from_user.first_name}",
                           reply_markup=start_markup)
    # await message.answer("метод отправки сообщение туду откуда пришло")
    # await message.reply("метод ответа на конкретное сообщение")


async def help_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Салам алейкум {message.from_user.first_name}!\n'
                                f'{message.from_user.first_name}, Чем могу помочь ?\n'
                                f'/start - Запуск\n'
                                f'/help - Помощь\n'
                                f'/quiz - Викторина\n'
                                f'/mems - Мэмы')


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Что нужно сделать, чтобы правельно подготовиться к контрольной ?"
    answers = [
        'Написать шпаргалку',
        'Сесть с отличником',
        'Повторить заданную тему',
        'Заболеть и не прийти в школу',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Повторение, мать учение!",
        open_period=10,
        reply_markup=markup
    )


# @dp.message_handler(commands=['mems'])
async def mems(message: types.Message):
    mem_photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, mem_photo)


async def get_random_user(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mems, commands=['mems'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(get_random_user, commands=['get'])