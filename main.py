import ctx as ctx
import discord
from discord import ChannelType, Channel
from discord import message
from discord.ext import commands
import random
import timelines

from discord.utils import find

import secrets
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='#', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def roll(dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices: str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))


@bot.command()
async def repeat(times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)


@bot.command()
async def joined(member: discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


@bot.command()
async def hello(message):
    await bot.say('hello')

@bot.command(pass_context=True)
async def start(ctx):
    await bot.say('starting a game of timelines')
    voice_channel = discord.utils.get(ctx.message.server.channels, name="General", type=discord.ChannelType.voice)
    members = voice_channel.voice_members

    memString = ""
    for mem in members:
        memString = memString + ", " + mem.name

    await bot.say('starting a game of timelines with' + memString)


    await timelines.startGame(members)
    timeLineString = await timelines.printTimeline()

    await bot.say("the time line is \n" + timeLineString)

    playerhands = ""
    for mem in members:
        playerhands += mem.name + " has his in hands \n"
        playerhands += str(await timelines.playerHand(mem))

    await bot.say(playerhands)
    await bot.say("Is this getting annoying yet?")




@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')


bot.run(secrets.token)