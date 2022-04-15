import discord
from discord.ext import commands
import music

client=commands.Bot(command_prefix='t!',intents=discord.Intents.all())

cogs=[music]

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

client.run("token")
