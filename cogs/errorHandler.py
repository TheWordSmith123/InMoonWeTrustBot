import discord
from discord.ext import commands

class ErrorHandler(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond(f"You do not have {error.missing_permissions[0].upper()} permission to execute this command!", ephemeral=True)
        else:
            await ctx.respond(error)
            raise error  # Here we raise other errors to ensure they aren't ignored
            
        
def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(ErrorHandler(bot)) # add the cog to the bot