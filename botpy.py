import lightbulb
import hikari
import os

bot=lightbulb.BotApp(
    token="e", 
    prefix='!',
    default_enabled_guilds=3234234234324234 #random
)

@bot.listen(hikari.StartedEvent)
async def bot_on(event):
  print("Bot is online.")

'''@bot.listen(hikari.VoiceEvent)
async def vc(event):
  if(event!=None):
    await bot.update_voice_state(event.guild_id, event.channel_id)
  else:
    await bot.update_voice_state(event.guild_id,None)''' #due to errors

@bot.command
@lightbulb.command('ping','replies with pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
  await ctx.respond('Pong!')

@bot.listen(hikari.GuildMessageCreateEvent)
async def hello(ctx):
  if ctx.content == 'hello there':
    await ctx.message.add_reaction('🤝')

@bot.command
@lightbulb.command("ping", "checks if the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand)
async def pings(ctx: lightbulb.Context) -> None:
  await ctx.respond("Pong!")

"""@bot.command
@lightbulb.command('group','This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def gp1(ctx):
  pass

@gp1.child
@lightbulb.command('subcommand','this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subgp1(ctx):
  await ctx.respond('a subcommand this is')"""

@bot.command
@lightbulb.option('num2','first number', type=int)
@lightbulb.option('num1','second number',type=int)
@lightbulb.command('add','adds two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def adding(ctx):
  await ctx.respond(ctx.options.num2+ctx.options.num1)

bot.run()
