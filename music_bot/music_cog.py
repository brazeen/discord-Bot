import discord
from discord.ext import commands
from discord import app_commands

from youtube_dl import YoutubeDL

import constants


class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False
        self.is_Paused = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}

        self.vc = None

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" %
                                        item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(
                m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self, interaction: discord.Interaction):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']

            if self.vc is None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                if self.vc is None:
                    await interaction.response.send_message("Could not connect to the voice channel")
                    return

            else:
                await self.vc.move_to(self.music_queue[0][1])

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(
                m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())

        else:
            self.is_playing = False

    @app_commands.command(name="play", description="Play the selected song from YouTube")
    async def play(self, interaction: discord.Interaction, query: str):
        try:
            voice_channel = interaction.user.voice.channel
        except AttributeError:
            await interaction.response.send_message("Connect to a voice channel!")
            return  # Return from function to prevent code below from getting executed

        if self.is_Paused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(False):
                await interaction.response.send_message("Could not download the song. Incorrect format, try a different keyword!")
            else:
                await interaction.response.send_message("Song added to the queue")
                self.music_queue.append([song, voice_channel])

                if not self.is_playing:
                    await self.play_music(interaction)

    @app_commands.command(name="pause", description="Pause the current song that is being played")
    async def pause(self, interaction: discord.Interaction):
        if self.is_playing:
            self.is_playing = False
            self.is_Paused = True
            self.vc.pause()
        elif self.is_Paused:
            self.is_playing = True
            self.is_Paused = False
            self.vc.resume()

    @app_commands.command(name="resume", description="Resumes playing the current song")
    async def resume(self, interaction: discord.Interaction):
        if self.is_Paused:
            self.is_playing = True
            self.is_Paused = False
            self.vc.resume()

    @app_commands.command(name="skip", description="Skips the current song")
    async def skip(self, interaction: discord.Interaction):
        if self.vc is not None and self.vc:
            self.vc.stop()
            await self.play_music(interaction)

    # TODO: List queue in a better way
    @app_commands.command(name="queue", description="Shows current song queue")
    async def queue(self, interaction: discord.Interaction):
        retval = ""

        for i in range(0, len(self.music_queue)):
            if i > 4:
                break

            retval += self.music_queue[i][0]['title'] + '\n'

        if retval != "":
            await interaction.response.send_message(retval)
        else:
            await interaction.response.send_message("No music in the queue.")

    @app_commands.command(name="clear", description="Stops playing the current song and clears the queue")
    async def clear(self, interaction: discord.Interaction):
        if self.vc is not None and self.is_playing:
            self.vc.stop()
        self.music_queue = []
        await interaction.response.send_message("Music queue cleared")

    @app_commands.command(name="leave", description="Leaves the voice channel")
    async def leave(self, interaction: discord.Interaction):
        self.is_playing = False
        self.is_Paused = False
        await self.vc.disconnect()


async def setup(bot: commands.Bot) -> None:
    """ Setup cog on bot """
    await bot.add_cog(music_cog(bot), guilds=[discord.Object(constants.GUILD_ID)])
