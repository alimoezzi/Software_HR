from Models.Models import db
from datetime import datetime


class Job(db.Model):
    __tablename__ = 'job'
    jid = db.Column(db.String(100), primary_key=True)
    result = db.Column(db.Text(), nullable=True)
    created = db.Column(db.DateTime())
    description = db.Column(db.Text(), nullable=False)

    def __init__(self,jid: str, result: str, description: str):
        self.jid = jid
        self.result = result
        self.description = description
        self.created = datetime.now()

    def __repr__(self):
        return "< {0} {1} {2}>".format(self.jid, self.description, self.created.strftime('%b %d, %Y'))
