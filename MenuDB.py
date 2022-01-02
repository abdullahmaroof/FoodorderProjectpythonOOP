from sqlite3 import *

con = connect("MenuData.db")

#sql = """CREATE TABLE menu (fastfood TEXT, taste1 TEXT, taste2 TEXT, taste3 TEXT, taste4 TEXT, taste5 TEXT)"""
#sql = """INSERT INTO menu VALUES ('Pizza','Chicken Fajita','Peeri Peeri','Smoke Mexico','Cheese Fajita','Thikka BarBQ')"""
#sql = """INSERT INTO menu VALUES ('Burger','Zinger','Beef','Chicken','Shotgun','BarBQ')"""
#sql = """INSERT INTO menu VALUES ('Biryani','Zinger','Beef','Chicken','Chinese Rice','BarBQ')"""
#sql = """INSERT INTO menu VALUES ('Paratha Roll','Zinger','Beef','Chicken','Smoke','BarBQ')"""
#sql = """SELECT * FROM menu"""
cursor = con.cursor()
#cursor.execute(sql)
#x = cursor.fetchall()
con.commit()
con.close()
#print(x)