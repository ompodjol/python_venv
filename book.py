#!/bin/python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import app

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=False)
    location = db.Column(db.String(100), unique=False, nullable=False)
    status = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.title} - {self.author} - {self.description} - {self.location} - {self.status}"