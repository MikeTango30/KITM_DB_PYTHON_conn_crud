import sqlite3
import pprint


def execute_query(db_name, query, entry):
    connection = sqlite3.connect(db_name)
    connection_cursor = connection.cursor()
    connection_cursor.execute(query, entry)
    connection.commit()
    connection.close()


def create_table(db_name, query):
    connection = sqlite3.connect(db_name)
    connection_cursor = connection.cursor()
    connection_cursor.execute(query)
    connection.commit()
    connection.close()


def select_data(db_name, query, entry):
    connection = sqlite3.connect(db_name)
    connection_cursor = connection.cursor()
    connection_cursor.execute(query, entry)
    connection.commit()
    rows = []
    for row in connection_cursor.execute(query, entry):
        rows.append(row)
    pp = pprint.PrettyPrinter()
    pp.pprint(rows)
    connection.close()


db_books = "books.db"
books_table_query = """CREATE TABLE IF NOT EXISTS books (
                                                        id integer PRIMARY KEY,
                                                        book_title text,
                                                        author text,
                                                        publish_date date,
                                                        publisher text,
                                                        selling_price numeric
                                                        )"""
publishers_table_query = """CREATE TABLE IF NOT EXISTS publishers (
                                                        id integer PRIMARY KEY,
                                                        publisher_name text,
                                                        book_title text,
                                                        author text,
                                                        printed_quantity integer,
                                                        printing_price numeric
                                                        )"""


# Insert
def insert_book(book_title, author, publish_date, publisher, selling_price):
    insert_query = """INSERT INTO books (book_title, author, publish_date, publisher, selling_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    book = [book_title, author, publish_date, publisher, selling_price]
    execute_query(db_books, insert_query, book)


def insert_publisher(publisher_name, book_title, author, printed_quantity, printing_price):
    insert_query = """INSERT INTO publishers (publisher_name, book_title, author, printed_quantity, printing_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    publisher = [publisher_name, book_title, author, printed_quantity, printing_price]
    execute_query(db_books, insert_query, publisher)


# Search
def get_from_books(search_string):
    select_query = """SELECT * FROM books WHERE book_title OR 
                                                author OR 
                                                publish_date OR 
                                                publisher OR 
                                                selling_price LIKE ?"""
    title = ['%' + search_string + '%']
    select_data(db_books, select_query, title)


def get_from_publishers(search_string):
    select_query = """SELECT * FROM publishers WHERE publisher_name OR 
                                                     book_title OR 
                                                     author OR 
                                                     printed_quantity OR 
                                                     printing_price LIKE ?"""
    title = ['%' + search_string + '%']
    select_data(db_books, select_query, title)


# Update Book methods
def update_book_title(new_value, old_value):
    update_query = """UPDATE books SET book_title = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_book_publisher(new_value, old_value):
    update_query = """UPDATE books SET publisher = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_book_author(new_value, old_value):
    update_query = """UPDATE books SET author = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_book_publish_date(new_value, old_value):
    update_query = """UPDATE books SET publish_date = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_book_selling_price(new_value, old_value):
    update_query = """UPDATE books SET selling_price = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


# Update Publisher methods
def update_publisher_name(new_value, old_value):
    update_query = """UPDATE publishers SET publisher_name = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_publisher_book_title(new_value, old_value):
    update_query = """UPDATE publishers SET book_title = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_publisher_author(new_value, old_value):
    update_query = """UPDATE publishers SET author = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_publisher_printed_quantity(new_value, old_value):
    update_query = """UPDATE publishers SET printed_quantity = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


def update_publisher_printing_price(new_value, old_value):
    update_query = """UPDATE publishers SET printing_price = ? WHERE id = ?"""
    update_data = [new_value, old_value]
    execute_query(db_books, update_query, update_data)


# Delete
def delete_book_by_id(book_id):
    delete_query = """DELETE FROM books WHERE id = ?"""
    entry_id = [book_id]
    execute_query(db_books, delete_query, entry_id)


def delete_publisher_by_id(publisher_id):
    delete_query = """DELETE FROM publishers WHERE id = ?"""
    entry_id = [publisher_id]
    execute_query(db_books, delete_query, entry_id)


# Demo :)))
print("Creating tables...")
create_table(db_books, books_table_query)
create_table(db_books, publishers_table_query)
print("Inserting Books data...")
insert_book("When Gravity Fails", "George Alec Effinger", 1987, "Audible", 21.99)
insert_book("A Fire in The Sun", "George Alec Effinger", 1989, "Audible", 24.99)
insert_book("The Exile Kiss", "George Alec Effinger", 1991, "Audible", 32.99)
print("Done!")
print("Books table data:")
print("--------------------------------------------------------------------------")
get_from_books("george")
print("--------------------------------------------------------------------------")
print(" ")
print("Inserting Publishers data...")
insert_publisher("Arbor House", "When Grovity Fails", "George Alec Effinger", 3000, 5.45)
insert_publisher("Doubleday", "A Lure in The Sun", "George Alec Effinger", 5000, 6.45)
insert_publisher("Doubleday", "The Exalted Kiss", "George Alec Effinger", 6500, 4.45)
print("Done!")
print("Publishers table:")
print("--------------------------------------------------------------------------")
get_from_publishers('george')
print("--------------------------------------------------------------------------")
print(" ")
print("Updating Book Data..")
update_book_publisher("Arbor House", 1)
update_book_publisher("Doubleday", 2)
update_book_publisher("Doubleday", 3)
print("Done!")
print("Updated Books table data:")
print("--------------------------------------------------------------------------")
get_from_books("george")
print("--------------------------------------------------------------------------")
print(" ")
print("Updating Publishers Data..")
update_publisher_book_title("When Gravity Fails", 1)
update_publisher_book_title("A Fire in The Sun", 2)
update_publisher_book_title("The Exile Kiss", 3)
print("Done!")
print("Updated Publishers Data:")
print("--------------------------------------------------------------------------")
get_from_publishers('george')
print("--------------------------------------------------------------------------")
print(" ")
print("Deleting Books data...")
delete_book_by_id(1)
delete_book_by_id(2)
delete_book_by_id(3)
print("Done!")
print("Deleted Books table data:")
print("--------------------------------------------------------------------------")
get_from_books("george")
print("--------------------------------------------------------------------------")
print(" ")
print("Deleting Publishers data...")
delete_publisher_by_id(1)
delete_publisher_by_id(2)
delete_publisher_by_id(3)
print("Done!")
print("Deleted Publishers Data:")
print("--------------------------------------------------------------------------")
get_from_publishers('george')
print("--------------------------------------------------------------------------")
