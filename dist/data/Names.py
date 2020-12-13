import sqlalchemy

from .db_session import SqlAlchemyBase

class User(SqlAlchemyBase):
    __tablename__ = "Santa_list"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    gift_person = sqlalchemy.Column(sqlalchemy.String)