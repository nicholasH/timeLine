import sqlite3
import card
import csv
conn = sqlite3.connect('history.db')


def createDB():
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE events (ID INTEGER primary key, name STRING, year STRING, bc STRING, info STRING)''')
    conn.commit()


def destroyDB():
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS events')
    conn.commit()

def addEvent(name,year,bc,info):
    c = conn.cursor()
    c.execute(
        "INSERT INTO events VALUES (?,?,?,?,?)", (
            None,
            name,
            year,
            bc,
            info
        ))
    conn.commit()

def getPlayingDeck():
    print("here")
    c = conn.cursor()
    c.execute("SELECT * FROM events")
    conn.commit()
    data = c.fetchall()
    fomantedData = reformatToCard(data)
    return fomantedData

def reformatToCard(data):
    returnData = []

    for c in data:
        returnData.append(card.Card(c[0],c[1],c[2],c[3],c[4]))

    return returnData

def addCardpack(pathToCardpack):
    c = conn.cursor()
    with open(pathToCardpack,"r") as file:
        dr =csv.DictReader(file)
        to_db = [(None,i["name"],i["year"],i["bc"],i['info']) for i in dr]

        c.executemany("INSERT INTO events VALUES (?, ?, ?, ?, ?);", to_db)
        conn.commit()
