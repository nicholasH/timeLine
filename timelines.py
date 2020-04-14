import random

import discord
import DBHandler
from card import Card
import os

playersDecks = dict()
inPlayDeck = list()
discardDeck = list()

startingCards = 3
timeline = list()

cardpackDir = "E:\discordBot\TimeLineBot\cardpacks"

async def test(bot):
    await bot.say('Yes, the bot is cool.')

async def startGame(members):
    global timeline
    global inPlayDeck

    timeline.clear()
    inPlayDeck = DBHandler.getPlayingDeck()
    print(len(inPlayDeck))
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
    order = 0

    timelineString += "Before \n"
    for card in timeline:
        timelineString += str(order)
        timelineString += ': '
        timelineString += str(card.name)
        timelineString += " "
        timelineString += str(card.year)
        timelineString += "BC" if card.bc_ac == -1 else ""
        timelineString += "\n"
        order += 1
    timelineString += "After \n"
    return timelineString


async def printPlayerHand(player):
    hand = ""
    order = 0

    for card in playersDecks[player]:
        hand += str(order)
        hand += ': '
        hand += str(card.name)
        hand += "\n"
        order += 1

    return hand


async def orderTimeLine():
    bc = list()
    ca = list()

    global timeline
    for card in timeline:
        if(card.bc_ac==-1):
            bc.append(card)
        else:
            ca.append(card)

    bc.sort(key= lambda x: x.year, reverse=True)
    ca.sort(key= lambda x: x.year)

    timeline = bc + ca

#attemps to places the cards before the card in the time line.
async def before(member,handPostion,timeLinePostion):
    global inPlayDeck
    deck = playersDecks[member]
    card = deck[handPostion]
    try:
        tlCardBefore = timeline.index(timeLinePostion - 1)
    except:
        tlCardBefore = None

    tlCard = timeline[timeLinePostion]

    if await isMiddle(card,tlCardBefore,tlCard):
        del deck[handPostion]
        timeline.insert(timeLinePostion,card)
        return True
    else:
        playersDecks[member].append(inPlayDeck.pop(0))
        del deck[handPostion]
        inPlayDeck.append(card)
        return False

#attemps to places the cards after the card in the time line.
async def after(member, handPostion, timeLinePostion):
    global inPlayDeck
    print(len(inPlayDeck))

    deck = playersDecks[member]
    card = deck[handPostion]
    try:
        tlCardAfter = timeline.index(timeLinePostion + 1)
    except:
        tlCardAfter = None

    tlCard = timeline[timeLinePostion]

    if await isMiddle(card,tlCard,tlCardAfter):
        del deck[handPostion]
        timeline.insert((timeLinePostion + 1),card)
        return True

    else:
        playersDecks[member].append(inPlayDeck.pop(0))
        del deck[handPostion]
        inPlayDeck.append(card)
        return False


async def isMiddle(card:Card ,cardBefore:Card,cardAfter:Card):
    isMiddleCard = False
    print(cardBefore,card,cardAfter)
    if cardAfter is None:
        if card > cardBefore:
            isMiddleCard = True

    elif cardBefore is None:
        if card < cardAfter:
            isMiddleCard = True

    elif(card > cardBefore and card < cardAfter):
        isMiddleCard = True

    return isMiddleCard

async def refeshPlayingDeck():
    DBHandler.destroyDB()
    DBHandler.createDB()

    for filename in os.listdir(cardpackDir):
        if filename.endswith(".csv"):
            DBHandler.addCardpack(cardpackDir+"\\"+filename)
            continue
        else:
            continue