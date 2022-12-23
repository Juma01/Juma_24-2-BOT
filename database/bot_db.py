import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('База данных подключина!')

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY, name TEXT,"
               "direction TEXT, age INTEGER, groups TEXT)")

    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()  # [(), (), (), (),]
    random_user = random.choice(result)    # ()
    await message.answer(f"Ваш ID: {random_user[0]},\n Ваше имя: {random_user[1]},\n "
                         f"Вам: {random_user[3]} лет,\n Ваше направление: {random_user[2]}\n"
                         f"Ваша группа: {random_user[4]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()

