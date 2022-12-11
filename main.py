from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам алейкум {message.from_user.first_name}")
    await message.answer("метод отправки сообщение туду откуда пришло")
    await message.reply("метод ответа на конкретное сообщение")


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(text="button_call_1")
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
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_2")
async def quiz_3(call: types.CallbackQuery):
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


@dp.message_handler(commands=['mems'])
async def mems(message: types.Message):
    mem_photo = open('media/mem.jpg', 'rb')
    await bot.send_photo(message.chat.id, mem_photo)


@dp.message_handler()
async def eho(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=str(message.text))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)