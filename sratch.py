import DBHandler
import random

DBHandler.destroyDB()
DBHandler.createDB()



def realcard():
    #DBHandler.addEvent("start of the revolutionary war","1775","","")
    #DBHandler.addEvent("USA lands on the moon","1969","","")


    #DBHandler.addEvent("Fall of the berlin wall","1991","","")
    #DBHandler.addEvent("Fall of the rome","476","","")
    #DBHandler.addEvent("Fall of the Soviet Union","1991","","")

    #DBHandler.addEvent("Treaty of versailles signed","1919","","")
    #DBHandler.addEvent("Treaty of paris","476","","")

    #DBHandler.addEvent("Assassination of julius Caesar", "44","bc","")
    #DBHandler.addEvent("Construction of the Great Pyramid of Giza", "2560","bc","")
    #DBHandler.addEvent("Founding of rome","753","bc","")

    #DBHandler.addEvent("Curiosity mars rover landed","2012","","")
    #DBHandler.addEvent("Sputnik launched","2057","","")
    return

def testCardsGenerator():
    for x in range(1,100):
        DBHandler.addEvent(str(x), str(x), "", "")
    for x in range(1,100):
        DBHandler.addEvent(str(x) + "bc", str(x), "bc", "")

testCardsGenerator()
l =  DBHandler.getPlayingDeck()

print(l)

print(random.shuffle(l))

print(l)