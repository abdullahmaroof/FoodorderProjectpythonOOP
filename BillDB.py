from sqlite3 import *

con = connect("BillRecord.db")
#sql = """CREATE TABLE bill (billno INTEGER, food TEXT, flavour TEXT, size TEXT, price INTEGER)"""
#sql = """INSERT INTO bill VALUES (1786,'pizza','smoke mexico','medium 8\"',800)"""
#sql = """SELECT * FROM bill"""
cursor = con.cursor()
#cursor.execute(sql)
#x = cursor.fetchall()
con.commit()
con.close()
#print(x)