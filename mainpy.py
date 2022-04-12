from replit import db
import discord
import os
from keep_alive import keep_alive

client=discord.Client()

def update_comm(command):
  db["command"]=command

def return_prefix():
  return db["command"]

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  msg=message.content
  author=message.author
  if author==client.user:
    return
  elif(db["response"]==False):
    if(msg.startswith("$response") and author.name==me):
      val=msg.split("$response ",1)[1]
      if((val.lower()).startswith("t")):
        if(db["response"]==False):
          db["response"]=True
          await message.channel.send("response turned on")
    else: return
  if msg.startswith('$hello'):
    await message.channel.send('hello!')
  if msg.startswith('i am') and author.name!=me and len(msg)>5:
    m=msg[5:]
    await message.channel.send("Hello {0}, I'm bot.".format(m))
  if msg.startswith("i'm") and author.name!=me and len(msg)>4:
    m=msg.content[4:]
    await message.channel.send("Hello {0}, I'm bot.".format(m))
  if msg.startswith('im') and author.name!=me and msg.index(" ")==2 and len(msg)>3:
    m=msg.content[3:]
    await message.channel.send("Hello {0}, I'm bot.".format(m))
  if msg=='$prefix':
    await message.channel.send(str(return_prefix()))
  if msg.startswith("$update prefix"):
    if(len(msg)==14):
      await message.channel.send("please specify the new prefix")
    else:
      update_comm(msg.split("$update prefix ",1)[1])
      await message.channel.send("Prefix updated successfully.")
  if(msg.startswith("$response") and author.name==me):
    val=msg.split("$response ",1)[1]
    if((val.lower()).startswith("f")):
      if(db["response"]==True):
        db["response"]=False
        await message.channel.send("response turned off")

keep_alive()
my_secret = os.environ['token']
client.run(my_secret)
