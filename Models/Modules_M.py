from sqlalchemy import Table, Text, UniqueConstraint
from Models.Models import db


class Modules_Modules(db.Model):
    __tablename__ = 'modules_modules'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    modules1_id = db.Column(db.Integer(), db.ForeignKey('modules.uid', onupdate="SET NULL", ondelete="SET NULL"),
                       nullable=False)
    modules2_id = db.Column(db.Integer(), db.ForeignKey('modules.uid', onupdate="SET NULL", ondelete="SET NULL"),
                        nullable=False)
    modules1 = db.relationship("Modules", back_populates="mdep1")
    modules2 = db.relationship("Modules", back_populates="mdep2")
    deprate = db.Column(db.Float(), nullable=True)
    dep_cat = db.Column(db.String(50), nullable=False)

    def __init__(self, modules1_id: int, modules2_id: int):
        self.modules2_id = modules2_id
        self.modules1_id = modules1_id

    def __repr__(self):
        return "< {0} {1} {2}>".format(self.uid, self.modules2_id, self.modules1_id)
