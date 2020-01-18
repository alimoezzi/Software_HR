from Models.Models import db


class Tag(db.Model):
    __tablename__ = 'tags'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    repos = db.relationship('Repo_Tag', back_populates='tag', passive_deletes=False, cascade="save-update, merge")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "< {0} {1} {2}>".format(self.uid, self.name, 'tag')
