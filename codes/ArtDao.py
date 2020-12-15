#これが提出用、もう編集しないこと

import mysql.connector
import dbconfig as cfg

class ArtDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['username'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )
        print("connection made")

    def create (self,art):
        cursor = self.db.cursor()
        sql = "insert into art (id, title,author, price) values (%s,%s,%s,%s)"
        values = [
            art['id'],
            art['title'],
            art['author'],
            art['price']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from art'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results :
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self,id):
        cursor = self.db.cursor()
        sql = 'select * from art where id = %s'
        values = [id]
        cursor.execute(sql,values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self,art):
        cursor = self.db.cursor()
        sql = "update art set title = %s, author = %s, price = %s where id =%s"
        values = [
            art['title'],
            art['author'],
            art['price'],
            art['id']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        return art

    def delete(self, id):
        cursor = self.db.cursor()
        sql = 'delete from art where id = %s'
        values = [id]
        cursor.execute(sql,values)
        return {}


    def convertToDict(self,result):
        colnames = ['id','title','author','price']
        art = {}

        if result :
            for i, colName in enumerate (colnames):
                value = result [i]
                art[colName] = value
        return art        

artDao = ArtDao()