from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import client_kb


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type != "private":
        await FSMAdmin.id.set()
        await message.answer("Ваш id ?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личку!")


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = message.bot.id
    await FSMAdmin.next()
    await message.answer("Ваше имя ?", reply_markup=client_kb.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text.capitalize()
    await FSMAdmin.next()
    await message.answer("Ваше Направление?", reply_markup=client_kb.cancel_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text.upper()
    await FSMAdmin.next()
    await message.answer("Ваш возраст?", reply_markup=client_kb.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif int(message.text) < 16 or int(message.text) > 50:
        await message.answer("Возростное ограничинеие.")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Ваша группа ?", reply_markup=client_kb.cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"Ваш ID: {data['id']}, Ваше имя: {data['name']},\n "
                             f"Вам:{data['age']} лет,Ваше направление: {data['direction']}\n"
                             f"Ваша группа: {data['group']}")
    await FSMAdmin.next()
    await message.answer("Всё верно?", reply_markup=client_kb.submit_markup)


async def submit_fsm(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # запись в базу данных
        await state.finish()
        await message.answer('ВСЁ!')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отменено !')
    else:
        await message.answer('Команда не верна.')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено !')


def register_handlers_fsmAdminMentor(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit_fsm, state=FSMAdmin.submit)











