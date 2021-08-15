import discord
import python_weather
import wikipedia
import os

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
            await message.channel.send(wikipedia.summary(query, sentences=3))
            print(query)

    if message.content.startswith("wetter"):
        if (message.channel.id == 778335092812021802) or (message.channel.id == 801470078579245056):
            query = message.content[7:]
            wclient = python_weather.Client(format=python_weather.METRIC)
            weather = await wclient.find(query)
            await message.channel.send("In " + query.capitalize() + " sind es " + str(weather.current.temperature) + " Grad.")
            await wclient.close()
            
client.run(os.getenv("BOT_1_TOKEN"))