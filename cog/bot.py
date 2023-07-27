from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
import modules.tools as tools
import discord, time, os




class BotAdministration(commands.Cog):
    def __init__(self, bot) -> None:
        #super().__init__()
        self.bot:Bot = bot
        self.color_embed:discord.Colour = discord.Colour.light_embed()
        print("initializing cog: BotAdministration")



    @commands.group(invoke_without_command=True)
    @commands.is_owner()
    async def extensions(self, ctx):
        #await ctx.send("cog")
        pass



    @extensions.command(name="list")
    async def extensions_list(self, ctx):
        loaded:str = ""
        available:str = ""

        for ext in self.bot.extensions:
            loaded += f"- {ext}\n"

        for file in os.listdir("cog"):
            if (".py" in file) and not (file.replace('.py', '') in self.bot.extensions):
                available += f"- cog.{file.replace('.py', '')}\n"
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
        embed.add_field(name="Unoading Extensions:", value=unloading) # create filed with list of all extensions that where tried to unload
        embed.add_field(name="Success:", value=successfull) # create filed with list of all successfully uloaded extensions
        embed.add_field(name="Failed:", value=failed) # create filed with list of all failed to unload extensions

        await ctx.send(embed=embed)



    @commands.command(name="guilds", invoke_without_command=True)
    @commands.is_owner()
    async def guilds(self, ctx):
        glist:str = ""

        for guild in self.bot.guilds:
            glist += f"-{guild.name}\n"

        embed = tools.create_bot_embed(ctx, self.bot, self.color_embed, title=f"Guilds/Servers: {len(self.bot.guilds)}") # create embed
        embed.add_field(name="Member of guilds:", value=glist) # create filed with list of all knonw guilds
    
        await ctx.send(embed=embed)



    @commands.command(name="members", invoke_without_command=True)
    @commands.is_owner()
    async def member(self, ctx):
        rlist:str = ""
        rcount = 0

        for e in self.bot.get_all_members():
            rlist += f"- {e.name}\n"
            rcount += 1

        embed = tools.create_bot_embed(ctx, self.bot, self.color_embed, title=f"Members: {str(rcount)}") # create embed
        embed.add_field(name="Known members:", value=rlist) # create filed with list of all known Members
        
        await ctx.send(embed=embed)


    @commands.command(name="channels", invoke_without_command=True)
    @commands.is_owner()
    async def channels(self, ctx):
        rlist:str = ""
        rcount = 0

        for e in self.bot.get_all_channels():
            rlist += f"- {e.name}\n"
            rcount += 1

        embed = tools.create_bot_embed(ctx, self.bot, self.color_embed, title=f"Channels: {str(rcount)}") # create embed
        embed.add_field(name="Accessible channels:", value=rlist) # create filed with list of all known channels
        
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