import pymysql
import dbconfig
connection = pymysql.connect(host="123.56.21.248",
                             user=deconfig.db_user,
                             passwd=dbconfig.db_password)
try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes(
id int NOT NULL AUTO_INCRRMENT,
latitude FLOAT(10, 6),
longitude FLOAT(10, 6),
data DATETIME,
category VARCHAR(50),
description VARCHAR(1000),
updateed_at TIMESTAMP,
PRIMARY KEY (id)
)"""
        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()