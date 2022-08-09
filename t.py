import mysql.connector


DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Stars4343__',
    db='rak'
)
cursor = DB.cursor()
