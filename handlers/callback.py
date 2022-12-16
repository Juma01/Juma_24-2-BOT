from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp


# @dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_1)
    question = "Сколько цветов у радуги ?"
    answers = [
        '8',
        '6',
        '3',
        '7',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="7",
        open_period=10,
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_3")
    markup.add(button_call_1)
    question = "Сколько будет ?"
    answers = [
        '4',
        '18',
        '16',
        '5',
        '12',
    ]
    photo = open('media/fruits.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="16",
        open_period=10,
        reply_markup=markup,
    )


# @dp.callback_query_handler(text="button_call_3")
async def quiz_4(call: types.CallbackQuery):
    question = "Ответ"
    answers = [
        '4',
        '8',
        '4, 6',
        '5',
        '2, 4',
    ]
    photo = open('media/cod.png', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="2, 4",
        open_period=10,
    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
    dp.register_callback_query_handler(quiz_4, text="button_call_3")

