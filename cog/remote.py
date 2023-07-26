from discord.ext import commands, tasks
from discord.ext.commands import Bot, Context
import module.tools as tools
import discord, time, os, random, subprocess, time




class Remote(commands.Cog):
    def __init__(self, bot) -> None:
        #super().__init__()
        print("initializing cog: RemoteCog")

        self.bot:Bot = bot
        self.color_embed:discord.Colour = discord.Colour.dark_gray()
        self.proc = subprocess.Popen(stdin=subprocess.PIPE, shell=True)
        #self.stdout = self.proc.communicate('ls -lash')

        
        print("remote initialised")


    @commands.is_owner()
    @commands.command(name="cmd")
    async def cmd(self, ctx, cmd:str, *args):
        line = cmd + " ".join(args)
        await ctx.send(f"EXECUTE: {line}")

        self.proc.stdin.write(line.encode() + b'\n')
        #self.proc.stdin.close()
        #self.proc.wait()
        time.sleep(0.25)
        
        out = ""
        for b in self.proc.stdout.readlines():
            out += str(b, "utf-8") + "\n"

        await ctx.send(out)



async def setup(bot):
    print("loading extension: remote")
    await bot.add_cog(Remote(bot))