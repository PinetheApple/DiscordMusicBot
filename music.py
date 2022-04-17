from http import client
import discord
from discord.ext import commands
import youtube_dl
from requests import get
import asyncio

class Queue():
    def _init_(self,song):
        self.song=song
        self.next=None

    

class music(commands.Cog):
    def _init_(self,client):
        self.client=client

    def search(arg,YDL_OPTIONS):
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            try:
                get(arg) 
            except:
                video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            else:
                video = ydl.extract_info(arg, download=False)

        return video

    def play(vc):
        e='e'

    @commands.command(aliases=['j'])
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Please join a voice channel before using this command.")
            return
        vc = ctx.author.voice.channel
        if ctx.voice_client is None:
            await vc.connect()
        else:
            await ctx.voice_client.move_to(vc)

    @commands.command(aliases=['dc', 'disconnect'])
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command()
    async def play(self,ctx):
        #ctx.voice_client.stop()
        url=ctx.message.content.split("t!play ",1)[1]
        FFMPEG_OPTIONS={"options":"-vn"}
        YDL_OPTIONS={'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info=music.search(url,YDL_OPTIONS)
            url2= info['formats'][0]['url']
            source= await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            await ctx.send(f"Now Playing: **{url}**")
            vc.play(source)
            while ctx.voice_client.is_playing():
                await asyncio.sleep(1)
            print("song ended boop")

    @commands.command(aliases=['stop'])
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused.")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resumed.")

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

def setup(client):
    client.add_cog(music(client))
