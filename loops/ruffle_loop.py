import asyncio, datetime, random
from keyboards import *
from db import *
from loader import bot

def get_format_day(value):
    words = ['день', 'дня', 'дней']
    if all((value % 10 == 1, value % 100 != 11)):
        return words[0]
    elif all((2 <= value % 10 <= 4,
            any((value % 100 < 10, value % 100 >= 20)))):
        return words[1]
    return words[2]


def date_to_str(date):
    new_date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M") - datetime.datetime.now()
    d = new_date.days
    h, rem = divmod(new_date.seconds, 3600)
    m, s = divmod(rem, 60)
    
    f = lambda x: str(x).rjust(2, "0")
    str_day = get_format_day(d)
    h, m, s = f(h), f(m), f(s)
    if d != 0:
        return f"{d} {str_day}, {h}:{m}:{s}"
    return f"{h}:{m}:{s}"


async def thread_ruffles():
    while True:
        ruffles = get_ruffles(active=True)
        for ruffle in ruffles:
            try:
                r_id, text, button, date, value_wins, chat_id, message_id, active = ruffle
                users = get_users_ruffle(r_id)
                if message_id == -1:
                    continue
                date_ruffle = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
                if datetime.datetime.now() > date_ruffle:
                    text_ruffle = text\
                        + "\n\nПриняло участие: " + str(len(users))\
                        + "\nРозыгрыш завершен, результаты нижееее"
                    text_ruffle_2 = "<b>Итоги:</b>"
                    text_adm = f"suc ruffle #{r_id}"
                    for i in range(12):
                        random.shuffle(users)
                    p_win = int(value_wins) / len(users) * 100
                    
                    for i in range(int(value_wins)):
                        if i >= len(users):
                            break
                        _uid, _idr, user_id, name, username = users[i]
                        username = f"@{username}" if str(username) != "None" else ""
                        text_ruffle_2 += f"\n{i + 1}| <a href='tg://user?id={user_id}'>{name}</a> {username}"
                        text_adm += f"\n{i + 1}| <a href='tg://user?id={user_id}'>{user_id}</a> {name}  {username}"
                    text_ruffle_2 += f"\n\nВ розыгрыше приняло участие: {len(users)}\nШанс победы составлял {p_win}%"
                    
                    await bot.send_message(chat_id, text_ruffle_2, reply_to_message_id=message_id)
                    await bot.edit_message_text(text=text_ruffle,
                                                chat_id=chat_id,
                                                message_id=message_id) 
                    admins = get_admins()
                    for admin in admins:
                        await bot.send_message(admin[0], text_adm)
                    
                    update_active_ruffle(r_id)


                else:
                    text_ruffle = text\
                        + "\n\n</b>Участвует челиков: </b><code>" + str(len(users)) + "</code>"\
                        + "\n</b>До конца розыгрыша: </b><code>" + date_to_str(date) + "</code>"
                    await bot.edit_message_text(text=text_ruffle,
                                                chat_id=chat_id,
                                                message_id=message_id,
                                                reply_markup=get_ruffle_keyboard(button, r_id))
            except:
                pass
        await asyncio.sleep(random.randint(4, 6)) 