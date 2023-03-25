import discord
from discord.ext import commands
import datetime


config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason='Ты не достоин быть здесь'):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} больше не будет мешать другим.')

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason='Вот и все'):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} зашел слишком далеко')

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, id: int) :
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f'{user} ожет быть приглашен обратно!')
        

@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    guild = ctx.guild
    await guild.create_role(name="mute")
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='mute')
    await member.add_roles(mute_role)
    await ctx.send(f'{member.mention} лишается права разговаривать')
    

@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='mute')
    await member.remove_roles(mute_role)
    await ctx.send(f'Чудо! {member.mention} снова может разговаривать!')
    

bot.run(config['token'])






