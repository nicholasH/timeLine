import sqlite3
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

async def getPlayingDeck():
    c = conn.cursor()
    c.execute("SELECT * FROM events")
    conn.commit()
    data = c.fetchall()
    return data


