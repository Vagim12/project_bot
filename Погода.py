import discord
from discord.ext import commands,tasks
import requests
import json

config = {
    'token': '',
    'prefix': '$',}
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)
api_key = "На сайте генерируется личный API-ключ"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
@bot.command()
async def wtr(ctx, *, city: str):
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
        await channel.send("В названии города допущена ошибка, либо такого города не существует.")

bot.run(config['token'])






