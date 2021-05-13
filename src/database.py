from settings import *
import datetime
import os
import pandas as pd
import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()

        try:
            self.create_table()
        except Exception as e:
            print(e)

    def connect_to_database(self):
        connection = sqlite3.connect("{}.db".format(self.db_name))
        return connection

    def create_table(self):
        self.connection.cursor().execute(
            """CREATE TABLE data(
            filename TEXT NOT NULL,
            mean REAL NOT NULL,
            median REAL NOT NULL,
            std REAL NOT NULL);"""
        )
        self.connection.commit()

    def insert_into_table(self, filename, mean, median, std):
        params = (filename, mean, median, std)
        self.cursor.execute(
            """INSERT INTO data (
            filename, 
            mean, 
            median, 
            std) VALUES (?, ?, ?, ?);""",
            params,
        )
        self.connection.commit()

    def save_as_CSV(self):
        db = pd.read_sql_query("SELECT * FROM data;", self.connection)
        db.to_csv("../data/{}.csv".format(CSV_NAME), index=False)

    def delete(self):
        self.connection.close()
        os.remove(self.db_name + ".db")
