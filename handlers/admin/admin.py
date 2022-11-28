from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import *
import asyncio, datetime, os
from loader import dp
from db import *
from .funcs import *

# help
@dp.message_handler(lambda msg: is_admin(msg.from_user.id), commands='help')
async def message_help_admins(message: types.Message):
    await message.answer("""helperka

<b>-| ADMINS |-</b>
/get_admins
/new_admin [user_id]
/del_admin [user_id]

<b>-| RUFFLES |-</b>
/new_ruffle [text];[text_button];[date];[value winners];[chat_id]
---|date=2022-11-26 01:15
/get_ruffles [active=None]
---| active = 0 or 1
/get_users_ruffle [ruffle_id]
""")

# admins
@dp.message_handler(lambda msg: is_admin(msg.from_user.id), commands='get_admins')
async def message_get_admins(message: types.Message):
    admins = get_admins()
    text = "list admins:"
    for admin_id in admins:
        admin_id = admin_id[0]
        text += f"\n<a href='tg://user?id={admin_id}'>id{admin_id}</a>"
    await message.answer(text)


@dp.message_handler(lambda msg: is_admin(msg.from_user.id), commands='new_admin')
async def message_new_admin(message: types.Message):
    user_id = message.text.split()[-1]
    if user_id.isdigit():
        new_admin(user_id)
        await message.reply("suc!")
        return
    await message.reply("invalid")


@dp.message_handler(lambda msg: is_admin(msg.from_user.id), commands='del_admin')
async def message_del_admin(message: types.Message):
    user_id = message.text.split()[-1]
    if user_id.isdigit():
        del_admin(user_id)
        await message.reply("suc!")
        return
    await message.reply("invalid")


# ruffles
@dp.message_handler(lambda msg: is_admin(msg.from_user.id), commands='new_ruffle')
async def message_new_ruffle(message: types.Message):
    res = message.html_text[12:].split(';')
    text, text_button, date, value_winners, chat_id = res
    text_ruffle = text\
        + "\n\n<b>Участвует челиков:</b> <code>" + str(0) + "</code>"\
        + "\n<b>До конца розыгрыша:</b> <code>" + date_to_str(date) + "</code>"
    ruffle_id = new_raffle(text, text_button, date, value_winners, chat_id, -1)
    new_message = await message.bot.send_message(
        chat_id, 
        text_ruffle, 
        reply_markup=get_ruffle_keyboard(text_button, ruffle_id))
    await message.reply(f"suc ruffle_id = {ruffle_id}")
    update_message_id_for_ruffle_id(ruffle_id, new_message.message_id)



@dp.message_handler(lambda msg: is_admin(msg.from_user.id), commands='get_ruffles')
async def message_get_ruffles(message: types.Message):
    a = message.text.split()[-1]
    if a == "1":
        a = True
    elif a == "0":
        a = False
    else:
        a = None
    ruffles = get_ruffles(active=a)
    for ruffle in ruffles:
        ruffle_id, text, button, date, value_wins, chat_id, msg_id, active = ruffle
        await message.answer(f"\n{ruffle_id=}\n{text}\n{button=}\n{date=}\n{value_wins=}\n{chat_id=}\n{msg_id=}\n{active=}")


@dp.message_handler(lambda msg: is_admin(msg.from_user.id), commands='get_users_ruffle')
async def message_get_users_ruffle(message: types.Message):
    ruffle_id = message.text.split()[-1]
    if ruffle_id.isdigit():
        users = get_users_ruffle(ruffle_id)
        text = ""
        for user in users:
            n_user, _, user_id, name, username = user 
            text += f"\n<a href='tg://user?id={user_id}'>id{user_id}</a> {name} @{username}"
        await message.reply(text)
        return
    await message.reply("invalid")