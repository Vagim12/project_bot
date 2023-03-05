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
async def git(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на git",
        url='https://github.com/Vagim12/project_bot',
    )
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = "В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = "Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = "Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = "Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = "В сети"

        t = member.status
        if t == discord.Status.offline:
            d = "Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = "Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = "Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)



bot.run(config['token'])
