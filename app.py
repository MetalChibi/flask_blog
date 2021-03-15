import sqlite3                              # Importing sqlite3 module.
from flask import Flask, render_template    # Importing Flask

def get_db_connection():                    # Function that connects us to DB and returns it.
    conn = sqlite3.connect('database.db')   # 1. Open connection to database.db via the `conn` object
    conn.row_factory = sqlite3.Row          # 2. Set row_factory to access DB columns based on names
    return conn                             # 3. Return connection object which is used for DB connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()              # Connect to DB via conn, using get_db_connection function.
    posts = conn.execute('SELECT * FROM posts').fetchall()  # Fetch data from DB by executing a query & write it into `posts` variable;
                                            # fetchall() fetches all lines of query execution result.
    conn.close()                            # Close DB connection via close() method.
    return render_template('index.html', posts=posts) # posts is an arg that contains results from DB (from `posts` variable)