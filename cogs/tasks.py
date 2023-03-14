import requests, json, sys
import discord
from discord.ext import commands, tasks

priorLive = False
currentLive = False
delay = 0 
class botTasks(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot
        self.submissionsCheck.start()

    def cog_unload(self):
        self.submissionsCheck.cancel()

    @tasks.loop(minutes=5)
    async def submissionsCheck(self):
        global delay
        if delay:
            delay -= 1
            return
        global priorLive
        global currentLive
        channelName = 'inmoonwetrust'
        contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')
        print(contents)
        if 'isLiveBroadcast' in contents: 
            currentLive=True
            delay = 36
        else:
            currentLive=False
            priorLive=True
        if currentLive and priorLive:
            streamChannel = await self.bot.fetch_channel(1073867160230838372)
            await streamChannel.send("Moon is live! https://twitch.tv/inmoonwetrust @here")
            priorLive = False

def setup(bot):
    bot.add_cog(botTasks(bot))