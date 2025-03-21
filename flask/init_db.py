import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts(title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts(title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )   
cur.execute("INSERT INTO posts(title, content) VALUES (?, ?)",

            ('Third Post', 'Content for the third post')
            )
cur.execute("INSERT INTO posts(title, content) VALUES (?, ?)",
            ('Fourth Post', 'Content for the fourth post')
            )
connection.commit()
connection.close()