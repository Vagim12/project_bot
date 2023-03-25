import discord
from discord.ext import commands
import random

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def prob(ctx):
    phrase = ["Я думаю вероятность этого",
              "Вселенная подсказывает, что вероятность этого",
              "Мне кажется, это произойдет с шансом",
              "В моих мыслях всплывает вероятность"]
    integer = random.randint(0, 101)
    random_index = random.randint(0, len(phrase) - 1)
    await ctx.reply(f'{phrase[random_index]} {integer}%')

@bot.command()
async def YN(ctx, arg):
    yes = ["Да", "Нет"]
    no = random.randint(0, 1)
    await ctx.reply(f'{yes[no]}')
    

bot.run(config['token'])






