from typing import Optional
import psycopg2


con = psycopg2.connect(
    dbname='db_name',   # input your database name
    user='db_user',     # input your database user's name
    password='db_password',     # input your database password
    host='host',    # input host example: localhost
    port='port'     # input port example: 5432
)
cur = con.cursor()


def function_db():
    query = '''
    create table if not exists users(
    id serial,
    user_id varchar(255) unique,
    user_name varchar(255),
    type bool not null,
    time timestamp default now()
    );'''

    cur = con.cursor()
    cur.execute(query)
    con.commit()


def get_user(userid: str) -> Optional[tuple]:
    query = 'select * from users where user_id = %s'  # noqa
    cur.execute(query, (userid,))
    return cur.fetchone()


def add_user(user_id: str, username: str, type_us: bool) -> tuple[str, str, bool]:
    query = 'insert into users(user_id, user_name, type) values(%s, %s, %s)' # noqa
    cur.execute(query, (user_id, username, type_us))
    con.commit()
    return True, '\n\t[✅ Added]'


def members():
    query = 'select * from users where type = false'
    cur.execute(query, )
    string = ''
    for i in cur.fetchall():
        string += f"ID: {i[0]}\t\t\t\t\tUSER-ID: {i[1]}\t\t\t\t\tUSERNAME: @{i[2]}\n\n"
    return string


def members2():
    query = 'select * from users where type = true'
    cur.execute(query, )
    string = ''
    for i in cur.fetchall():
        if i[1] != '190767640':
            string += f"ID: {i[0]}\t\t\t\t\tUSER-ID: {i[1]}\t\t\t\t\tUSERNAME: @{i[2]}\n\n"
        else:
            continue
    return string


def add_admins(user_idd: str):
    query = 'UPDATE users SET type = true WHERE user_id = %s and type = false'
    cur.execute(query, (user_idd, ))
    con.commit()
    return get_user(user_idd)


def remove_admins(user_idd: str):
    query = 'UPDATE users SET type = false WHERE user_id = %s and type = true'
    cur.execute(query, (user_idd,))
    con.commit()
    return get_user(user_idd)


def checker_type(user_idd: str):
    query = 'select * from users where user_id = %s and type = true'
    cur.execute(query, (user_idd, ))
    return cur.fetchone()





