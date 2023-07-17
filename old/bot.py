import discord

class MyClient(discord.Client):
    async def setup_hook(self):
        print('This is asynchronous!')

@MyClient.event
async def on_connect(client):
    print('connected')


@MyClient.event
async def on_ready(client):
    print('Ready!')


@MyClient.event
async def on_error(client, event):
    print(f'ERROR: {str(event)}')