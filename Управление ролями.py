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

@bot.command(pass_context=True)
async def add_role(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(role)

@bot.command(pass_context=True)
async def re_role(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await member.remove_roles(role)

@bot.command(pass_context=True)
async def create_role(ctx, name: str):
    guild = ctx.guild
    await guild.create_role(name=name)

bot.run(config['token'])






