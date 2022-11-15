import discord
from discord import app_commands
from discord.ext import commands

import constants


class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.text_channel_text = []

    @app_commands.command(name="help", description="Displays all the available commands")
    async def help(self, interaction: discord.Interaction):
        # TODO: Change to random colour
        embed = discord.Embed(title="Help", color=0x00ffb7)
        embed.set_footer(text=f"Requested by: {interaction.user.name}",
                         icon_url=interaction.user.avatar)

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

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """ Setup cog on bot """
    await bot.add_cog(help_cog(bot), guilds=[discord.Object(id=constants.GUILD_ID)])
