import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def _init_(self,client):
        self.client=client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Please join a voice channel before using this command.")
        v_c = ctx.author.voice.channel
        if ctx.voice_client is None:
            await v_c.connect()
        else:
            await ctx.voice_client.move_to(v_c)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS={"before_options": "reconnect 1 -reconnect_steamed 1 -reconnect_delay_max 5","options":"-vn"}
        YDL_OPTIONS={'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info=ydl.extract_info(url,download=False)
            url2= info['format'][0]['url']
            source= await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused.")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resumed.")

def setup(client):
    client.add_cog(music(client))