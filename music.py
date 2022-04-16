import discord
from discord.ext import commands
import youtube_dl
from requests import get

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
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS={"options":"-vn"}
        YDL_OPTIONS={'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info=music.search(url,YDL_OPTIONS)
            url2= info['formats'][0]['url']
            source= await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)
            await ctx

    @commands.command(aliases=['stop'])
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused.")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resumed.")

def setup(client):
    client.add_cog(music(client))
