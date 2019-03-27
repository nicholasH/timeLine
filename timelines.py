import random

import discord
import DBHandler

playersDecks = dict()
inPlayDeck = list()
discardDeck = list()

startingCards = 3;


timeline = list()





async def test(bot):
    await bot.say('Yes, the bot is cool.')

async def startGame(members):
    global timeline
    inPlayDeck = await DBHandler.getPlayingDeck()

    random.shuffle(inPlayDeck)

    print(startingCards)

    for mem in members:
        x = 0
        playersDecks[mem] = list()
        while(x<startingCards):
            playersDecks[mem].append(inPlayDeck.pop(0))
            x += 1

    timeline.append(inPlayDeck.pop(0))
    timeline.append(inPlayDeck.pop(0))

    await orderTimeLine()

async def printTimeline():
    timelineString = ""
    global timeline
    for x in timeline:
        timelineString += str(x[1])
        timelineString += "\n"
    return timelineString


async def playerHand(player):
    hand = ""

    for x in playersDecks[player]:
        hand += str(x[0])
        hand += "\n"

    return hand



async def orderTimeLine():
    bc = list()
    ca = list()

    global timeline
    for event in timeline:
        if(event[3]=="bc"):
            bc.append(event)
        else:
            ca.append(event)

    bc.sort(key= lambda x: x[1], reverse=True)
    ca.sort(key= lambda x: x[1])

    timeline = bc + ca






async def before(member,handPostion,timeLinePostion):
    deck = playersDecks[member]
    card = deck[handPostion]
    tlCardBefore = timeline[timeLinePostion - 1]
    tlCard = timeline[timeLinePostion]

    if(tlCardBefore[3] == "bc" and tlCard[3] == "bc" ):
        if(card[3] != "bc"):
            return False
        elif(card[2] > tlCardBefore[2] or card[2] < tlCard[2] ):
            return False
        else:
            return True
    elif(tlCardBefore[3] == "" and tlCard[3] == ""):
        if(card[3] != ""):
            return False
        elif(card[2] < tlCardBefore[2] or card[2] > tlCard[2] ):
            return False
        else:
            return True
    elif(tlCardBefore[3] == "bc" and tlCard[3] == ""):
        if(card[3] == "bc"):
            if(card[2] > tlCardBefore[2]):
                return False
            else:
                return True
        elif(card[3] == ""):
            if(card[2] > tlCard[2]):
                return False
            else:
                return True



async def after(member, handPostion,timeLinePostion):
    return
