from twitchio.ext import commands
import twitchio
import requests
import json
import random
from deep_translator import GoogleTranslator
from transliterate import translit
import csv
import pandas as pd
import datetime
import time
import urllib
import re
from datetime import date

HEADERS = { #Это нужно для API OpenAI, он оказался платным, вроде бы через одну библиотеку он бесплатный, потом попробую
    'Authorization': 'Bearer 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', 
    'Content-Type': 'application/json'
}
weather_api_key = '62974faf81d841e3833101541232104'

banlist = ['TheRennaisance', 'Remoornie']
afk_list = []


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token="oauth:8633bmzy890o7alhrt6fvm1tvq45jx", #возможно токен деактивируется, из-за попадания в открый доступ
            prefix="$", #Префикс потом заменю на более удобный в использовании 
            initial_channels=["striginae", "alexproduct"],
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"123")

    @commands.command()
    async def random_emote(self, ctx: commands.Context): #вроде бы не работает, у них проблемы с апи
        response = requests.get(
            f"https://7tv.io/v3/emote-sets", params=ctx.channel.name
        ).text
        n = json.loads(response)
        await ctx.send(f"{n['emotes'][random.randint(0, len(n['emotes'])-1)]['name']}")

    @commands.command()
    async def random(self, ctx: commands.Context):
        n = random.randint(0, 100)
        if n == 69:
            await ctx.send('69! Nice')
        else:
            await ctx.send(str(n))

    @commands.command()
    async def prediction_ball(self, ctx: commands.Context):
        answers = ['😃 Несомненно', '😃 Это определенно так', '😃 Без сомнения', '😃 Да - определенно', '😃 Вы можете положиться на это', '😃 Насколько я понимаю, да', '😃 Скорее всего', '😃 Перспективы хорошие', '😃 Да', '😃 Знаки указывают на "да"', '😐 Ответ туманный, попробуйте еще раз.', '😐 Спросите еще раз позже', '😐 Лучше не говорить тебе сейчас.', '😐 Сейчас не могу предсказать', '😐 Сконцентрируйтесь и спросите еще раз.', '😦 Не рассчитывайте на это', '😦 Мой ответ - нет.', '😦 Мои источники говорят, что нет.', '😦 Перспективы не очень хорошие.', '😦 Очень сомнительно']
        await ctx.send(random.choice(answers))

    @commands.command()
    async def coin_flip(self, ctx: commands.Context):
        answers = ['Орел', 'Решка']
        await ctx.send(random.choice(answers))

    @commands.command()
    async def fill(self, ctx: commands.Context, *args):
        answer = []
        while len(' '.join(answer)) <= 500:
            answer.append(random.choice(args))
        while len(' '.join(answer)) >= 500:
            answer.pop(-1)
        await ctx.send(' '.join(answer))

    @commands.command()
    async def rmeal(self, ctx: commands.Context, arg='get'):
        response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php').text
        n = json.loads(response)
        print(n)
        if arg == 'get':
            global old_n
            old_n = n.copy()
            ans = f"{n['meals'][0]['strMeal']}. Ingredients: "
            for i in range(1, 21):
                if n['meals'][0][f'strIngredient{i}'] != '' and n['meals'][0][f'strIngredient{i}'] != None:
                    ans += n['meals'][0][f'strIngredient{i}']
                    ans += ', '
            await ctx.send(GoogleTranslator(source='auto', target='ru').translate(ans.rstrip(', ')))
        elif arg == 'recipe':
            for i in old_n['meals'][0][f'strInstructions'].split('\r\n'):
                await ctx.send(GoogleTranslator(source='auto', target='ru').translate(i))
        elif arg == 'video':
            await ctx.send(old_n['meals'][0][f'strYoutube'])
            

    @commands.command()
    async def transliterate(self, ctx: commands.Context, *args):
        await ctx.send(translit(' '.join(args), reversed=True))

    @commands.command()
    async def translate(self, ctx: commands.Context, language, *args):
        args = list(args)
        for i in range(len(args)):
            args[i] = GoogleTranslator(source='auto', target=language).translate(args[i])
        await ctx.send(' '.join(args))

    async def event_message(self, message):
        ctx = commands.Context(message, self.__init__)
        with open("afks.json", "r", encoding="utf-8") as f:
                text = json.load(f)
        if message.content.startswith('Striginea'):
            if ' или ' in message.content:
                res = list(message.content.split(' или '))
                await ctx.send(random.choice(res).strip('Striginea').strip('?'))
        elif message.author.name in text[1]:
            flag = False
            for i in text[0]:
                if i['nickname_twitch'] == ctx.author.name:
                    res_message = i['afk_message']
                    i['afk_status'] = False
                    i['afk_message'] = ''
                    i['afk_type'] = ''
                    try:
                        text[1].pop(text[1].index(i['nickname_discord']))
                    except:
                        pass
                    break
            text[1].pop(text[1].index(ctx.author.name))
            await ctx.send(f'{ctx.author.display_name} вернулся: {res_message}')
            with open("afks.json", "w") as f:
                json.dump(text, f)
        else:
            await self.handle_commands(message) 

    @commands.command()
    async def afk(self, ctx: commands.Context, *afk_message):
        with open("afks.json", "r", encoding="utf-8") as f:
            text = json.load(f)
        flag = False
        for i in text[0]:
            if i['nickname_twitch'] == ctx.author.name:
                i['afk_status'] = True
                i['afk_message'] = ' '.join(afk_message)
                i['afk_type'] = 'afk'
                if i['platform_connected'] == False:
 #                   await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
                    pass
                else:
                    text[1].append(i['nickname_discord'])
                flag = True
                break
        if not flag:
            text[0].append({'nickname_twitch': ctx.author.name, 'nickname_discord': '', 'afk_type': 'afk', 'afk_status': True, 'afk_message': ' '.join(afk_message), 'platform_connected': False})
 #           await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
        text[1].append(ctx.author.name)
        await ctx.send(f'{ctx.author.display_name} отошел от устройства: {" ".join(afk_message)}')
        with open("afks.json", "w") as f:
            json.dump(text, f)

    @commands.command()
    async def Fridge(self, ctx: commands.Context):
       await ctx.send('ВОРУЮ ИЗ ТВОЕГО Fridge')
       time.sleep(10)
       await ctx.send('УКРАЛ SOLE ИЗ ТВОЕГО Fridge')


    @commands.command()
    async def weather(self, ctx: commands.Context, location):
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json", params={'key': weather_api_key, 'q': location}
        ).text
        n = json.loads(response)
        await ctx.send(GoogleTranslator(source='auto', target='ru').translate(f"{n['location']['country']}, {n['location']['region']}, {n['location']['name']}: Temperature {n['current']['temp_c']} C°, feels like {n['current']['feelslike_c']} C°, {n['current']['condition']['text']}, wind speed {n['current']['wind_kph']} kmph. 🌤 "))

    #@commands.command()
    #async def air(self, ctx: commands.Context, location):
    #    response = requests.get(
    #        f"http://api.weatherapi.com/v1/current.json", params={'key': weather_api_key, 'q': location, 'aqi': True}
    #    ).text
    #    n = json.loads(response)
    #    print(n)
    #    await ctx.send(GoogleTranslator(source='auto', target='ru').translate(f"{n['location']['country']}, {n['location']['region']}, {n['location']['name']}: Качество воздуха {n['current']['aqi']}"))

    @commands.command()
    async def gn(self, ctx: commands.Context, *afk_message):
        with open("afks.json", "r", encoding="utf-8") as f:
            text = json.load(f)
        flag = False
        for i in text[0]:
            if i['nickname_twitch'] == ctx.author.name:
                i['afk_status'] = True
                i['afk_message'] = ' '.join(afk_message)
                i['afk_type'] = 'sleep'
                if i['platform_connected'] == False:
  #                   await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
                    pass
                else:
                    text[1].append(i['nickname_discord'])
                flag = True
                break
        if not flag:
            text[0].append({'nickname_twitch': ctx.author.name, 'nickname_discord': '', 'afk_type': 'afk_status', 'afk_status': True, 'afk_message': ' '.join(afk_message), 'platform_connected': False})
#            await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
        text[1].append(ctx.author.name)
        await ctx.send(f'{ctx.author.display_name} ушел спать: {" ".join(afk_message)}')
        with open("afks.json", "w") as f:
            json.dump(text, f)

    @commands.command()
    async def nap(self, ctx: commands.Context, *afk_message):
        with open("afks.json", "r", encoding="utf-8") as f:
            text = json.load(f)
        flag = False
        for i in text[0]:
            if i['nickname_twitch'] == ctx.author.name:
                i['afk_status'] = True
                i['afk_message'] = ' '.join(afk_message)
                i['afk_type'] = 'nap'
                if i['platform_connected'] == False:
 #                   await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
                    pass
                else:
                    text[1].append(i['nickname_discord'])
                flag = True
                break
        if not flag:
            text[0].append({'nickname_twitch': ctx.author.name, 'nickname_discord': '', 'afk_type': 'afk_status', 'afk_status': True, 'afk_message': ' '.join(afk_message), 'platform_connected': False})
#            await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
        text[1].append(ctx.author.name)
        await ctx.send(f'{ctx.author.display_name} прилег передохнуть: {" ".join(afk_message)}')
        with open("afks.json", "w") as f:
            json.dump(text, f)
    
    @commands.command()
    async def study(self, ctx: commands.Context, *afk_message):
        with open("afks.json", "r", encoding="utf-8") as f:
            text = json.load(f)
        flag = False
        for i in text[0]:
            if i['nickname_twitch'] == ctx.author.name:
                i['afk_status'] = True
                i['afk_message'] = ' '.join(afk_message)
                i['afk_type'] = 'study'
                if i['platform_connected'] == False:
#                    await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
                    pass
                else:
                    text[1].append(i['nickname_discord'])
                flag = True
                break
        if not flag:
            text[0].append({'nickname_twitch': ctx.author.name, 'nickname_discord': '', 'afk_type': 'afk_status', 'afk_status': True, 'afk_message': ' '.join(afk_message), 'platform_connected': False})
#            await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
        text[1].append(ctx.author.name)
        await ctx.send(f'{ctx.author.display_name} занялся учебой: {" ".join(afk_message)}')
        with open("afks.json", "w") as f:
            json.dump(text, f)
    
    @commands.command()
    async def work(self, ctx: commands.Context, *afk_message):
        with open("afks.json", "r", encoding="utf-8") as f:
            text = json.load(f)
        flag = False
        for i in text[0]:
            if i['nickname_twitch'] == ctx.author.name:
                i['afk_status'] = True
                i['afk_message'] = ' '.join(afk_message)
                i['afk_type'] = 'work'
                if i['platform_connected'] == False:
#                    await ctx.send(f'{ctx.author.display_name} , похоже у вас не подключен дискорд аккаунт. Если вы хотите подключить его, введите $connect ник, либо введите $connect not в противном случае')
                    pass
                else:
                    text[1].append(i['nickname_discord'])
                flag = True
                break
        if not flag:
            text[0].append({'nickname_twitch': ctx.author.name, 'nickname_discord': '', 'afk_type': 'afk_status', 'afk_status': True, 'afk_message': ' '.join(afk_message), 'platform_connected': False})
        text[1].append(ctx.author.name)
        await ctx.send(f'{ctx.author.display_name} ушел работать: {" ".join(afk_message)}')
        with open("afks.json", "w") as f:
            json.dump(text, f)

    @commands.command()
    async def yt(self, ctx: commands.Context, *keywords):
        query_string = urllib.parse.urlencode({"search_query": ' '.join(keywords)})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        await ctx.send("http://www.youtube.com/watch?v=" + search_results[0])

    @commands.command()
    async def dt(self, ctx: commands.Context):
        current_date = date.today()
        await ctx.send(f"Сегодняшняя дата: {current_date}.")

    @commands.command()
    async def funfact(self, ctx: commands.Context):
        year = random.randint(2017, 2021)
        month = random.randint(1, 12)
        n = requests.get("https://uselessfacts.net/api/posts", params={'d': (year, month)}).json()
        await ctx.send(GoogleTranslator(source='auto', target='ru').translate(n[random.randint(0, len(n) - 1)]['title']))

    @commands.command()
    async def connecty(self, ctx: commands.Context, nickname):
        with open("afks.json", "r", encoding="utf-8") as f:
            text = json.load(f)
        flag = False
        for i in text[0]:
            if i['nickname_twitch'] == ctx.author.name:
                if nickname == 'not':
                    i['platform_connected'] = True
                else:
                    i['platform_connected'] = True
                    i['nickname_discord'] = nickname
        if not flag:
            if nickname == 'not':
                text[0].append({'nickname_twitch': ctx.author.name, 'nickname_discord': '', 'afk_type': 'afk_status', 'afk_status': True, 'afk_message': '', 'platform_connected': True})
            else:
                text[0].append({'nickname_twitch': ctx.author.name, 'nickname_discord': nickname, 'afk_type': 'afk_status', 'afk_status': True, 'afk_message': '', 'platform_connected': True})
        with open("afks.json", "w") as f:
            json.dump(text, f)

    @commands.command()
    async def hug(self, ctx: commands.Context, target):
        await ctx.send(f'{ctx.author.display_name} , вы обняли {target}')

    @commands.command()
    async def tuck(self, ctx: commands.Context, target):
        await ctx.send(f'{ctx.author.display_name} , вы уложили спать {target}')

        
        


    
    

bot = Bot()
bot.run()
