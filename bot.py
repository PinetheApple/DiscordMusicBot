import disnake
from disnake.ext import commands
import music

act = disnake.Game(name='Hopefully a music bot')
bot=commands.Bot(command_prefix="t!",activity=act)
bot.color=0xff0000

cogs=[music]

for i in range(len(cogs)):
    cogs[i].setup(bot)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.channel.send("HEllO")

@bot.command()
async def ping(ctx):
    """Check my reaction time!"""
    resp = await ctx.send('Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content=f':ping_pong: Pong! **API** latency: {1000*diff.total_seconds():.1f}ms. **{bot.user.name}** latency: {round(bot.latency * 1000)}ms')

bot.run(process.env.TOKEN)
