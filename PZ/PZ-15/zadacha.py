import sqlite3

conn = sqlite3.connect("meds.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS medicals (
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    count INTEGER NOT NULL,
    price REAL NOT NULL
)
''')
data = [
    ("Med", 5, 6500),
    ("Med2", 15, 500),
    ("Med3", 1, 9500),
]
cursor.executemany("INSERT INTO medicals (name, count, price) VALUES (?, ?, ?)", data)
conn.commit()
def add_med(name, count, price):
    cursor.execute("INSERT INTO medicals (name, count, price) VALUES (?, ?, ?)", (name, count, price))
    conn.commit()

name, count, price = input("Name: "), int(input("Count: ")), float(input("Price: "))
add_med(name, count, price)

print(cursor.execute("SELECT*FROM medicals").fetchall())