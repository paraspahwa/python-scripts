# Interact with a SQLite database using sqlite3

import sqlite3

# Connect to the database (or create a new one)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))

# Commit the changes and close the connection
conn.commit()
conn.close()
