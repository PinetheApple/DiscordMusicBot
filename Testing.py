import discord
from discord.ext import commands

import asyncio
bot = commands.Bot(command_prefix='p!')
@bot.event
async def on_ready():
    print("The bot is ready!")
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
bot.run('P_Bot')

