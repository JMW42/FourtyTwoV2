from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
import module.tools as tools
import discord, time, os




class BotAdministration(commands.Cog):
    def __init__(self, bot) -> None:
        #super().__init__()
        self.bot:Bot = bot
        self.color_embed:discord.Colour = discord.Colour.light_embed()
        print("initializing cog: BotAdministration")



    @commands.group(invoke_without_command=True)
    async def extensions(self, ctx):
        #await ctx.send("cog")
        pass



    @extensions.command(name="list")
    async def extensions_list(self, ctx):
        loaded:str = ""
        available:str = ""

        for ext in self.bot.extensions:
            loaded += f" - {ext}\n"

        for file in os.listdir("cog"):
            if ".py" in file:
                available += f"- cog.{file}\n"
            else:
                continue

        embed = tools.create_bot_embed(ctx, self.bot, self.color_embed, title=f"Extensions: {len(self.bot.extensions)}") # create embed
        embed.add_field(name="Loaded Extensions:", value=loaded) # create filed with list of all loaded extensions
        embed.add_field(name="Available Extensions:", value=available) # create filed with list of all available extensions
    
        await ctx.send(embed=embed)



    @extensions.command(name="load")
    async def extensions_load(self, ctx, *names):

        loading:str =""
        failed:str = ""
        successfull:str = ""

        for ext in names:
            loading += f"- {ext}\n"
            try:
                await self.bot.load_extension(ext)
                successfull += f"- {ext} \n"
            except Exception as E:
                await ctx.send(str(E))
                failed += f"- {ext} \n"


        embed = tools.create_bot_embed(ctx, self.bot, self.color_embed, title=f"Extensions: {len(self.bot.extensions)}") # create embed
        embed.add_field(name="Loading Extensions:", value=loading) # create filed with list of all extensions that where tried to load
        embed.add_field(name="Success:", value=successfull) # create filed with list of all successfully loaded extensions
        embed.add_field(name="Failed:", value=failed) # create filed with list of all failed to load extensions

        await ctx.send(embed=embed)



    @extensions.command(name="unload")
    async def extensions_unload(self, ctx, *names):

        unloading:str =""
        failed:str = ""
        successfull:str = ""

        for ext in names:
            unloading += f"- {ext}\n"
            try:
                await self.bot.unload_extension(ext)
                successfull += f"- {ext} \n"
            except Exception as E:
                await ctx.send(str(E))
                failed += f"- {ext} \n"


        embed = tools.create_bot_embed(ctx, self.bot, self.color_embed, title=f"Extensions: {len(self.bot.extensions)}") # create embed
        embed.add_field(name="Loading Extensions:", value=unloading) # create filed with list of all extensions that where tried to unload
        embed.add_field(name="Success:", value=successfull) # create filed with list of all successfully uloaded extensions
        embed.add_field(name="Failed:", value=failed) # create filed with list of all failed to unload extensions

        await ctx.send(embed=embed)



    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        print("SHUTING DOWN ...")
        await ctx.send("shutting down ...")
        await self.bot.close()
        print("Bot closed")



async def setup(bot):
    print("loading extension: bot")
    await bot.add_cog(BotAdministration(bot))