import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
TOKEN = "OTEwMTc4OTEzMTY5MzIyMDQ1.GguIrK.mpVtP0c-k0kiBWGRLTvRiZ63R3S3jd8ej2l8u4"


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.quilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f"Привет, {member.name}!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "привет" in message.content.lower():
            await message.channel.send("И тебе привет")
        else:
            await message.channel.send("Спасибо за сообщение")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
        
        





