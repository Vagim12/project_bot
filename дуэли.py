import discord
from discord.ext import commands
import random
import time

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def дуэль(ctx, member: discord.Member=None):
    if member == None:
        await ctx.send("Вы не указали, кого вызываете ни битву!")
        return
    if ctx.author.id == member.id:
        await ctx.send("Если хотите убить самого себя, то для вас есть рулетка.")
        return
    if str(member.id) == "910178913169322045":
        await ctx.send("Бота не трогайте, я не виновен.")
        return
    await ctx.send(f'Все сюда! {ctx.author} вызвал на дуэль {member}!')
    await ctx.send(f"{member}, Вы согласны? (Да или нет)")
    command = bot.get_command('дуэль')
    command.update(enabled=False)
    t = time.time()
    while True:
        t1 = time.time() - t
        if t1 > 60:
            await ctx.send(f"{member} не принял поединок. Время истекло.")
            command.update(enabled=True)
            return
        message = await bot.wait_for('message')
        if message.author.id == member.id:
            if message.content.lower() == "да":
                break
            elif message.content.lower() == "нет":
                await ctx.send(f"{member} отказался от поединка. Позор ему!")
                command.update(enabled=True)
                return
            else:
                await ctx.send(f"{member} ответил что-то невнятное, возможно он не в состоянии сейчас сражаться. Все идите домой.")
                command.update(enabled=True)
                return
    await ctx.send("Преимущество на стороне того, кто выстрелит первым, написав <пиу> или <пау> или <выстрел> или <огонь>")
    await ctx.send("При промахе, дуэль продолжается. Одному участнику несколько раз подряд стрелять нельзя.")
    await ctx.send("Даю время подготовиться, после этого начнется отсчет. По его окончанию - стреляйте!")
    time.sleep(10)
    await ctx.send("Стреляем через:")
    await ctx.send("5")
    time.sleep(1)
    await ctx.send("4")
    time.sleep(1)
    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    time.sleep(1)
    await ctx.send("Пли!")
    m1 = 0
    m2 = 0
    n = 1
    while True:
        message = await bot.wait_for('message')
        faer = ["пиу", "выстрел", "огонь", "пау"]
        if message.author.id != ctx.author.id and message.author.id != member.id:
            continue    
        if message.content.lower() in faer and n == 1 and message.author.id == ctx.author.id or message.author.id == member.id and message.content.lower() in faer and n == 1:
            vs = message.author.id
        if message.author.id == vs and n > 1 and message.content.lower() in faer:
            await ctx.send(f"{message.author}, не ваша очередь стрелять!")
            continue
        elif message.author.id != vs and n > 1:
            vs = message.author.id
        if message.content.lower() == "пиу" or message.content.lower() == "пау" or message.content.lower() == "выстрел" or message.content.lower() == "огонь":
            duet = [1, 2, 3, 4, 5]
            ran = [1, 2, 3, 4, 5, 6]
            if message.author.id == ctx.author.id and m1 > 0 or message.author.id == member.id and m2 > 0:
                if random.randint(0, len(ran) - 1) == 1:
                    await ctx.send(f"{message.author} убивает противника!")
                    await ctx.send(f"Дуэли конец!")
                    command.update(enabled=True)
                    return
                elif random.randint(0, len(ran) - 1) == 2 or random.randint(0, len(ran) - 1) == 3 or random.randint(0, len(ran) - 1) == 4:
                    await ctx.send(f"{message.author} не попадает!")
                else:
                    await ctx.send(f"{message.author} попал и ранил оппонента, у него перевес в шансах!")
                    if message.author.id == ctx.author.id:
                        m2 += 1
                    else:
                        m1 += 1
                    if m1 == 3:
                        await ctx.send(f"{ctx.author} скончался от полученных ран. {member} победил!")
                        command.update(enabled=True)
                        return
                    elif m2 == 3:
                        await ctx.send(f"{member} скончался от полученных ран. {ctx.author} празднует победу!")
                        command.update(enabled=True)
                        return
            else:
                if random.randint(0, len(duet) - 1) == 1:
                    await ctx.send(f"{message.author} убивает противника!")
                    await ctx.send(f"Дуэли конец!")
                    command.update(enabled=True)
                    return
                elif random.randint(0, len(duet) - 1) == 2 or random.randint(0, len(duet) - 1) == 3:
                    await ctx.send(f"{message.author} не попадает!")
                else:
                    await ctx.send(f"{message.author} попал и ранил оппонента, у него перевес в шансах!")
                    if message.author.id == ctx.author.id:
                        m2 += 1
                    else:
                        m1 += 1
                    if m1 == 3:
                        await ctx.send(f"{ctx.author} скончался от полученных ран. {member} победил!")
                        command.update(enabled=True)
                        return
                    elif m2 == 3:
                        await ctx.send(f"{member} скончался от полученных ран. {ctx.author} празднует победу!")
                        command.update(enabled=True)
                        return
        n += 1
    
bot.run(config['token'])






