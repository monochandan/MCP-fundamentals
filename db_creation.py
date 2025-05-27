'''
Create a simple databse
'''
import sqlite3
import os # https://docs.python.org/3/library/os.html#module-os

# sqilte docs : https://www.sqlite.org/docs.html
# sqlite interface : https://docs.python.org/3/library/sqlite3.html#cursor-objects

# path = 'RAG_MCP/my_db'
# 1. create db
os.makedirs('my_db', exist_ok=True)

# 2 connect db
conn = sqlite3.connect('my_db/employees.db')

# 3 in order to execute sql
cursor = conn.cursor()

# 4 create table
# https://www.sqlite.org/datatype3.html
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            salary REAL,
            hired_date TEXT
        )
    ''')

# 5 insert the data into the table
data = [
    (1, 'Mono', 'Chandan', 'xyz@gmail.com', 45000.00, '2023-10-01'),
    (2, 'Ab', 'cd', 'ab@gmail.com', 49000.00, '2023-11-01'),
    (3, 'Lala', 'land', 'lal@gmail.com', 65000.00, '2023-10-05'),
    (4, 'Chrom', 'ext', 'ct@gmail.com', 48000.00, '2023-10-01'),
    (5, 'Brave', 'br', 'br@gmail.com', 46000.00, '2024-10-01'),
    (6, 'first', 'secnd', 'fs@gmail.com', 35000.00, '2023-10-01'),
    (7, 'see', 'blue', 'sb@gmail.com', 25000.00, '2022-10-01'),
    (8, 'clever', 'dumb', 'cz@gmail.com', 15000.00, '2023-20-01'),
    (9, 'sky', 'earth', 'se@gmail.com', 65000.00, '2013-10-01'),
    (10, 'water', 'vap', 'wv@gmail.com', 85000.00, '2033-10-01'),

]
cursor.executemany("INSERT OR REPLACE INTO employees (id, first_name, last_name, email, salary, hired_date) VALUES(?,?,?,?,?,?)", data)

#6 commit change , close the connection
conn.commit()
conn.close()

print("Database name employee created successfully")


