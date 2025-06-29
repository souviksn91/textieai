# project/models.py
from project import db
from datetime import datetime, timezone

class Correction(db.Model):
    __tablename__ = 'corrections'
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.Text, nullable=False)
    corrected_text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Correction {self.id}>"