import numpy as np
from flask import request
from src.database import db 
from src.app import app

@app.route('/lab/create/<name>')
def create_lab(name):
    """Crea el nombre de un lab"""
    new_lab = {
    'Lab': name}
    result = db.pull.insert_one(new_lab)
    return {'_id': str(result.inserted_id)}

@app.route('/lab/<lab>/meme')
def random_meme(lab):
    """Coge un meme random"""
    result=db.pull_request.aggregate([
        { "$match":  {"Lab": lab} },
        { "$sample": {"size": 1} },
        { "$project": { "Url" : 1, "_id": 0}}
      ])
    return dumps(result)