import discord
from discord.ext import tasks, commands
import os
from keep_alive import keep_alive
import logging

#coin
from embed import get_embed

client = discord.Client()
logging.basicConfig(level=logging.INFO)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    if not send.is_running():
        send.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('coins'):
        print('from message')
        _embed = get_embed()
        await message.channel.send(embed=_embed)


@tasks.loop(hours=1)
async def send():
    print('from loop')
    embed = get_embed()
    channel = client.get_channel(882212176243359784)
    await channel.send(embed=embed)


@send.before_loop
async def before():
    await client.wait_until_ready()


keep_alive()
client.run(os.getenv('TOKEN'))
