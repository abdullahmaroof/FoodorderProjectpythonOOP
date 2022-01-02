import xlsxwriter as excelWriter
from sqlite3 import *
import datetime

con = connect("UserInfo.db")
sql = """SELECT * From UserData"""
cursor = con.cursor()
cursor.execute(sql)
x = cursor.fetchall()

def excelUSERReportGeneration():
    currentDataAndTime = datetime.datetime.now()
    dateAndTime = currentDataAndTime.strftime("%Y.%m.%d-%H.%M.%S")
    excelfileName = "user-report-" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()
    row = 0
    column = 0

    for eachRow in x:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0
    myWorkbook.close()