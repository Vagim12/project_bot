import discord
import logging
import random

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
TOKEN = ""

class YLBotClient(discord.Client):
    async def on_message(self, message):
        mate = ["ху", "ёб", "еб", "долб", "оху", "пи"]
        if message.author == self.user:
            return
        for i in mate:
            if i in message.content.lower():
                await message.channel.send("Мне кажется? Я что вижу неприличные выражения?")    
        if "отгадай число" in message.content.lower() or "какое число я загадал" in message.content.lower() and "бот" in message.content.lower():
            await message.channel.send("Какие рамки вашего числа? От какого до какого?")
            await message.channel.send("Напишите: 'Бот от {число} до {число}'")
        if "от" in message.content.lower() and "до" in message.content.lower() and "бот" in message.content.lower():
            str1 = message.content.lower().find("д")
            int1 = random.randint(int(message.content[7:str1 - 1]), int(message.content[str1 + 3:]) - 1) 
            await message.channel.send(int1)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
        
        





