import os,asyncio
import discord

import requests
from io import BytesIO
from PIL import Image

intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('We have logged in as {0.user}'.format(bot))
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_member_join(member):
        response = requests.get(member.avatar_url)
        asyncio.sleep(1)
        icon=Image.open(BytesIO(response.content))
        images = [Image.open("image.gif"),icon,icon,icon,icon,icon,icon,icon]
        gif = []
        for image in images:
                gif.append(image)
        gif[0].save('welcome.gif',save_all=True,optimize=False, append_images=gif[1:], loop=0)
        channel = discord.utils.get(member.guild.channels, name='welcome')
        await channel.send(file=discord.File('./welcome.gif'))
bot.run(token)
