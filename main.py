import discord

from discord.ext import commands
import random
import timelines


import secrets
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='`', description=description)
@commands.bot_has_permissions(read_messages = True)


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
    timeLineChannel = discord.utils.get(bot.get_all_channels(), name='timeline-game')

    async for message in timeLineChannel.history(limit=1000):
        await message.delete()
        print("deleted message")


    text_channel = ctx.channel
    await text_channel.send("starting a game of time lines")

    voice_channel = ctx.author.voice.channel
    members = voice_channel.members

    memString = ""
    for mem in members:
        memString = memString + ", " + mem.name

    await timeLineChannel.send('starting a game of timelines with' + memString)


    await timelines.startGame(members)
    timeLineString = await timelines.printTimeline()

    await timeLineChannel.send("the time line is \n" + timeLineString)

    playerhands = "hands \n"
    for mem in members:
        playerhands += mem.name + " has this in hands \n"
        playerhands += str(await timelines.printPlayerHand(mem))
        playerhands += "\n_______________________________________________________"

    await timeLineChannel.send(playerhands)


#attemps to places a card in order
#place 1 befor 5
@bot.command(pass_context=True)
async def put(ctx,*args):
    timeLineChannel = discord.utils.get(bot.get_all_channels(), name='timeline-game')

    result = False
    if(args[1] == "before"):
        result = await timelines.before(ctx.message.author ,int(args[0]), int(args[2]))
    elif(args[1] == "after"):
        result = await timelines.after(ctx.message.author ,int(args[0]), int(args[2]))

    if(result):
        await timeLineChannel.send(ctx.message.author.name + " is correct")
        await timeLineChannel.send(await timelines.printTimeline())
    else:
        await timeLineChannel.send(ctx.message.author.name + " incorrect")

#prints players hand.
@bot.command(pass_context=True)
async def hand(ctx,*args):
    timeLineChannel = discord.utils.get(bot.get_all_channels(), name='timeline-game')
    await timeLineChannel.send("Your hand is")
    await timeLineChannel.send(await timelines.printPlayerHand(ctx.message.author))

#prints players hand.
@bot.command(pass_context=True)
async def tl(ctx,*args):
    timeLineChannel = discord.utils.get(bot.get_all_channels(), name='timeline-game')
    await timeLineChannel.send("The time line is")
    await timeLineChannel.send(await timelines.printTimeline())

#prints players hand.
@bot.command(pass_context=True)
async def packCards(ctx,*args):
    timeLineChannel = discord.utils.get(bot.get_all_channels(), name='timeline-game')
    await timeLineChannel.send("packing cards")
    await timelines.refeshPlayingDeck()

@bot.command(pass_context=True)
async def clearGame(ctx,*args):
    timeLineChannel = discord.utils.get(bot.get_all_channels(), name='timeline-game')
    async for message in timeLineChannel.history(limit=1000):
        await message.delete()
        print("deleted message")


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


@bot.command(pass_context=True)
async def speak(ctx,*args):
    channel = ctx.channel
    lines = open("E:\discordBot\TimeLineBot\TimeLineBot\speech").read().splitlines()
    line = random.choice(lines)
    await channel.send(line, tts=True)


@bot.command(pass_context=True)
async def test(ctx,*args):
    channel = ctx.channel
    await channel.send("ţ̴̥̜͓̗͖̱̘͂̉̽́͂̌͜͜e̶͔̭̘̼̜̞͑̓̍́͜ṡ̸̢̜̤̠̩̊̑̕͘ẗ̶͉̬̝́̈̌͜͝")

bot.run(secrets.token)