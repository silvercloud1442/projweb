import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'category'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    prog = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    des = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    av = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    mrk = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    tw = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)

    categories = orm.relationship("User", backref="categories")