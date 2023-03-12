import discord, sys, time, json, os

sys.path.append('..')

from discord.commands import SlashCommandGroup
from discord.ext import commands
from usefulFunctions import format_duration

class AutoResponseCommands(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    responses = SlashCommandGroup("responses", "Various commands pertaining to the auto-response function.")

    @responses.command(name = "list", description = "Lists the various auto-responses set up.")
    async def list(self, ctx: discord.ApplicationContext):
        embed=discord.Embed(title="Auto-Response List", description="The auto-responses set up for this server")

        with open('CallAndResponse.json', 'r') as f:
            callAndResponse = json.load(f)
        for key in callAndResponse:
            embed.add_field(name=key, value=callAndResponse[key], inline=False)
        await ctx.respond(embed=embed)
        
def setup(bot):
    bot.add_cog(AutoResponseCommands(bot))