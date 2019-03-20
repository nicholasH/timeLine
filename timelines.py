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

async def printTimeline():
    timelineString = ""
    global timeline
    for x in timeline:
        timelineString += str(x[0])
        timelineString += "\n"
    return timelineString


async def playerHand(player):
    hand = ""

    for x in playersDecks[player]:
        hand += str(x[0])
        hand += "\n"



    return hand

