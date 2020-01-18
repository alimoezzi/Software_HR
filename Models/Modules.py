from Models.Models import db


class Modules(db.Model):
    __tablename__ = 'modules'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    sid = db.Column(db.Integer(), db.ForeignKey('software.uid',onupdate="SET NULL", ondelete="SET NULL"), nullable=True)
    security_issues = db.Column(db.Integer(), nullable=True)
    performance = db.Column(db.Integer(), nullable=True)
    inlining_performance = db.Column(db.Integer(), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    cat = db.Column(db.String(50), nullable=False)
    language = db.Column(db.Text(300), nullable=True)
    mdep1 = db.relationship('Modules_Modules', back_populates='modules1', passive_deletes=False, cascade="save-update, merge")
    mdep2 = db.relationship('Modules_Modules', back_populates='modules2', passive_deletes=False, cascade="save-update, merge")

    def __init__(self, sid: int, security_issues: int, name: str, performance: int, inlining_performance: int, cat: str,language: str):
        self.sid = sid
        self.security_issues = security_issues
        self.name = name
        self.performance = performance
        self.cat = cat
        self.language = language
        self.inlining_performance = inlining_performance


    def __repr__(self):
        return "< {0} {1} {2}>".format(self.uid, self.name, 'origrepos')
