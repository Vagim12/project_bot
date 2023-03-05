import discord
from discord.ext import commands
from random import randint
from datetime import date

config = {
    'token': '',
    'prefix': '$',
}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def dt(ctx):
    current_date = date.today()
    await ctx.send(f"Сегодняшняя дата: {current_date}.")

@bot.command()
async def paswd(ctx, *arg):
    pas = "qwe1rty2uio3plk4j5h6gfds7az8x9cvb0nmQWERTYUIOPLKJHGFDSAZXCVBNM"
    a = ''
    for _ in range(8):
        a += pas[randint(0, 61)]
    await ctx.reply(f'{a}')



bot.run(config['token'])
