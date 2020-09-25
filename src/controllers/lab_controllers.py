import numpy as np
from flask import request
from src.database import db 
from src.app import app

@app.route('/lab/create/<name>')
def create_lab(name):
    """Crea el nombre de un lab"""
    new_lab = {
    'Title': name}
    result = db.pull.insert_one(new_lab)
    return {'_id': str(result.inserted_id)}
"""
@app.route('/lab/<lab_name>/meme')
def random_meme(lab_name):
   
    result=db.pull_request.aggregate([
        { "$match":  {"Title": lab} },
        { "$sample": {"size": 1} },
        { "$project": { "Meme" : 1, "_id": 0}}
      ])
    return dumps(result)
"""