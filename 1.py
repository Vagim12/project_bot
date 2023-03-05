import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
TOKEN = ""


class YLBotClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        if "привет" in message.content.lower() and "бот" in message.content.lower():
            await message.channel.send("И тебе привет")
        if message.content.lower() == 'бот':
            await message.channel.send("На месте!")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
        
        





