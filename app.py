import sqlite3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from book import *
from salary import *
from employee import *

#app = Flask(__name__)
#db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Employees API
@app.route('/employees')
def get_employees():
    employees = Employee.query.all()

    output = []
    for employee in employees:
        employee_data = {'id': employee.id, 'first_name': employee.first_name, 'middle_name': employee.middle_name, 'last_name': employee.last_name}

        output.append(employee_data)

    return {"employees": output}

@app.route('/employees/<id>')
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return {"first_name": employee.first_name, "middle_name": employee.middle_name, "last_name": employee.last_name}

@app.route('/employees', methods=['POST'])
def add_employee():
    employee = Employee(first_name=request.json['first_name'],
        middle_name=request.json['middle_name'],
        last_name=request.json['last_name'])
    db.session.add(employee)
    db.session.commit()
    return {"first_name": employee.first_name, "middle_name": employee.middle_name, "last_name": employee.last_name}

@app.route('/employees/<id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee is None:
        return {"error": "not found"}
    db.session.delete(employee)
    db.session.commit()
    return {"message": "employee delete"}

@app.route('/')
def get_welcome():
    return {"message": "welcome!"}



# Employee Salary API
@app.route('/employees/<id>/salary', methods=['POST'])
def add_employee_salary(id):
    employee = Employee.query.get(id)
    if employee is None:
        return {"error": "not found"}
    salary = Salary(employee_id = request.json['employee_id'],
        employee_salary = request.json['employee_salary'])
    db.session.add(salary)
    db.session.commit()
    return {"employee_id": employee.id, "first_name": employee.first_name, "middle_name": employee.middle_name, "last_name": employee.last_name, "employee_salary": salary.employee_salary}

@app.route('/employees/<id>/salary', methods=['GET'])
def get_employee_salary(id):
    salary = Salary.query.get_or_404(id)
    employee = Employee.query.get(id)
    if employee is None:
        return {"error": "not found"}

    return {"employee_id": employee.id, "first_name": employee.first_name, "middle_name": employee.middle_name, "last_name": employee.last_name, "employee_salary": salary.employee_salary}


# Book API
@app.route('/create_book_table_db')
def create_book_table():
    # Connect to database
    conn = sqlite3.connect('data.db')
    # Create a cursor
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS book
    (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        description TEXT NOT NULL,
        location TEXT NOT NULL,
        status TEXT NOT NULL
    );""")

    return {"message": "book table created"}

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'id': book.id, 'title': book.title, 'author': book.author, 'description': book.description, 'location': book.location, 'status': book.status}

        output.append(book_data)
    return {"books": output}


@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'id': book.id, 'title': book.title, 'author': book.author, 'description': book.description, 'location': book.location, 'status': book.status}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(title=request.json['title'],
        author=request.json['author'],
        description=request.json['description'],
        location=request.json['location'],
        status=request.json['status'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id, 'title': book.title, 'author': book.author, 'description': book.description, 'location': book.location, 'status': book.status}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "book not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "book deleted"}