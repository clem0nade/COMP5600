import sqlite3
from sqlite3 import Error
import os.path

def getAllAgeRates(namesIn):
    connection = sqlConnect()
    sql_Select = "select * from Age"
    cursor = connection.cursor()
    cursor.execute(sql_Select)
    records = cursor.fetchall()
    age1 = []
    age2 = []
    age3 = []
    age4 = []

    for row in records:
        for name in namesIn:
            if(name == row[0]):
                age1.append(row[3]/row[2])
                age2.append(row[4]/row[2])
                age3.append(row[5]/row[2])
                age4.append(row[6]/row[2])
    
    cursor.close()
    return age1, age2, age3, age4

def getAllEducation(namesIn):
    connection = sqlConnect()
    sql_Select = "select * from Education"
    cursor = connection.cursor()
    cursor.execute(sql_Select)
    records = cursor.fetchall()
    edu1 = []
    edu2 = []
    edu3 = []
    edu4 = []
    edu5 = []
    edu6 = []
    edu7 = []
    edu8 = []
    edu9 = []

    for row in records:
        for name in namesIn:
            if(name == row[0]):
                edu1.append(row[3]/row[2])
                edu2.append(row[4]/row[2])
                edu3.append(row[5]/row[2])
                edu4.append(row[6]/row[2])
                edu5.append(row[7]/row[2])
                edu6.append(row[8]/row[2])
                edu7.append(row[9]/row[2])
                edu8.append(row[10]/row[2])
                edu9.append(row[11]/row[2])
    
    cursor.close()
    return edu1, edu2, edu3, edu4, edu5, edu6, edu7, edu8, edu9


def fetchAge():
    connection = sqlConnect()
    sql_Select = "select * from Age"
    cursor = connection.cursor()
    cursor.execute(sql_Select)
    records = cursor.fetchall()
    cursor.close()
    return records


def fetchEducation():
    connection = sqlConnect()
    sql_Select = "select * from Education"
    cursor = connection.cursor()
    cursor.execute(sql_Select)
    records = cursor.fetchall()
    cursor.close()
    return records


def sqlConnect():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "CensusData.db")
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection