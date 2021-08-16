import discord
import python_weather
import wikipedia
import os
from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(",info"):
        if message.channel.id in (778335092812021802, 801470078579245056):
            query = message.content[5:]
            wikipedia.set_lang("de")
            await message.channel.send(wikipedia.summary(query))
            print(query)

    if message.content.startswith(",wetter"):
        if message.channel.id in (778335092812021802, 801470078579245056):
            query = message.content[7:]
            wclient = python_weather.Client(format=python_weather.METRIC)
            weather = await wclient.find(query)
            await message.channel.send("In " + query.capitalize() + " sind es " + str(weather.current.temperature) + " Grad.")
            await wclient.close()

    if message.content.startswith(",frage"):
        if message.channel.id in (778335092812021802, 801470078579245056):
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
                # Ausgabe des Google-Snippets
                await message.channel.send(snippet.text)
            else:
                # Wenn kein Snippet verfügbar ist wird ein Chuck Norris Witz gekloppt.
                response = requests.get("https://api.chucknorris.io/jokes/random").json()
                quote = response["value"]
                german_quote = GoogleTranslator(source='en', target='de').translate(quote)
                await message.channel.send("Keine Ahnung, aber: "+german_quote)
          
    if message.content == ",trampel":
        if message.channel.id == 801470078579245056:
            response = requests.get("https://api.tronalddump.io/random/quote").json()
            quote = response["value"]
            await message.channel.send("Wie Tronald Dump sagen würde: "+quote)

    if message.content == ",cn":
        if message.channel.id in (801470078579245056, 800788397065109566):
            # channels: Commands, Mainchat
            response = requests.get("https://api.chucknorris.io/jokes/random").json()
            quote = response["value"]
            german_quote = GoogleTranslator(source='en', target='de').translate(quote)
            await message.channel.send(german_quote)
    
client.run(os.getenv("BOT_1_TOKEN"))