import discord, sys, time

sys.path.append('..')

from discord.commands import SlashCommandGroup
from discord.ext import commands
from usefulFunctions import format_duration

start_time = time.time()

class DevCommands(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    timings = SlashCommandGroup("timings", "Various timing commands")

    @timings.command(name = "ping", description = "Shows the bot's latency.")
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"Pong! Latency is {int(self.bot.latency*1000)} ms.")
    
    @timings.command(name = "uptime", description = "Shows the bot's uptime." )
    async def uptime(self, ctx: discord.ApplicationContext):
        currentUptime = int(time.time()-start_time) + 3630
        await ctx.respond(f"This bot has been up for {format_duration(currentUptime)}.")

    owners = SlashCommandGroup("owner", "Various Owner-Only Commands", checks=[commands.is_owner().predicate])

    @owners.command(name = "quit", description="Turns off the bot.")
    @commands.is_owner()
    async def quit(self, ctx):
        await ctx.respond("Shutting down the bot")
        await self.bot.close()


def setup(bot):
    bot.add_cog(DevCommands(bot))