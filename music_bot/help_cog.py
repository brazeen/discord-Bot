import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """

```
General commands:
penis help - displays all the available commands
penis play (keywords) - plays music
penis pause - pauses music/unpauses music
penis queue - displays music queue
penis leave - leaves the voice channel
penis resume - resumes playing music
penis skip - skips the current song being played
penis clear - clears the queue
```
"""
        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx,):
        await ctx.send(self.help_message)