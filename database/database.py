import sqlite3
import pprint
from book import book
from publisher import publisher


def execute_query(db_name, query, entry=None):
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


def select_data(db_name, query, entry=None):
    if entry is None:
        entry = []
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
                                                        selling_price numeric,
                                                        FOREIGN KEY (book_title)
                                                        REFERENCES publishers (book_title)
                                                        ON UPDATE CASCADE
                                                        ON DELETE CASCADE
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
def insert_book(book):
    insert_query = """INSERT INTO books (book_title, author, publish_date, publisher, selling_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    query_values = [book.book_title, book.author, book.publish_date, book.publisher, book.selling_price]
    execute_query(db_books, insert_query, query_values)


def insert_publisher(publisher):
    insert_query = """INSERT INTO publishers (publisher_name, book_title, author, printed_quantity, printing_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    query_values = [publisher.publisher_name, publisher.book_title, publisher.author, publisher.printed_quantity, publisher.printing_price]
    execute_query(db_books, insert_query, query_values)


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
def update_book(new_value, book_object, field, book_id):
    update_query = """UPDATE books SET ? = ? WHERE id = ?"""
    update_data = (field, new_value, )


def update_book_title(new_value, book_id):
    update_query = """UPDATE books SET book_title = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_publisher(new_value, book_id):
    update_query = """UPDATE books SET publisher = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_author(new_value, book_id):
    update_query = """UPDATE books SET author = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_publish_date(new_value, book_id):
    update_query = """UPDATE books SET publish_date = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_selling_price(new_value, book_id):
    update_query = """UPDATE books SET selling_price = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


# Update Publisher methods
def update_publisher_name(new_value, publisher_id):
    update_query = """UPDATE publishers SET publisher_name = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_book_title(new_value, publisher_id):
    update_query = """UPDATE publishers SET book_title = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_author(new_value, publisher_id):
    update_query = """UPDATE publishers SET author = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_printed_quantity(new_value, publisher_id):
    update_query = """UPDATE publishers SET printed_quantity = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_printing_price(new_value, publisher_id):
    update_query = """UPDATE publishers SET printing_price = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
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


def potential_profit():
    query = """SELECT SUM((selling_price - printing_price) * printed_quantity) 
                                        FROM books 
                                        JOIN publishers 
                                        ON books.book_title=publishers.book_title"""
    select_data(db_books, query)


# Demo :)))
# print("Creating tables...")
create_table(db_books, books_table_query)
create_table(db_books, publishers_table_query)
# print("Inserting Books data...")
# insert_book("When Gravity Fails", "George Alec Effinger", 1987, "Audible", 10)
# insert_book("A Fire in The Sun", "George Alec Effinger", 1989, "Audible", 10)
# insert_book("The Exile Kiss", "George Alec Effinger", 1991, "Audible", 10)
# print("Done!")
# print("Books table data:")
# print("--------------------------------------------------------------------------")
# get_from_books("george")
# print("--------------------------------------------------------------------------")
# print(" ")
# print("Inserting Publishers data...")
# insert_publisher("Arbor House", "When Gravity Fails", "George Alec Effinger", 1000, 5)
# insert_publisher("Doubleday", "A Fire in The Sun", "George Alec Effinger", 1000, 5)
# insert_publisher("Doubleday", "The Exile Kiss", "George Alec Effinger", 1000, 5)
# print("Done!")
# print("Publishers table:")
# print("--------------------------------------------------------------------------")
# get_from_publishers('george')
# print("--------------------------------------------------------------------------")
# print(" ")
# print("Updating Book Data..")
# update_book_publisher("Arbor House", 1)
# update_book_publisher("Doubleday", 2)
# update_book_publisher("Doubleday", 3)
# print("Done!")
# print("Updated Books table data:")
# print("--------------------------------------------------------------------------")
# get_from_books("george")
# print("--------------------------------------------------------------------------")
# print(" ")
# print("Updating Publishers Data..")
# update_publisher_book_title("When Gravity Fails", 1)
# update_publisher_book_title("A Fire in The Sun", 2)
# update_publisher_book_title("The Exile Kiss", 3)
# print("Done!")
# print("Updated Publishers Data:")
# print("--------------------------------------------------------------------------")
# get_from_publishers('george')
# print("--------------------------------------------------------------------------")
# print(" ")
# print("Deleting Books data...")
# delete_book_by_id(1)
# delete_book_by_id(2)
# delete_book_by_id(3)
# print("Done!")
# print("Deleted Books table data:")
# print("--------------------------------------------------------------------------")
# get_from_books("george")
# print("--------------------------------------------------------------------------")
# print(" ")
# print("Deleting Publishers data...")
# delete_publisher_by_id(1)
# delete_publisher_by_id(2)
# delete_publisher_by_id(3)
# print("Done!")
# print("Deleted Publishers Data:")
# print("--------------------------------------------------------------------------")
# get_from_publishers('george')
# print("--------------------------------------------------------------------------")
# print(" ")
# print("All done!")


# book = book.book("Conffesions of a Sociopath","M. E. Thomas", 2015, "Factory", 20.15)
publisher = publisher.publisher("Factory", "M. E. Thomas", "Conffesions of a Sociopath", 5000, 5.12)
# insert_book(book)
# insert_publisher(publisher)

# query_sample = """SELECT books.book_title, printed_quantity, printing_price, selling_price
#                                         FROM books
#                                         JOIN publishers
#                                         ON books.book_title=publishers.book_title"""

# queryBooks = "SELECT * FROM books"
queryPublisher = "SELECT * FROM publishers"
# select_data(db_books, queryBooks)
select_data(db_books, queryPublisher)
# potential_profit()
