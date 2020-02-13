from Models.Models import db


class OrigRepos(db.Model):
    __tablename__ = 'orig_repos'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    gid = db.Column(db.Integer(), nullable=True)
    star = db.Column(db.Integer(), nullable=True)
    open_issue = db.Column(db.Integer(), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=True)
    comfork = db.Column(db.Boolean, default=False, server_default='false')
    fork = db.Column(db.Integer(), db.ForeignKey('orig_repos.uid',onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    tags = db.relationship('Repo_Tag', back_populates='repo', passive_deletes=False, cascade="save-update, merge")

    def __init__(self, gid: int, star: int, open_issue: int, name: str, description: str, comfork: bool,fork=None):
        self.gid = gid
        self.star = star
        self.open_issue = open_issue
        self.name = name
        self.description = description
        self.comfork = comfork
        self.fork = fork

    def __repr__(self):
        return "< {0} {1} {2}>".format(self.uid, self.name, 'origrepos')
