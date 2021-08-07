from datetime import datetime, timedelta

from random import choice, randint
from typing import Optional
from asyncio import sleep

from discord import Embed, Member
from discord.ext.commands import Cog, Greedy
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions, bot_has_permissions

from ..db import db

class User(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="hello", aliases=["hi"])
    async def somecommand(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")
            
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("user")
        
def setup(bot):
    bot.add_cog(user(bot))
    
