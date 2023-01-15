
/* This trivial "dump" file re-creates the database table
   needed for the assignment. You should not need to use
   this script at all - it should be possible to open the
   shopping_cart.db file from the DB Browser for SQLite's
   "Open Database" menu option.  (Do not drag-and-drop the
   database file into the DB Browser's GUI. On some systems
   this causes the DB Browser to ask for a password, even
   though the database is not password protected.) In the
   unlikely event that you need to create a fresh copy of
   the database using this script you can do so easily using
   the DB Browser's "Import database from SQL file" menu
   option. Ensure that you call the resulting database
   "shopping_cart.db". */

CREATE TABLE "ShoppingCart" (
	`Item`	TEXT,
	`Price`	REAL
);

