from sqlalchemy import Table, Text, UniqueConstraint
from Models.Models import db


class Repo_Tag(db.Model):
    __tablename__ = 'repo_tag'
    uid = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    tag_id = db.Column(db.Integer(), db.ForeignKey('tags.uid', onupdate="SET NULL", ondelete="SET NULL"),
                       nullable=False)
    repo_id = db.Column(db.Integer(), db.ForeignKey('orig_repos.uid', onupdate="SET NULL", ondelete="SET NULL"),
                        nullable=False)
    tag = db.relationship("Tag", back_populates="repos")
    repo = db.relationship("OrigRepos", back_populates="tags")

    def __init__(self, tag_id: int, repo_id: int):
        self.tag_id = tag_id
        self.repo_id = repo_id

    def __repr__(self):
        return "< {0} {1} {2}>".format(self.uid, self.tag_id, self.repo_id)
