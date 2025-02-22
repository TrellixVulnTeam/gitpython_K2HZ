import sqlite3
from db import db


class ItemModel(db.Model):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def findByname(clc, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        result = result.fetchone()
        connection.close()
        if result:
            item = clc(*result)
            return item.json(), 200

    def writeItem(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        insert_query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(insert_query, (self.name, self.price))
        connection.commit()
        connection.close()

    def updateItem(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        update_query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(update_query, (self.price, self.name))
        connection.commit()
        connection.close()
