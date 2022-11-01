#!/bin/python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

class Salary(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_salary = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"{self.first_name} - {self.middle_name} - {self.last_name}"