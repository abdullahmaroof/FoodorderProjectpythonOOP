from sqlite3 import *

con = connect("UserInfo.db")
#sql = """CREATE TABLE UserData (firstname TEXT, secondname TEXT, email TEXT, age INTEGER, password TEXT)"""
#sql = """INSERT INTO UserData VALUES ('zubair','ali','zubair@gmail.com',20,'1234')"""
#sql = """INSERT INTO UserData VALUES ('abdullah','maroof','abdullah@gmail.com',20,'1234')"""
cursor = con.cursor()
cursor.execute(sql)

con.commit()
con.close()
