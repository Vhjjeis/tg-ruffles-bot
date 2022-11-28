from db.loader_db import *
 
# ruffles
def new_raffle(text, button, date, value_wins, chat_id, message_id):
    cur.execute(f'INSERT INTO raffles(text, button, date, value_wins, chat_id, message_id, active) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (text, button, date, value_wins, chat_id, message_id, 1))
    raffle_id = cur.execute('select id from raffles').fetchall()[-1][0]
    conn.commit()
    return raffle_id


def get_ruffles(active=None):
    if active == None:
        res = cur.execute(f'SELECT * FROM raffles').fetchall()
    elif active == True:
        res = cur.execute(f'SELECT * FROM raffles where active = 1').fetchall()
    else:
        res = cur.execute(f'SELECT * FROM raffles where active = 0').fetchall()
    return res


def del_ruffle(ruffle_id):
    cur.execute(f'delete from raffles where id = ?', (ruffle_id,))
    conn.commit()


def update_message_id_for_ruffle_id(raffle_id, message_id):
    cur.execute(f"update raffles set message_id = ? where id = ?", (message_id, raffle_id))
    conn.commit()


def update_active_ruffle(r_id, active=0):
    cur.execute(f"update raffles set active = ? where id = ?", (active, r_id))
    conn.commit()

# ruffle users
def get_users_ruffle(ruffle_id):
    res = cur.execute(f'SELECT * FROM raffle_users where id_raffle = ?', (ruffle_id, )).fetchall()
    return res


def is_user_ruffle(user_id, ruffle_id):
    res = cur.execute(f'SELECT * FROM raffle_users where id_raffle = ? and user_id = ?', (ruffle_id, user_id)).fetchall()
    return res


def new_user_ruffle(user_id, name, username, ruffle_id):
    cur.execute(f'INSERT INTO raffle_users(id_raffle, user_id, name, username) VALUES (?, ?, ?, ?)',
        (ruffle_id, user_id, name, username))
    conn.commit()

# admin
def new_admin(user_id):
    cur.execute(f"INSERT INTO admins VALUES (?)", (user_id, ))
    conn.commit()


def is_admin(user_id):
    res = cur.execute(f'SELECT * FROM admins where user_id = ?', (user_id, )).fetchall()
    return res


def get_admins():
    res = cur.execute(f'SELECT * FROM admins').fetchall()
    return res


def del_admin(user_id):
    cur.execute(f'delete from admins where user_id = ?', (user_id,))
    conn.commit()

