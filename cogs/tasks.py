import requests, json, sys
import discord
from discord.ext import commands, tasks

priorLive = False
currentLive = False
class botTasks(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.submissionsCheck.start()

    def cog_unload(self):
        self.submissionsCheck.cancel()

    @tasks.loop(minutes=0.2)
    async def submissionsCheck(self):
        channelName = 'inmoonwetrust'
        contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')
        if 'isLiveBroadcast' in contents: 
            currentLive=True
        else:
            currentLive=False
            priorLive=True
        if currentLive and priorLive:
            streamChannel = self.bot.fetch_channel(1073867160230838372)
            await streamChannel.send("Moon is live! https://twitch.tv/inmoonwetrust @here")
            priorLive = False

def setup(bot):
    bot.add_cog(botTasks(bot))