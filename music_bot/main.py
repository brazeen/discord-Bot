import discord
from discord.ext import commands
import os

import constants


intents = discord.Intents.all()
intents.message_content = True
intents.voice_states = True


# Define bot class
class MusicBot(commands.Bot):
    def __init__(self) -> None:
        """ Initialises bot """
        super().__init__(
            command_prefix="pls ",
            intents=intents,
            application_id=constants.APP_ID
        )

    async def setup_hook(self) -> None:
        """ Load cogs """
        await self.load_extension("help_cog")
        await self.load_extension("music_cog")
        await bot.tree.sync(guild=discord.Object(id=constants.GUILD_ID))

    async def on_ready(self) -> None:
        print("Bot is ready.")


bot = MusicBot()
bot.remove_command("help")

token = os.getenv("discord bot token")
bot.run(token)
