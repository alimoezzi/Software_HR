from Models.Models import db


class Software(db.Model):
    __tablename__ = 'software'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    version = db.Column(db.Float(), nullable=True)
    pkgname = db.Column(db.String(50), nullable=False)
    repo_id = db.Column(db.Integer(), db.ForeignKey('orig_repost.uid',onupdate="SET NULL", ondelete="SET NULL"), nullable=True)

    def __init__(self,pkgname: str, repo_id=None):
        self.pkgname = pkgname
        self.repo_id = repo_id

    def __repr__(self):
        return "< {0} {1} {2}>".format(self.uid, self.pkgname, 'software')
