from twitchio.ext import commands
import twitchio
import requests
import json
import random
from deep_translator import GoogleTranslator
from transliterate import translit
import sqlite3

HEADERS = { #Это нужно для API OpenAI, он оказался платным, вроде бы через одну библиотеку он бесплатный, потом попробую
    'Authorization': 'Bearer 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', 
    'Content-Type': 'application/json'
}



class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token="oauth:aq7iawwx0p8bys0vvn7vydviluo50h", #возможно токен деактивируется, из-за попадания в открый доступ
            prefix="₽", #Префикс потом заменю на более удобный в использовании
            initial_channels=["striginae", "alexproduct"],
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Я родился")

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
        answer.pop(-1)
        await ctx.send(' '.join(answer))

    @commands.command()
    async def rmeal(self, ctx: commands.Context, arg='get'):
        response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php').text
        n = json.loads(response)
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




bot = Bot()
bot.run()


#Просто несколько комманд, как пример. Нет только примеров работы с дб, но это позже
#Не могу показать на занятии, нет доступа к микрофону
#Еще меня не будет с понедельника по пятницу, улетаю на финал НТО
