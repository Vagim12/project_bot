import discord
from discord.ext import commands

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command(pass_context=True)
async def new_voice(ctx, name):
    await ctx.guild.create_voice_channel(name)
    await ctx.send(f'Канал {name} успешно создан. Можете общаться!')

@bot.event
async def on_guild_join(guild):
    text_channels = guild.text_channels
    if text_channels:
        channel = text_channels[0]
    await channel.send('Привет, {guild.name}! Для ознакомления с инструкцией ко мне напишите "$help"')   

bot.run(config['token'])






