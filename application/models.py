from application import db, app
from datetime import datetime

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    content = db.Column(db.String(511), nullable = False)
    category = db.Column(db.String(255), nullable = False)
    urgency = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.now)
    is_done = db.Column(db.Boolean, default = False, nullable = False)