import discord
from discord.ext import commands
import youtube_dl

class music_player(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, context):
        if context.author.voice is None:
            await context.send("You're not in a voice channel you fuckin oaf")
        voice_channel = context.author.voice.channel
        if context.voice_client is None:
            await voice_channel.connect()
        else:
            await context.voice_client.move_to(voice_channel)
    
    @commands.command()
    async def disconnect(self, context):
        await context.voice_client.disconnect()
    
    @commands.command()
    async def fuckoff(self, context):
        await context.voice_client.disconnect()
    
    @commands.command()
    async def play(self, context, url):
        context.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = context.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
    
    @commands.command()
    async def pause(self, context, url):
        await context.voice_client.pause()
        await context.send("You paused dat shit")
    
    @commands.command()
    async def resume(self, context, url):
        await context.voice_client.resume()
        await context.send("You resumed dat shit")

def setup(client):
    client.add_cog(music_player(client))