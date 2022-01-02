import xlsxwriter as excelWriter
import sqlite3
import datetime

conn = sqlite3.connect("MenuData.db","BillRecord.db")
cur = conn.cursor()
sql = """SELECT * FROM menu LEFT JOIN bill ON menu.food = bill.food"""
cur.execute(sql)

def exceloracleReportGeneration():
    currentDataAndTime = datetime.datetime.now()
    dateAndTime = currentDataAndTime.strftime("%Y.%m.%d-%H.%M.%S")
    excelfileName = "oraclejoin-report-" + str(dateAndTime) + ".xlsx"
    myWorkbook = excelWriter.Workbook(excelfileName)
    myWorksheet = myWorkbook.add_worksheet()
    row = 0
    column = 0

    for eachRow in cur:
        for eachItem in eachRow:
            myWorksheet.write(row, column, eachItem)
            column = column + 1
        row = row + 1
        column = 0
    myWorkbook.close()
    conn.commit()
    conn.close()
