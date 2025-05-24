import sqlite3

# connect to the database (create it if it doesn't exist)
conn = sqlite3.connect('workshop_db.db')

# create a cursor object to execute SQL commands
cursor = conn.cursor()

# create the workshop entry list table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS workshop_entry_list (
        id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        car_type TEXT NOT NULL,
        chasis_no TEXT NOT NULL,
        reg_no TEXT NOT NULL,
        vehicle_model TEXT NOT NULL,
        complaint TEXT NOT NULL,
        problem TEXT NOT NULL,
        solution TEXT NOT NULL,
        conclusion TEXT NOT NULL,
        year INTEGER NOT NULL
    )
''')

# commit the changes and close the connection
conn.commit()
conn.close()


import sqlite3

# connect to the database
conn = sqlite3.connect('workshop_db.db')

# create a cursor object to execute SQL commands
cursor = conn.cursor()

# select all rows from the workshop_entry_list table
cursor.execute('SELECT * FROM workshop_entry_list')

# print the results
for row in cursor.fetchall():
    print(row)

# close the connection
conn.close()

