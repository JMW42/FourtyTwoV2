
from yaml.loader import SafeLoader
from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context


import yaml, discord

# ========================================================================================================================
# ========================================================================================================================
# MAIN:

def main():

    # loading bot config
    print(f'loading bot configuration:')
    config_bot = load_bot_config()
    for key in config_bot:
        print(f' - {key}: {config_bot[key]}')
    


    bot = setup_bot(config_bot)
    bot.run(config_bot["TOKEN"])

# ========================================================================================================================
# ========================================================================================================================
# METHODS:

def load_bot_config():
    with open("config/bot.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as E:
            print(E)
            return None

def setup_bot(config_bot):
    bot = Bot(command_prefix=commands.when_mentioned_or(config_bot["PREFIX"]), intents=discord.Intents.default())

    @bot.event
    async def on_ready() -> None:
        print("bot ready")

    @bot.event
    async def on_command_error(ctx, err) -> None:
        print("ERROR:", err)
    
    return bot

# ========================================================================================================================

if __name__ == "__main__":
    main()