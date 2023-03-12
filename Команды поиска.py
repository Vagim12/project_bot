import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import re
import urllib

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def ball(ctx):
    response =[
        'Без сомнения.', 
        'Хорошая перспектива.', 
        'Лучше об этом не думать.', 
        'Не могу предсказать сейчас.',
        'Мой ответ - нет.', 
        'Мне кажется это плохая идея.',
    ]

    await ctx.send(random.choice(response))

@bot.command()
async def gif(msg, *, search):
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen("https://giphy.com/search/" + query_string)
    search_results = re.findall(query_string[13:], html_content.read().decode())
    await msg.send("https://giphy.com/search/" + search_results[0])    

@bot.command()
async def yt(msg, *, search):
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    await msg.send("http://www.youtube.com/watch?v=" + search_results[0])

bot.run(config['token'])






