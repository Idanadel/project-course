import sqlite3


class DBhandler:
    def __init__(self, name:str): # constructor
        if isinstance(name, str):
            self.DBname = name
        else:
            raise ValueError ("DB name Must be a STRING!")


    @property
    def name(self):
        return self.DBname
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.DBname = value
        else:
            raise ValueError ("DB name Must be a STRING!")

    def __str__(self):
        return f"DataBase name: {self.DBname}"
