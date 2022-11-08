import discord
from discord.ext import commands
import os

from help_cog import help_cog
from music_cog import music_cog
intents = discord.Intents.all()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="penis ", intents = intents)

bot.remove_command("help")

@bot.event
async def on_ready():

    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

token = os.getenv("discord bot token")
bot.run(token)