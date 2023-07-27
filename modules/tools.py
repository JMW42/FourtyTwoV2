

from discord.ext import commands
from yaml.loader import SafeLoader
from discord.ext import commands, tasks
#from discord.ext.commands import Bot, Context

import yaml, discord, asyncio, os, time

def create_bot_embed(ctx, bot, color_embed, title=""):

    embed = discord.Embed(title=title, color=color_embed)
    embed.set_thumbnail(url = bot.user.avatar.url)
    #embed.set_author(name=str(ctx.author.name))
    
    footer = f'{ctx.author.name} - {time.strftime("%H:%M")}' 
    embed.set_footer(text=footer, icon_url=ctx.author.avatar.url)
    return embed




def process_config_file_dict(file_dict):
    res = {}
    for key in file_dict:
        if str(file_dict[key]).startswith("file:"):
            f = str(file_dict[key]).replace("file:", "")
            res[key] = load_config_file(f)[key]
        else:
            res[key] = file_dict[key]

    return res


def load_config_file(filepath) -> dict:
    with open(filepath, "r") as stream:
        res = None
        try:
            d = yaml.safe_load(stream)
            res = process_config_file_dict(d)
        except yaml.YAMLError as E:
            print(E)
        
        return res