import discord
from discord.ext import commands


class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.text_channel_text = []

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0x00ffb7)  # TODO: Change to random colour
        embed.set_footer(text=f"Requested by: {ctx.message.author.name}",
                         icon_url=ctx.message.author.avatar)

        embed.add_field(name="penis help",
                        value="Displays all the available commands",
                        inline=False)
        embed.add_field(name="penis play (query)",
                        value="Plays music from the query",
                        inline=False)
        embed.add_field(name="penis pause",
                        value="Pauses/Unpauses music",
                        inline=False)
        embed.add_field(name="penis queue",
                        value="Displays music queue",
                        inline=False)
        embed.add_field(name="penis leave",
                        value="Leaves the voice channel",
                        inline=False)
        embed.add_field(name="penis resume",
                        value="Resumes playing the music",
                        inline=False)
        embed.add_field(name="penis skip",
                        value="Skips the current song being played",
                        inline=False)
        embed.add_field(name="penis clear",
                        value="Clears the queue",
                        inline=False)

        await ctx.send(embed=embed)
