from init import app,db
import datetime
import json
from datetime import timedelta
from collections import OrderedDict
 
def jsonDefault(OrderedDict):
    return OrderedDict.__dict__
class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.String(80), unique=False, nullable=False, default="AD01")
    accuracy = db.Column(db.String(80), unique=False, nullable=False)
    date = db.Column(db.String(80), nullable=False, default=((datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')))
    path = db.Column(db.String(80), unique=False, nullable=False)
    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'camera_id': self.camera_id,
           'accuracy': self.accuracy,
           'date': self.date,
           'path': self.path
       }

    def __repr__(self):
        return json.dumps('{ "camera_id": %r, "acurracy": %r, "date": %r, "path": %r }' % (self.camera_id, self.accuracy,self.date,self.path),default=jsonDefault, indent=4)

class contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.nombre