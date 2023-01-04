import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("OK")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Пора учиться!")


async def scheduler():
    aioschedule.every().friday.tuesday.at("20:00").do(go_to_sleep)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: "go" in word.text)