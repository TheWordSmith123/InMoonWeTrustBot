import discord, logging, os

from discord import commands
from discord.ext import commands
from discord.commands import SlashCommandGroup
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    successful = []
    failed = []
    errors = []
    for file in os.listdir("cogs"):
        try:
            if file[-3:] == ".py":
                bot.load_extension("cogs." + file[:-3])
                successful.append(file[:-3])
        except Exception as err:
            failed.append(file[:-3])
            errors.append(err)
    if len(successful):
        logging.info(f"Succesfully loaded {len(successful)} cogs: {', '.join(successful)}")
    if len(failed):
        logging.error(msg=f"Failed to load {len(failed)} cogs: {', '.join(failed)}")
        for error in errors:
            print(error)
    bot.run(os.getenv('TOKEN'))