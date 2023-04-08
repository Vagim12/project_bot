import discord
import logging
import random
from discord.ext import commands
from datetime import date
from discord.ext.commands import Bot
import re
import urllib
from discord.utils import get
from discord.ext import tasks
import os
from dotenv import load_dotenv
import youtube_dl
import requests
import json
from googlesearch import search
import datetime
from googletrans import Translator
from datetime import datetime as dtte
import asyncio
import time

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)
bot.remove_command('help')
api_key = "1bbb3d633de948b0863a1c524d292fb4"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
youtube_dl.utils.bug_reports_message = lambda: x
ytdl_format_options = {
    'format':'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist':True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet':True,
    'no_warnings':True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

@bot.event
async def on_ready():
    await newloop()

@tasks.loop(hours=11) 
async def newloop():
    night = [18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5]
    day = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    now = dtte.now()
    if int(now.hour) in night: 
        with open('img1.jpg', 'rb') as image:
            await bot.user.edit(avatar=image.read())
    else:
        with open('img2.jpg', 'rb') as image:
            await bot.user.edit(avatar=image.read())

@newloop.before_loop  
async def before_newloop():
  await bot.wait_until_ready()

@bot.event
async def on_guild_join(guild):
    await bot.process_commands(message)
    text_channels = guild.text_channels
    if text_channels:
        channel = text_channels[0]
    await channel.send('Привет, {guild.name}! Для ознакомления с инструкцией ко мне напишите "$help"')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    mate = ["ху", "ёба", "еба", "долб", "оху", "пиз", "пид"]
    answers_mate = ["Мне кажется? Я что вижу неприличные выражения?",
                    "Это кто тут ругается?",
                    "Следите за своим языком!"]
    for i in mate:
        if i in message.content.lower():
            mat = random.randint(0, 2)
            await message.channel.send(answers_mate[mat])
            break
    if "отгадай число" in message.content.lower() or "какое число я загадал" in message.content.lower() and "бот" in message.content.lower():
        await message.channel.send("Какие рамки вашего числа? От какого до какого?")
        await message.channel.send("Напишите: 'Бот от {число} до {число}'")
    if "от" in message.content.lower() and "до" in message.content.lower() and "бот" in message.content.lower():
        str1 = message.content.lower().find("д")
        int1 = random.randint(int(message.content[7:str1 - 1]), int(message.content[str1 + 3:]) - 1) 
        await message.channel.send(int1)
    if "привет" in message.content.lower() and "бот" in message.content.lower():
        await message.channel.send("И тебе привет")
    if message.content.lower() == 'бот':
        await message.channel.send("На месте!")
    if "прощай" in message.content.lower() or "до свидания" in message.content.lower() or "пока" in message.content.lower() and "бот" in message.content.lower():
        await message.channel.send("Буду с нетерпением вас ждать")
    if "рецепт оладий" in message.content.lower() or "приготовить оладьи" in message.content.lower() and "бот" in message.content.lower():
        embed=discord.Embed(title="Рецепт оладий", color=0xFF5733)
        embed.add_field(name="Состав/Ингредиенты:", value="Молоко_____________2 Стакана "
                        "Яйцо_____________1 Штука "
                        "Мука_____________3 Стакана "
                        "Уксус_____________10 Миллилитров "
                        "Соль и сахар_____________По вкусу "
                        "Растительное масло_____________По вкусу "
                        "Количество порций_____________10", inline=False) 
        embed.add_field(name="Шаг 1:", value="Берем два стакана молока и добавляем в него уксус."
                        "Оставляем на 10 минут, после чего молоко прокиснет. Теперь можно вбивать яйцо, взбивать и добавлять все остальные ингредиенты.",
                        inline=False)
        embed.add_field(name="Шаг 2:", value="В последнюю очередь всыпаем муку и доводим массу до однородной консистенции."
                        "Можно воспользоваться миксером, чтобы ускорить процесс. Тесто по густоте должно быть классическое (как на оладьи)."
                        "Если хотите, чтобы оладьи получились как панкейки - сделайте тесто немного реже классического.",
                        inline=False)
        embed.add_field(name="Шаг 3:", value="Жарим на растительном масле с обеих сторон до полного приготовления на среднем огне.",
                        inline=False)
        embed.add_field(name="Завершение:", value="Подаем в горячем виде к чаю, кофе, какао или компоту."
                        "Такие оладьи можно кушать горячими и даже холодными с любым наполнителем (сметаной, джемом и т.п)."
                        "Приятного чаепития!", inline=False) 
        await message.channel.send(embed=embed)
    if "рецепт блинов" in message.content.lower() or "приготовить блины" in message.content.lower() and "бот" in message.content.lower():
        embed=discord.Embed(title="Рецепт блинов", color=0xe74c3c)
        embed.add_field(name="Состав/Ингредиенты:", value="Яйцо куриное_____________2 Штуки "
                        "Молоко_____________500 Миллилитров "
                        "Мука_____________300-400 грамм "
                        "Соль_____________1 щепотка "
                        "Сахар_____________1 Чайная ложка "
                        "Растительное масло_____________2 Столовые ложки "
                        "Количество порций_____________12", inline=False) 
        embed.add_field(name="Шаг 1:", value="В глубокую миску разбейте яйца, добавьте щепотку соли и сахар по вкусу. "
                        "Слегка взбейте ручным венчиком, чтобы яйца стали более-менее однородными.",
                        inline=False)
        embed.add_field(name="Шаг 2:", value="Затем добавьте небольшое количество молока и снова размешайте",
                        inline=False)
        embed.add_field(name="Шаг 3:", value="Всыпьте муку и полностью вмешайте ее в молочно-яичную массу.",
                        inline=False)
        embed.add_field(name="Шаг 4:", value="Теперь добавьте оставшееся молоко "
                        "(можно влить не все сразу, чтобы посмотреть на консистенцию и только потом по необходимости добавить остальное). "
                        "Приготовив тесто моим способом, вы добьетесь полностью однородной консистенции и в тесте не будет ни одного комочка. "
                        "Тесто должно получиться по консистенции похожим на густой кефир, но более вязким. "
                        "Кстати, чтобы не смазывать каждый раз сковороду маслом, масло можно добавить сразу в тесто "
                        "(но если у вас хорошая сковорода с антипригарным покрытием, то масло вам и так не понадобится).",
                        inline=False)
        embed.add_field(name="Шаг 5:", value="Дайте тесту постоять 10-15 минут. "
                        "Затем разогрейте сковороду и смажьте ее небольшим количеством растительного масла "
                        "(только для первого блина, далее этого делать не нужно). Налейте на сковороду полчерпака теста и распределите по дну. "
                        "Выпекайте блинчик около минуты на одной стороне. "
                        "Затем переверните и блин широкой деревянной лопаткой и подержите на горячей сковороде еще полминуты.",
                        inline=False)
        embed.add_field(name="Завершение:", value="Сложите готовые блины стопкой на блюдо или заверните в них начинку. Приятного чаепития!", inline=False) 
        await message.channel.send(embed=embed)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume= 0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url =  ""

    @bot.command()
    async def yt_url(cls, url=None, *, loop=None, stream=False):
        if url == None:
            await cls.send('Вы не дали мне ссылку на видео!')
            return
        loop = loop or asyncio.get_event_loop()
        data = await run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries'in data:
            data = data ['entries'][0]
            filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


@bot.command()
async def dt(ctx):
    current_date = date.today()
    await ctx.send(f"Сегодняшняя дата: {current_date}.")

@bot.command()
async def paswd(ctx):
    pas = "qwe1rty2uio3plk4j5h6gfds7az8x9cvb0nmQWERTYUIOPLKJHGFDSAZXCVBNM"
    a = ''
    for _ in range(8):
        a += pas[randint(0, 61)]
    await ctx.reply(f'{a}')

@bot.command()
async def git(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на git",
        url='https://github.com/Vagim12/project_bot',
    )
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx, member: discord.Member=None, guild: discord.Guild=None):
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

@bot.command()
async def ball(ctx, arg=None):
    response = [
        'Без сомнения.', 
        'Хорошая перспектива.', 
        'Лучше об этом не думать.', 
        'Не могу предсказать сейчас.',
        'Мой ответ - нет.', 
        'Мне кажется это плохая идея.',
    ]
    if arg == None:
        await ctx.send('Вы не задали свой вопрос')
    else:
        await ctx.send(random.choice(response))

@bot.command()
async def gif(msg, *, search=None):
    if search == None:
        await ctx.send('Укажите название гифки!')
        return
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen("https://giphy.com/search/" + query_string)
    search_results = re.findall(query_string[13:], html_content.read().decode())
    await msg.send("https://giphy.com/search/" + search_results[0])    

@bot.command()
async def yt(msg, *, search=None):
    if search == None:
        await ctx.send('Укажите название видео!')
        return
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    await msg.send("http://www.youtube.com/watch?v=" + search_results[0])

@bot.command()
async def обнять(ctx, member: discord.Member = None):
    if member == None:
        return    
    await ctx.channel.send(f"{ctx.author.mention} обнял {member.mention}")

@bot.command()
async def поцеловать(ctx, member: discord.Member = None):
    if member == None:
        return    
    await ctx.channel.send(f"{ctx.author.mention} поцеловал {member.mention}")

@bot.command()
async def пнуть(ctx, member: discord.Member = None):
    if member == None:
        return    
    await ctx.channel.send(f"{ctx.author.mention} пнул {member.mention}")

@bot.command()
async def ударить(ctx, member: discord.Member = None):
    if member == None:
        return    
    await ctx.channel.send(f"{ctx.author.mention} ударил {member.mention}")

@bot.command()
async def prob(ctx, arg=None):
    phrase = ["Я думаю вероятность этого",
              "Вселенная подсказывает, что вероятность этого",
              "Мне кажется, это произойдет с шансом",
              "В моих мыслях всплывает вероятность"]
    if arg == None:
        await ctx.send('Вы не указали для какого случая мине выдать вероятность.')
    else:
        integer = random.randint(0, 100)
        random_index = random.randint(0, len(phrase) - 1)
        await ctx.reply(f'{phrase[random_index]} {integer}%')

@bot.command()
async def YN(ctx, arg=None):
    if arg == None:
        await ctx.send('Вы не задали вопрос, на который я смог бы ответить да или нет.')
    else:
        yes = ["Да", "Нет"]
        no = random.randint(0, 1)
        await ctx.reply(f'{yes[no]}')

@bot.command(name='join')
async def ms(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f"{ctx.message.author.name} не подключен к голосовому каналу")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if ctx.guild.voice_client in bot.voice_clients:
        await voice_client.disconnect()
    else:
        await ctx.send(f"Бот не подключен к голосовому каналу")

@bot.command()
async def wtr(ctx, *, city=None):
    if city == None:
         await ctx.send('Вы забыли указать в каком городе нужен прогноз погоды.')
         return
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Погода в городе {city_name}",
                              color=ctx.message.author.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Описание", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Температура(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Влажность(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Атмосферное давление(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Запрошенный {ctx.author.name}")
        await channel.send(embed=embed)
    else:
        await channel.send("В названии города допущена ошибка, либо такого города не существует")

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

@bot.command()
async def googl(ctx, search_msg=None):
    if search_msg == None:
        await ctx.send('Пожалуйста, скажите, что мне искать!')
    else:
        for url in search(search_msg):
            await ctx.send(url)
            break

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)
    
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member=None, *, reason='Ты не достоин быть здесь'):
    if member == None:
        await ctx.send('Вы не сказали кого мне выгонять.')
    else:
        await ctx.channel.purge(limit=1)
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} больше не будет мешать другим.')

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member=None, *, reason='Вот и все'):
    if member == None:
        await ctx.send('Вы не сказали кого мне банить.')
    else:
        await ctx.channel.purge(limit=1)
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} зашел слишком далеко')

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, id=None):
    if id == None:
        await ctx.send('Вы не указали id забаненного.')
    else:
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f'{user} может быть приглашен обратно!')
        
@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if member == None:
        await ctx.send('Вы не написали кому запрещать говорить.')
    else:
        await member.timeout(datetime.timedelta(hours=1))
        await ctx.send(f'{member.mention} лишается права разговаривать')
    
@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if member == None:
        await ctx.send('Вы не написали кому разрешить говорить вновь.')
    else:
        await member.timeout(datetime.timedelta(hours=0))
        await ctx.send(f'Чудо! {member.mention} снова может разговаривать!')

@bot.command()
@commands.has_permissions(administrator=True)
async def new_channel(ctx, name=None):
    if name == None:
        await ctx.send('Укажите название канала!')
    else:
        guild = ctx.message.guild
        channel = await guild.create_text_channel(name)
        channel1 = bot.get_channel(channel.id)
        await channel1.send('Приветствую в новом канале. Можете общаться!')

@bot.command()
@commands.has_permissions(administrator=True)
async def new_category(ctx, name=None):
    if name == None:
        await ctx.send('Укажите название категории!')
    else:
        guild = ctx.message.guild
        category = await guild.create_category(name)
        await ctx.send('Категория успешно создана!')

@bot.command()
async def tr(ctx, lang, *, thing=None):
    if thing == None:
        await ctx.send('Напишите какое слово мне перевести!')
    else:
        translator = Translator()
        translation = translator.translate(thing, dest=lang)
        await ctx.send(translation.text)

@bot.command()
@commands.has_permissions(administrator=True)
async def new_voice(ctx, name=None):
    if name == None:
        await ctx.send('Вы забыли дать название голосовому каналу!')
    else:
        await ctx.guild.create_voice_channel(name)
        await ctx.send(f'Канал {name} успешно создан. Можете общаться!')

@bot.command()
@commands.has_permissions(administrator=True)
async def add_role(ctx, name, member: discord.Member=None):
    if member == None:
        await ctx.send('Вы не указали у кого отбирать роль!')
    else:
        role = discord.utils.get(ctx.message.guild.roles, name=name)
        if role:
            member = member or ctx.message.author
            await member.add_roles(role)
        else:
            await ctx.send('Я не могу обнаружить такую роль на этом сервере!')

@bot.command()
@commands.has_permissions(administrator=True)
async def re_role(ctx, name, member: discord.Member=None):
    if member == None:
        await ctx.send('Вы не указали у кого отбирать роль!')
    else:
        role = discord.utils.get(ctx.message.guild.roles, name=name)
        if role:
            member = member or ctx.message.author
            await member.remove_roles(role)
        else:
            await ctx.send('Я не могу обнаружить такую роль на этом сервере!')    

@bot.command()
@commands.has_permissions(administrator=True)
async def create_role(ctx, name=None):
    if name == None:
        await ctx.send('Правильно укажите роль!')
    else:
        guild = ctx.guild
        await guild.create_role(name=name)

@bot.command()
@commands.has_permissions(administrator=True)
async def del_role(ctx, *, name=None):
    if name == None:
        await ctx.send('Правильно укажите роль!')
    role = discord.utils.get(ctx.message.guild.roles, name=name)
    if role:
        await role.delete()
    else:
        await ctx.send('Кажется, такой роли на сервере нет.')

@bot.command()
async def rand(ctx):
    await ctx.reply(random.randint(0, 100))

@bot.command()
async def help(ctx):
    BotAvatar = bot.user.avatar
    embed=discord.Embed(title="Инструкция по использованию", color=discord.Colour.red())
    embed.set_thumbnail(url=f'{BotAvatar}')
    embed.add_field(name="Работа с контекстом:", value="Вы можете поздороваться с ботом, попращаться с ним. "
                    "Попробовать попросить его отгадать загаданное вами число. "
                    "Бот распознает в сообщениях некоторые нецензурные выражения, будьте поосторожнее с этим! "
                    "Попробуйте узнать у бота рецепты оладий и блинов). "
                    "На все это он будет отвечать, если правильно напишите сообщение и обязательно укажите в сообщение слово <бот>. "
                    "Основное управление осуществялется посредством команд.", inline=False)
    embed1=discord.Embed(title="", color=discord.Colour.red())
    embed1.add_field(name="Команды, используемые и на серверах и в личной переписке с ботом:", value="$wtr ['Название города'] - бот расскажет о погоде в этом городе.\n"
                    "$googl ['Ваш запрос'] - бот выведет ссылку из гугла по вашему запросу. "
                    "Не используйте слишком часто данную команду за маленький промежуток времени,"
                    " т.к. гугл против слишком частого запрашивание url, он распознает это как спам!\n"
                    "$tr ['Язык, на который нужно перевести, в формате <en>, <ru>, <af> и т.д.'] ['Слово, которое нужно перевести, на любом языке'] "
                    "- бот переведет ваше слово на указанный вами язык.\n"
                    "$rand - бот выдаст рандомное число от 0 до 100.\n"
                    "$пинг - бот скажет ваш пинг.\n"
                    "НЕ НУЖНО УКАЗЫВАТЬ КВАДРАТНЫЕ СКОБКИ И КАВЫЧКИ ДЛЯ КОМАНД, ЭТО ДЛЯ ПРОСТОТЫ ВОСПРИЯТИЯ!\n"
                    "Пример: $prob что я упаду со стула",
                    inline=False)
    embed2=discord.Embed(title="", color=discord.Colour.red())
    embed2.add_field(name="Команды, используемые и на серверах и в личной переписке с ботом2:", value="$yt_url ['Ссылка на видео с ютуб'] - бот загружает видео по ссылке и выводит в чате.\n"
                    "$dt - бот пишет дату сегодняшнего дня.\n"
                    "$paswd - бот генерирует для вас пароль из 8 символов.\n"
                    "$git - бот дает ссылку на github, а точнее на git-репозиторий, где вы можете увидеть код нашего бота и узнать как он работает.\n"
                    "$ball ['Ваш вопрос/действие'] - бот расскажет свое отношение к этому.\n"
                    "$gif ['Предмет, про который вы хотите найти гифку(лучше писать на английском языке)'] - бот найдет для вас гифку. "
                    "Если бот ничего не выводит значит, что гифки по такой тематике нет, а если даст просто ссылку на сайт, "
                    "то на сайте нет таких гифок.\n"
                    "$yt ['Название видео(одно слово)'] - выдаст ссылку на видео, выданное ютубом по вашему запросу.\n"
                    "$prob ['Случай/событие'] - бот скажет с каким шансом произойдет данное событие.\n"
                    "$YN ['Вопрос'] - бот ответит да или нет, на поставленный вами вопрос.\n",
                    inline=False)
    embed3=discord.Embed(title="", color=discord.Colour.red())
    embed3.add_field(name="Команды для сервера:", value="Примечание: все предыдущие команды на сервере тоже можно использовать.", inline=False)
    embed3.add_field(name="Для всех участников:", value="$info ['@Участник сервера'] - выводит информацию о данном пользователе.\n"
                    "$обнять ['@Участник сервера'] - вы обнимете этого человека.\n"
                    "$поцеловать ['@Участник сервера'] - вы поцелуете этого человека.\n"
                    "$пнуть ['@Участник сервера'] - вы пнёте этого человека.\n"
                    "$ударить ['@Участник сервера'] - вы ударите этого человека.\n"
                    "$join - бот подключиться к голосовому каналу, если вы там есть.\n"
                    "$leave - бот покинет голосовой канал, если он там находился.\n"
                    "$ser_info - выдаёт информацию о сервере.\n"
                    "Пример: $пнуть @Шарик",
                    inline=False)
    embed4=discord.Embed(title="", color=discord.Colour.red())
    embed4.add_field(name="Для администраторов сервера:", value="$new_category ['Название'] - бот создает новую категорию с данным вами названием, где вы можете создавать каналы.\n"
                    "$new_voice ['Название'] - бот создает новый голосовой канал с вашим названием.\n"
                    "$create_role ['Имя роли'] - бот создаст роль с этим именем, которую можно будет настроить в настройках сервера.\n"
                    "$add_role ['Имя роли'] ['@Участник сервера'] - бот даст этому участнику данную роль, но роль должна быть создана!\n"
                    "$re_role ['Имя роли'] ['@Участник сервера'] - бот заберёт у этого участника данную роль, которая должна быть создана и должна быть у этого участника!\n"
                    "$del_role ['Имя роли'] - бот удалит с этого сервера роль с таким именем, роль должна быть создана!\n"
                    "Пример: $add_role Бот @Шарик",
                    inline=False)
    embed5=discord.Embed(title="", color=discord.Colour.red())
    embed5.add_field(name="Для администраторов сервера2:", value="$clear ['Количество сообщений(если не укжите число, то удалятся последние 100 сообщений'] - бот очищает чат.\n"
                    "$kick ['@Участник сервера'] - бот удаляет этого пользователя с сервера.\n"
                    "$ban ['@Участник сервера'] - бот добавляет этого человека в список забаненых и удаляет с сервера.\n"
                    "$unban ['id забаненного пользователя'] - бот убирает пользователя из списка забаненых и его можно будет заново пригласить на этот сервер.\n"
                    "$mute ['@Участник сервера'] - бот отправляет этого человека в тайм-аут, он не сможет писать и разговаривать в голосовом канале на протяжении одного часа.\n"
                    "$unmute ['@Участник сервера'] - бот убирает тайм-аут у этого человека.\n"
                    "$new_channel ['Название'] - бот создает новый текстовый канал с этим именем.\n",
                    inline=False)
    embed6=discord.Embed(title="", color=discord.Colour.red())
    embed6.add_field(name="Заключение:", value="Рекомендуйте этого бота друзьям, вот его id - 910178913169322045. "
                    "С помощью него добавьте бота на свой сервер, дайте ему все нужные разрешения(я рекомендую дать все для корректной работы, а особенно сделать бота администратором.\n"
                    "Если вы столкнулись с какими-то проблемами, то напишите нам в телеграме - t.me/Vagym.\n"
                    "Поддержите нас - https://new.donatepay.ru/@Vagym_ds_bot.\n"
                    "Приятного использования!",
                    inline=False)
    await ctx.channel.send(embed=embed)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)
    await ctx.channel.send(embed=embed3)
    await ctx.channel.send(embed=embed4)
    await ctx.channel.send(embed=embed5)
    await ctx.channel.send(embed=embed6)  

@bot.command(name="пинг")
async def ping(ctx):
    start = time.perf_counter()
    msg = await ctx.send("Пинг..")
    end = time.perf_counter()
    duration = (end - start) * 1000
    duration = round(duration, 0)
    await ctx.send(f"Понг! {duration}ms")

@tr.error
async def cmd_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Вы неправильно указали язык!")

bot.run(config['token'])
