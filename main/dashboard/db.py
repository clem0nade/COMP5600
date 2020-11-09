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