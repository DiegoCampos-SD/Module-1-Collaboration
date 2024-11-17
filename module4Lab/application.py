from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    book_name=db.Column(db.String(80), unique=True, nullable=False)
    author=db.Column(db.String(120))
    publisher=db.Column(db.String(50))
    
    def __repr__(self):
        return f"{self.id} - {self.book_name} - {self.author} - {self.publisher}"
    

@app.route('/')
def index():
    return 'Hello World!'

#Read all
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'Id: ' : book.id, 'Name: ' : book.book_name, 'Author: ':book.author, 'Publisher: ':book.publisher}
        output.append(book_data)
    return {"books": output}


#Read 1
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'Name: ' : book.book_name, 'Author: ':book.author, 'Publisher: ':book.publisher}

#Create
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id:': book.id}

#Delete
@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "{book.id} deleted."}

#Update
@app.route('/books/<id>', methods=['PUT'])
def update_book():
    book = Book.query.get(id)
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    
    db.session.commit()