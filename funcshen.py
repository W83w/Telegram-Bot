import sqlite3


def sqlfunc():
    con = sqlite3.connect( "itbotproger.db") # Создаю базу sql
    cur = con.cursor()

    cur.execute("""CREATE TABLE ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    title TEXT NOT NULL, 
    description_image TEXT NOT NULL, 
    name_user TEXT NOT NULL, 
    name_image TEXT NOT NULL);""") #Создаю таблицу если ее нет sql запросом
    cur.commit()