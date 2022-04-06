import psycopg2
import os


def open_connection():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    con = psycopg2.connect(DATABASE_URL)
    cur = con.cursor()
    return con, cur


def close_connection(con, cur):
    cur.close()
    con.close()


def insert_into_db(table_name, title, date, img_url, img_copyright):
    db = open_connection()
    cur = db[1]
    con = db[0]
    sql = 'INSERT INTO ' + table_name + ' (title,date,img_url,img_copyright) VALUES (%s,%s,%s,%s);'
    cur.execute(sql, (title, date, img_url,img_copyright))
    con.commit()
    close_connection(con, cur)


def get_row(table_name):
    db = open_connection()
    cur = db[1]
    con = db[0]
    sql = 'SELECT * FROM ' + table_name + ' WHERE id = (SELECT MAX (id) FROM ' + table_name + ');'
    cur.execute(sql)
    row = cur.fetchone()

    close_connection(con, cur)
    return row
