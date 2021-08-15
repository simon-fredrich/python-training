import discord
import python_weather
import wikipedia
import os
from bs4 import BeautifulSoup
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("info"):
        if (message.channel.id == 778335092812021802) or (message.channel.id == 801470078579245056):
            query = message.content[5:]
            wikipedia.set_lang("de")
            await message.channel.send(wikipedia.summary(query))
            print(query)

    if message.content.startswith("wetter"):
        if (message.channel.id == 778335092812021802) or (message.channel.id == 801470078579245056):
            query = message.content[7:]
            wclient = python_weather.Client(format=python_weather.METRIC)
            weather = await wclient.find(query)
            await message.channel.send("In " + query.capitalize() + " sind es " + str(weather.current.temperature) + " Grad.")
            await wclient.close()

    if message.content.startswith("frage"):
        if (message.channel.id == 778335092812021802) or (message.channel.id == 801470078579245056):
            query = str(message.content[7:])
            query = query.replace(" ", "+")
            headers = {
                'User-agent':
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
            }

            html = requests.get('https://www.google.com/search?q='+query, headers=headers).text
            soup = BeautifulSoup(html, 'html.parser')

            snippet = soup.find("span", class_="hgKElc")
            if snippet != None:
                await message.channel.send(snippet.text)
            else:
                await message.channel.send("Dazu nehme ich keine Stellung...")
          
            
client.run(os.getenv("BOT_1_TOKEN"))