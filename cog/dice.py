from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
import module.tools as tools
import discord, time, os, random




class Dice(commands.Cog):
    def __init__(self, bot) -> None:
        #super().__init__()
        self.bot:Bot = bot
        self.color_embed:discord.Colour = discord.Colour.light_embed()
        print("initializing cog: Dice")



    @commands.command(name="W")
    async def dice_roll(self, ctx, dice:int=6):
        await ctx.send(f'W{dice} --> {random.randint(0, dice)}')


    
    @commands.command(name="randint")
    async def randint(self, ctx, start:int=0, stop:int=10):
        await ctx.send(f'randint: [{start}, {stop}] --> {random.randint(start, stop)}')
    

    
    @commands.command(name="randfloat")
    async def randfloat(self, ctx, start:float=0, stop:float=10):
        roll = random.random(start, stop)
        rand = start + (stop-start)*roll
        await ctx.send(f'randint: [{start}, {stop}[ --> {rand}')



async def setup(bot):
    print("loading extension: bot")
    await bot.add_cog(Dice(bot))