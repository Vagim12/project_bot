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
async def ser_info(ctx, *, server: discord.Guild = None):
    if server == None:  
        server = ctx.guild
    embedVar = discord.Embed(color=0xfaa61a)
    date_format = "%a, %d %b %Y %I:%M %p"
    embedVar.add_field(name="Создан:", value=server.created_at.strftime(date_format))
    embedVar.add_field(name="Количество учатсников", value=sum(not member.bot for member in ctx.guild.members))
    embedVar.add_field(name="Боты", value=sum(member.bot for member in ctx.guild.members))

    if server.premium_tier == 0:
        embedVar.add_field(name="Уровень буста", value='0')
    if server.premium_tier == 1:
        embedVar.add_field(name="Уровень буста", value='1')
    if server.premium_tier == 2:
        embedVar.add_field(name="Уровень буста", value='2')
    if server.premium_tier == 3:
        embedVar.add_field(name="Уровень буста", value='3')
    
    embedVar.add_field(name="Владелец", value=server.owner)
    return await ctx.send(embed=embedVar)

bot.run(config['token'])






