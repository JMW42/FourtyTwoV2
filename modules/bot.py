from discord.ext import commands
from yaml.loader import SafeLoader
from discord.ext import commands, tasks
#from discord.ext.commands import Bot, Context
import modules.tools as tools

import yaml, discord, asyncio, os


class UniversalBot(commands.Bot):
    def __init__(self, config_file:str):

        self.config_file = config_file
        #self.config_dict = self.load_config(config_file)
        self.bot_config = tools.load_config_file(self.config_file)
        
        commands.Bot.__init__(self, command_prefix=commands.when_mentioned_or(self.bot_config["PREFIX"]), intents = discord.Intents.all())
        
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # METHODS:

    async def setup(self):

        # print config:
        print(r'seting up bot:')
        for key in self.bot_config:
            print(f'\t - {key}: {self.bot_config[key]}')

        # set username
        await self.user.edit(username=self.bot_config['BOTNAME'])

        # load startup cogs
        for cog in self.bot_config["STARTUPEXTENSIONS"]:
            await self.load_extension(cog)

        
        # basic commands:
        @self.command(name="restartup")
        @commands.is_owner()
        async def restartup(ctx):
            await ctx.send("loading startup configuration")
            await self.setup()
            await ctx.send("done")



    def start_service(self):
        self.run(self.bot_config["TOKEN"])    

    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # EVENTS:

    async def on_ready(self) -> None:
        await self.setup()
        print("bot ready")
    


    async def on_command_error(self, ctx, err) -> None:
        # dynamic dialog handler
        if isinstance(err, commands.errors.CommandNotFound) and self.user.mentioned_in(ctx):
            # dialog handling
            await ctx.send("DIALOG: " + str(ctx))
            print("DIALOG:", str(ctx))

        else:
            # normal error handling
            await ctx.send(str(err))
            print("ERROR:", err)
    


    async def on_message(self, ctx):
        if ctx.author.id == self.user.id: return
        
        if self.user.mentioned_in(ctx):
            await ctx.channel.send("Hey! I've been mentioned.")
        
        await self.process_commands(ctx)
        
        
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------