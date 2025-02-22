import sqlite3
from db import db


class UserModel(db.Model):

    __tablename__ = "user"
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.String(80))
    password = db.column(db.String(80))

    def __init__(self, _id, username, password):

        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findByUsername(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def findById(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user


for num in [1, 2, 3, 4]:
    print(num)
