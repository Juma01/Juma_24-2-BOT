from aiogram import types, Dispatcher
from config import bot, dp


# @dp.message_handler()
async def echo(message: types.Message):
    if message.chat.type != 'private':
        bad_words = ["дурак", "придурок", "чмо", "болван", ]
        for word in bad_words:
            if word in message.text.lower().replace(" ", ""):
                await bot.delete_message(message.chat.id, message.message_id)
                await message.answer(f"Сам ты {word.upper()}!\n"
                                     f"Не матерись {message.from_user.first_name}")

    if message.text.startswith("."):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'dice':
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        print(a.dice.value)

    if message.text.isdigit():
        await bot.send_message(chat_id=message.from_user.id, text=int(message.text) ** 2)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=str(message.text))


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)