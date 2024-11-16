"""
16.3 Create a CSV file called books2.csv by using these lines:

title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
"""
books2_data = """title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
"""

with open('chapter16/books2.csv', 'w') as f:
    f.write(books2_data)


"""
16.4 Use the sqlite3 module to create a SQLite database called books.db
and a table called books with these fields: title (text), author (text),
and year (integer).
"""

import sqlite3

connection = sqlite3.connect('chapter16/books.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

connection.commit()
connection.close()



"""
16.5 Read books2.csv and insert its data into the book table.
"""

import csv
import sqlite3

connection = sqlite3.connect('chapter16/books.db')
cursor = connection.cursor()


with open('chapter16/books2.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
            INSERT INTO books (title, author, year)
            VALUES (?, ?, ?)
        ''', (row['title'], row['author'], row['year']))


connection.commit()
connection.close()

"""
16.6 Select and print the title column from the book table in alphabetical order.
"""

import sqlite3


connection = sqlite3.connect('chapter16/books.db')
cursor = connection.cursor()


cursor.execute('SELECT title FROM books ORDER BY title')
titles = cursor.fetchall()

for title in titles:
    print(title[0])

connection.close()


"""
16.7 Select and print all columns from the book table in order of publication.
"""
import sqlite3


connection = sqlite3.connect('chapter16/books.db')
cursor = connection.cursor()


cursor.execute('SELECT * FROM books ORDER BY year')
books = cursor.fetchall()

for book in books:
    print(book)
    

"""6.8 Use the sqlalchemy module to connect to the sqlite3 database books.db
that you just made in exercise 16.4. As in 16.6, select and print the title column
from the book table in alphabetical order.
"""

from sqlalchemy import create_engine, MetaData, Table


engine = create_engine('sqlite:///chapter16/books.db')
metadata = MetaData()

books_table = Table('books', metadata, autoload_with=engine)


with engine.connect() as connection:
    result = connection.execute(books_table.select().order_by(books_table.c.title))
    
    for row in result:
        print(row['title'])