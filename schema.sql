DROP TABLE IF EXISTS posts; /* deletes all existing tables named `posts`, if any*/

CREATE TABLE posts (		/* creates `posts` table */
    id INTEGER PRIMARY KEY AUTOINCREMENT,	/* Filled automatically; primary key with unique value for every record */
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,	/* Filled automatically; NOT NULL = can't be empty; DEFAULT = time of post addition to base*/
    title TEXT NOT NULL,
    content TEXT NOT NULL
);