from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
import discord, time



def create_bot_embed(ctx, bot, color_embed, title=""):

    embed = discord.Embed(title=title, color=color_embed)
    embed.set_thumbnail(url = bot.user.avatar.url)
    #embed.set_author(name=str(ctx.author.name))
    
    footer = f'{ctx.author.name} - {time.strftime("%H:%M")}' 
    embed.set_footer(text=footer, icon_url=ctx.author.avatar.url)
    return embed