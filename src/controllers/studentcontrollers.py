#funcion controladora
import numpy as np
from flask import request
from src.database import db
from src.app import app
from bson.json_util import dumps

@app.route('/') 
def welcome():
    return {
        "status": "OK",
        "message": "Welcome to My Api"
        }

@app.route('/student/create/<name>')
def create_student(name):
    """ Crea el nombre del estudiante"""
    new_student = {
        'Usuario': name}
    result = db.pull.insert_one(new_student)
    return {'_id': str(result.inserted_id)}

@app.route('/student/all')
def allstudents():
    """Da el listado de todos los usuarios"""
    result = db.pull.distinct("Usuario")
    return dumps(result)
