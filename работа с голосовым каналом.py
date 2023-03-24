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

@bot.command(name='join', help='Сообщает боту присоединиться к голосовому каналу')
async def ms(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f"{ctx.message.author.name} не подключен к голосовому каналу")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='Чтобы заставить бота покинуть голосовой канал')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if ctx.guild.voice_client in bot.voice_clients:
        await voice_client.disconnect()
    else:
        await ctx.send(f"Бот не подключен к голосовому каналу")

bot.run(config['token'])






