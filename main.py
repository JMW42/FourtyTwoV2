
from yaml.loader import SafeLoader
from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context


import yaml, discord, asyncio

import module.bot as botlib

# ========================================================================================================================
# ========================================================================================================================
# MAIN:

def main():
    
    bot = botlib.UniversalBot("config/bot.yaml")
    bot.start_service()

    #bot = setup_bot(config_bot)
    #bot.run(config_bot["TOKEN"])


# ========================================================================================================================

if __name__ == "__main__":
    main()