import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('school.db')

        return con

    except Error:
        print(Error)


def sql_table(con):

    cursObj = con.cursor()

    cursObj.execute("CREATE TABLE stu(id integer PRIMARY KEY, name text, regNumber real, accommodationType text, course text)")

    con.commit()

con = sql_connection()

sql_table(con)


