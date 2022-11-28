from config import ADMIN_ID
def create_tables_for_sql(cur, conn):
    cur.execute('''CREATE TABLE if not exists raffles
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text text,
    button text,
    date text,
    value_wins integer,
    chat_id integer,
    message_id integer,
    active integer
    );''')


    cur.execute('''CREATE TABLE if not exists raffle_users
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_raffle integer,
    user_id text, 
    name text,
    username text
    );''')


    cur.execute('''CREATE TABLE  if not exists admins
    (
    user_id integer
    );''')

    res = cur.execute(f'SELECT * FROM admins where user_id = ?', (ADMIN_ID, )).fetchall()
    if not res:
        cur.execute(f"INSERT INTO admins VALUES (?)", (ADMIN_ID, ))
        conn.commit()   
