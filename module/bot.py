from discord.ext import commands
from yaml.loader import SafeLoader
from discord.ext import commands, tasks
#from discord.ext.commands import Bot, Context

import yaml, discord, asyncio


class UniversalBot(commands.Bot):
    def __init__(self, config_file:str):

        self.config_file = config_file
        self.bot_config = self.load_config(config_file)
        
        commands.Bot.__init__(self, command_prefix=commands.when_mentioned_or(self.bot_config["PREFIX"]), intents=discord.Intents.default())

    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # METHODS:

    def load_config(self, filepath):
        with open("config/bot.yaml", "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as E:
                print(E)
                return None
    

    async def setup(self):

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
        await ctx.send(str(err))
        print("ERROR:", err)
            

        
        
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------