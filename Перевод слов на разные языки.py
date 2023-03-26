import discord
from discord.ext import commands
from discord.utils import get
from googletrans import Translator

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def tr(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)

bot.run(config['token'])






