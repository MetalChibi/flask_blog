import sqlite3                              # Importing sqlite3 module.
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort       # Import abort() from Werkzeug lib

def get_db_connection():                    # Function that connects us to DB and returns it.
    conn = sqlite3.connect('database.db')   # 1. Open connection to database.db via the `conn` object
    conn.row_factory = sqlite3.Row          # 2. Set row_factory to sqlite3.Row to access DB columns based on names
    return conn                             # 3. Return connection object which is used for DB connection

def get_post(post_id):                      # Argument post_id: determintes which blog post is to be returned.
    conn = get_db_connection()              # Connect to DB, then run SQL to get post ID.
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
        (post_id,)).fetchone()              # fetchone() gets one result & saves it to `post` var.
                                            # WTF is (post_id,)? Why the comma?
    conn.close()                            # Close connection.
    if post is None:                        # If no post is found: 404.
        abort(404)
    return post                             # Else: return the post as is.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alohomora'

@app.route('/')
def index():
    conn = get_db_connection()              # Connect to DB via conn, using get_db_connection function.
    posts = conn.execute('SELECT * FROM posts').fetchall()  # Fetch data from DB by executing a query & write it into `posts` variable;
                                            # fetchall() fetches all lines of query execution result.
    conn.close()                            # Close DB connection via close() method.
    return render_template('index.html', posts=posts) # posts is an arg that contains results from DB (from `posts` variable)


@app.route('/<int:post_id>')                # Add rule of variable: an integer to route which contains a post ID.
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post) # `post` is an arg that contains results from DB (from `post` variable)

@app.route('/create', methods=('GET', 'POST'))
# GET: Accepted by default.
# For non-default methods: pass a tuple with GET & POST to `methods` of the @app.route() decorator.
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
    # This code will only execute if the request is POST.
    # Get data from request.form object that can access form data in request.

    if not title:
        flash('Title is required')
    # If title isn't entered, show error. Else: do the magic!
    else:
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        # Insert post title/content into DB.
        conn.commit()
        conn.close()
        return redirect(url_for('index')) # Return to index.
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
# example: .../420/edit - editing post with ID 420
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # Get form data.

        if not title:
            flash('Title is required')
        # Show error if title is missing.
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                ' WHERE id = ?',
                (title, content, id)) 
            # Update `posts` table for a record with matching ID
            conn.commit()
            conn.close()
            return redirect(url_for('index')) # Return to index.

    return render_template('edit.html', post=post)