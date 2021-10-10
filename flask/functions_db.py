import sqlite3, json
from flask import g
from datetime import datetime, date


DATABASE = 'database.db'

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def create_usernamedata(conn, usernamedob):

    sql = ''' INSERT INTO usernamedob(name,dob)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, usernamedob)


def post_usernamedob_db(username, jsondata):
    jsondumps = json.dumps(jsondata)
    jsoned = json.loads(jsondumps)
    dob = str(jsoned['dateOfBirth'])
    dob_date = datetime.strptime(dob, '%Y-%m-%d')

    conn = create_connection(DATABASE)
    with conn:
        create_table_func(conn)
        cur = conn.cursor()
        cur.execute("SELECT name,dob FROM usernamedob WHERE name= ?", (username,))
        record=cur.fetchall()
        if len(record)==0:
            dobvals = (username, dob_date);
            dob_id = create_usernamedata(conn, dobvals)
        else: 
            cur.execute("UPDATE usernamedob SET dob = ? WHERE name= ?", (dob_date, username,))


def create_table_func(conn):
    create_dobtable = """ CREATE TABLE IF NOT EXISTS usernamedob(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        dob text
                                    ); """
    create_table(conn, create_dobtable)


def get_username_db(username):
    query= f"SELECT name,dob FROM usernamedob WHERE name='{username}'"

    conn = create_connection(DATABASE)
    cur = conn.cursor()
    cur.execute(query)
    record = cur.fetchall()

    return record[0][1]