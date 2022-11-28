from aiogram import types
from db import *


def get_ruffle_keyboard(text_button, ruffle_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text=text_button, 
        callback_data=f"take_ruffle {ruffle_id}"))
    return keyboard