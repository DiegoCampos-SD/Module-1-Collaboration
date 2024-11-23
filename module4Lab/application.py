from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    title=db.Column(db.String(80), unique=True, nullable=False)
    author=db.Column(db.String(120))
    publisher=db.Column(db.String(50))
    
    def __repr__(self):
        return f"{self.id} - {self.title} - {self.author} - {self.publisher}"
    

@app.route('/')
def index():
    return 'Hello World!'

#Read all
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'Id: ' : book.id, 'Title: ' : book.title, 'Author: ':book.author, 'Publisher: ':book.publisher}
        output.append(book_data)
    return {"books": output}


#Read 1
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'Title: ' : book.title, 'Author: ':book.author, 'Publisher: ':book.publisher}

#Create
@app.route('/books', methods=['POST'])
def create_book():
    new_book = Book(title=request.json['title'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added'}), 201


#Delete
@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "{book.id} deleted."}

#Update
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)
    
    db.session.commit()
    
if __name__ == "__main__":
    db.create_all()  # Create the database tables
    app.run(debug=True)