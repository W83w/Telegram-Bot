import sqlite3


def sqlfunc():
    con = sqlite3.connect("itbotproger.db") # Создаю базу sql
    cun = con.cursor()

    cun.execute("""CREATE TABLE table ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    title TEXT NOT NULL, 
    description_image TEXT NOT NULL, 
    name_user TEXT NOT NULL, 
    name_image TEXT NOT NULL);""") #Создаю таблицу если ее нет sql запросом
    cun.commit()