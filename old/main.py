import os
import discord
import asyncio
import bot.events


TOKEN = "MTA5ODY2MTA0ODU4NTgzNDcxNg.GV2Ssk.jq_pgeCbKYpq1twF7ttT7Zq2LZPuWS3lCrlR7A"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_connect():
    print('connected')


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_error(event, *args, **kwargs):
    print(f'ERROR: {str(event)}')


async def main():
    # do other async things
    #await my_async_function()
    print("starting")
    
    # start the client
    async with client:
        await client.start(TOKEN)


asyncio.run(main())