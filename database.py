import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

def creating_table():
    # creating the table for book data
    cur.execute("CREATE TABLE book_data(book_title,book_isbn,book_author)")

    # creating table for user data
    cur.execute("CREATE TABLE user_data(user_email,user_password)")

    # creating table for admin acc
    # cur.execute("CREATE TABLE admin_acc(admin_email,admin_password)")

    # creating table for reserved book data
    cur.execute("CREATE TABLE reserved_book_data(user_name,user_roll_no,book_title,book_isbn,book_author)")

    # commiting changes
    conn.commit()

# creating_table()

books_titles = ["To Kill a Mockingbird","1984","The Great Gatsby","Pride and Prejudice","The Catcher in the Rye","The Lord of the Rings","The Alchemist","The Hobbit","Brave New World","The Book Thief","The Road"]

books_isbns = ["978-0061120084","978-0451524935","978-0743273565","978-1503290563","978-0316769488","978-0618640157","978-0062315007","978-0547928227","978-0060850524","978-0375842207","978-0307387899"]

books_authors = ["Harper Lee","George Orwell","F. Scott Fitzgerald","Jane Austen","J.D. Salinger","J.R.R. Tolkien","Paulo Coelho","J.R.R. Tolkien","Aldous Huxley","Markus Zusak","Cormac McCarthy"]

# for i in range(len(books_titles)):
#     cur.execute("INSERT INTO book_data VALUES(?,?,?)",(books_titles[i],books_isbns[i],books_authors[i]))
# conn.commit()

# inserting the user data into the database
# cur.execute("INSERT INTO admin_acc VALUES('agent07','limegreen')")
# conn.commit()

# inserting the user data into the database
# cur.execute("INSERT INTO user_data VALUES(?,?)",("",""))
# conn.commit()


# inserting the reserved book data into the database
# cur.execute("INSERT INTO reserved_book_data VALUES('muhammad','jalal','html css','123-234324238','jhon duckett')")
# cur.execute("INSERT INTO reserved_book_data VALUES('muhammad','jalal','html css','123-234324238','jhon duckett')")
# cur.execute("INSERT INTO reserved_book_data VALUES('muhammad','jalal','html css','123-234324238','jhon duckett')")
# cur.execute("INSERT INTO reserved_book_data VALUES('uzair','35','pyhton','123-234324238','jhon duckett')")
# conn.commit()


# deleting the table
# cur.execute("DROP TABLE book_data")
# cur.execute("DROP TABLE user_data")
# cur.execute("DROP TABLE reserved_book_data")
# cur.execute("DROP TABLE admin_acc")
# conn.commit()

# for printing the data in table for checking
# def printing_data_in_table():
#     cur.execute("SELECT *,rowid from book_data")
#     print(cur.fetchall())

# for counting the rows in table
# cur.execute("SELECT count(*) from book_data")
# print(cur.fetchone()[0])

# for getting a specific data
# cur.execute("SELECT book_title from book_data")
# print(cur.fetchall())

# book_title = []
# book_isbn = []
# book_author = []

# cur.execute("SELECT * FROM book_data")
# data = cur.fetchall()
# for item in data:
#     book_title.append(item[0])
#     book_isbn.append(item[1])

# for deleting row from the database
# cur.execute("DELETE from reserved_book_data WHERE book_isbn LIKE '11'")

# showing all the data from user data table


# searching specific data in database
# search = "muh"
# cur.execute(f"SELECT * FROM reserved_book_data WHERE user_name LIKE '{search}%'")
# result = cur.fetchall()
# print(result)


# printing_data_in_table()

# conn.commit()

# cur.execute(f"UPDATE user_data SET user_password = '11' WHERE user_email = '1'")
# conn.commit()

# cur.execute("SELECT * from user_data")
# result = cur.fetchall()
# print(result)

books = [
    ["To Kill a Mockingbird", "9780061120084", "Harper Lee"],
    ["1984", "9780451524935", "George Orwell"],
    ["The Great Gatsby", "9780743273565", "F. Scott Fitzgerald"],
    ["The Catcher in the Rye", "9780316769488", "J.D. Salinger"],
    ["Pride and Prejudice", "9780141040349", "Jane Austen"],
    ["The Hobbit", "9780547928227", "J.R.R. Tolkien"],
    ["Harry Potter and the Sorcerer’s Stone", "9780590353427", "J.K. Rowling"],
    ["The Alchemist", "9780062315007", "Paulo Coelho"],
    ["Brave New World", "9780060850524", "Aldous Huxley"],
    ["Moby-Dick", "9781503280786", "Herman Melville"]
]

cur.executemany("INSERT INTO book_data VALUES (?,?,?)",books)
conn.commit()
# cur.execute("SELECT * FROM book_data")
# res = cur.fetchall()
# print(res)