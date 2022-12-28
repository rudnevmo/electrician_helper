import sqlite3
from params import tabl

base = sqlite3.connect('cable.db')
cur = base.cursor()

'''
base.execute('CREATE TABLE IF NOT EXISTS {}(core_material, padding_method, voltage, current, power, section)'.
             format('data'))
base.commit()

cur.executemany('INSERT INTO data VALUES(?, ?, ?, ?, ?, ?)', tabl)
base.commit()

r = cur.execute('SELECT section FROM data').fetchall()
print(r)
sec = cur.execute('SELECT section FROM data WHERE current == ?', (230.0,)).fetchone()
print(sec)
'''
curr = float(input('Ток = '))
res = cur.execute("SELECT section FROM data WHERE core_material == 'copper' AND padding_method == 'outside' "
                  "AND voltage == 400 AND current == ?", (curr, )).fetchone()
print(res)
