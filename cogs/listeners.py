import discord
from discord.ext import commands
import json
import os

class Listeners(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener(name="on_message")
    async def on_message(self, msg: discord.Message):
        if msg.author.id == self.bot.user.id:  
            return
        dir_path = os.path.dirname(os.path.realpath(__file__))
        parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
        json_path = os.path.join(parent_dir_path, 'CallAndResponse.json')

        with open(json_path, 'r') as f:
            callAndResponse = json.load(f)
        for key in callAndResponse:
            if key in msg.content.lower():
                await msg.channel.send(callAndResponse[key])

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Listeners(bot)) # add the cog to the bot