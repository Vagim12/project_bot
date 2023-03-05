import random
import discord
from discord.ext import commands

config = {
    'token': '',
    'prefix': '$',
}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100))

bot.run(config['token'])
