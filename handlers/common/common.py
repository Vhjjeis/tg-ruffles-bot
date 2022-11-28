from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import *
import asyncio, datetime, os
from loader import dp
from db import *
from .texts import *


@dp.message_handler()
async def message_default(message: types.Message):
    await message.reply(DEFAULT_TEXT)

    
@dp.callback_query_handler(lambda call: call.data.split()[0] == "take_ruffle")
async def message_take_ruffle(call: types.CallbackQuery):
    r_id = call.data.split()[-1]
    user_id = call.from_user.id
    name = call.from_user.full_name
    username = call.from_user.username
    if is_user_ruffle(user_id, r_id):
        await call.answer("Ты уже участвуешь!")
    else:
        new_user_ruffle(user_id, name, username, r_id)
        await call.answer("Удачииииииии")