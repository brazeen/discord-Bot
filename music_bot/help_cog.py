import discord
from discord.ext import commands

from main import PREFIX


class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.text_channel_text = []

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0x00ffb7)  # TODO: Change to random colour
        embed.set_footer(text=f"Requested by: {ctx.message.author.name}",
                         icon_url=ctx.message.author.avatar_url)

        embed.add_field(name=f"{PREFIX} help",
                        value="Displays all the available commands",
                        inline=False)
        embed.add_field(name=f"{PREFIX} play (query)",
                        value="Plays music from the query",
                        inline=False)
        embed.add_field(name=f"{PREFIX} pause",
                        value="Pauses/Unpauses music",
                        inline=False)
        embed.add_field(name=f"{PREFIX} queue",
                        value="Displays music queue",
                        inline=False)
        embed.add_field(name=f"{PREFIX} leave",
                        value="Leaves the voice channel",
                        inline=False)
        embed.add_field(name=f"{PREFIX} resume",
                        value="Resumes playing the music",
                        inline=False)
        embed.add_field(name=f"{PREFIX} skip",
                        value="Skips the current song being played",
                        inline=False)
        embed.add_field(name=f"{PREFIX} clear",
                        value="Clears the queue",
                        inline=False)

        await ctx.send(embed=embed)
