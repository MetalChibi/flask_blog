import sqlite3                                  # Importing sqlite3 module.

connection = sqlite3.connect('database.db')     # Variable with connection to the database file `database.db` 
                                                # which will be created as soon as python file is run.
# executescript() method creates a cursor object by calling the cursor() method, 
# calls the cursor’s executescript() method with the given sql_script, 
# and returns the cursor
with open('schema.sql') as f:
    connection.executescript(f.read())


cur = connection.cursor()                       # Cursor object is created here but wtf is a cursor method
                                                # Anyways, this cursor's execute() method will be called with the SQL script???
                                                # After that, the cursor is returned?? what???? lmao

# Add data to DB:
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", 
    ('First Post', 'Content for the first post')
    )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
    ('Second Post', 'Content for the second post')
    )

connection.commit()                             # Changes are committed here.
connection.close()                              # And the connection is closed. Voila!