import discord
from discord.ext import commands
from discord.utils import get

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def new_channel(ctx, name: str):
    guild = ctx.message.guild
    channel = await guild.create_text_channel(name)
    channel1 = bot.get_channel(channel.id)
    await channel1.send('Приветствую в новом канале. Можете общаться!')

@bot.command()
async def new_category(ctx, name: str):
    guild = ctx.message.guild
    category = await guild.create_category(name)
    await ctx.send('Категория успешно создана!')
    
bot.run(config['token'])






