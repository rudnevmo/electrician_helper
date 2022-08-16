import sqlite3
from params import tabl

base = sqlite3.connect('cable.db')
cur = base.cursor()


base.execute('CREATE TABLE IF NOT EXISTS {}(core_material, padding_method, voltage, current, power, section)'.
             format('data'))
base.commit()

cur.executemany('INSERT INTO data VALUES(?, ?, ?, ?, ?, ?)', tabl)
base.commit()
