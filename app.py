from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    middle_name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.first_name} - {self.middle_name} - {self.last_name}"

@app.route('/')
def index():
    return 'Hello'

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
