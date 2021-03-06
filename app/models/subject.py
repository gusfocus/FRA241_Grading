import sqlite3
from flask import url_for


# declare class
class Subject:
    # when create function
    def __init__(self, Subject_Id, Year):
        # declare attribute when create
        self.Subject_Id = Subject_Id
        self.Year = Year
        # make a dictionary
        self.data = self.Get_data()
        self.Status = ""
        self.Work = ""  # url_for('static', filename='')
        self.Student = ""
        self.File = ""
        self.path =""

    def Get_data(self):
        # connect with database
        connect = sqlite3.connect('Data.db')
        # create a being that process data (go get filter etc.)
        c = connect.cursor()
        # get table column
        tableField = c.execute("PRAGMA table_info(subject)")
        tableField = tableField.fetchall()
        column = []
        for x in tableField:
            column.append(str(x[1]))
        # get profile data
        myData = c.execute("SELECT * from subject WHERE Subject_ID = ? AND Year = ?",(str(self.Subject_Id),str(self.Year)))
        k = myData.fetchone()
        # make it into dict
        datadict = {}
        for x, y in zip(k, column):
            datadict[str(y)] = str(x)
        # close connection
        c.close()
        # return the dict
        return datadict

    def get_work(self):
        # connect with database
        connect = sqlite3.connect('Data.db')
        # create a being that process data (go get filter etc.)
        c = connect.cursor()
        work = c.execute("SELECT * from work WHERE Subject_ID = ? AND Year = ?",(str(self.Subject_Id),str(self.Year)))
        work = work.fetchall()
        #close connection
        c.close()
        #return work [list]
        return work
