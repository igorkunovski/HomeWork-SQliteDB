import sqlite3 as sql

with sql.connect('main.db') as con:
    cur = con.cursor()


def show_all():
    cur.execute('''SELECT * FROM inventory''')
    for result in cur:
        print(result)
    return
