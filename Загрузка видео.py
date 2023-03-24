import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

youtube_dl.utils.bug_reports_message = lambda: x
ytdl_format_options = {
    'format':'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist':True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet':True,
    'no_warnings':True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}
ffmpeg_options = {
    'options':'-vn'
}
ytdl = youtube_dl.YoutubeDL (ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume= 0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url =  ""
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries'in data:
            data = data ['entries'][0]
            filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

bot.run(config['token'])






