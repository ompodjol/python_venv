import sqlite3

connection = sqlite3.connect('employee_data.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Employee
    (
        id INT PRIMARY KEY NOT NULL,
        first_name TEXT NOT NULL,
        middle_name TEXT NOT NULL,
        last_name TEXT NOT NULL
    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Employee
    (
        id INT PRIMARY KEY NOT NULL,
        email_address TEXT NOT NULL,
        FOREIGN KEY(Employee_id) REFERENCES Department(id)
    );""")

print("Table Names created successfully!")


sqlite_insert_query = """INSERT INTO Employee
    (
        id, first_name, middle_name, last_name
    )
    VALUES
    (
        1, 'Jud', 'Cabeza', 'Jacquez'
    )
"""

count = cursor.execute(sqlite_insert_query)
connection.commit()



cursor.close()