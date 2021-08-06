import os
import random
import logging

import discord #discord python library
from discord.ext import commands #discord python library for bot specific features

import nest_asyncio #needed to run async in IDEs without async 
from dotenv import load_dotenv #allows creation of environment variables

#logging setup
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs\discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#applies async capabilities and looks for env variables
nest_asyncio.apply()
load_dotenv()

#get env variables
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')
CHANNEL = os.getenv('DISCORD_CHANNEL')
print(CHANNEL)

#intents are required from discord API now
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
description = "A bot to track the accountability of users and provide reminders."

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

########################### CODE COMMANDS HERE ##########################


@bot.command(name='check_ctx')
async def check_context(ctx):
    if str(ctx.channel) != str(CHANNEL):
        return
    await ctx.send("you're in the correct channel :)!")

@box.command(name='
    
















########################### CODE COMMANDS HERE ##########################


    
#client.run(TOKEN)
bot.run(TOKEN)
