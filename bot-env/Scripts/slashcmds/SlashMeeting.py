import discord
from discord import app_commands


# TODO Implement Permission Checks

class MeetingGroup(app_commands.Group):

    @app_commands.command(description="Creates a meeting")
    @app_commands.choices(meetingTypes=[
        discord.app_commands.Choice(name="Build", value=1),
        discord.app_commands.Choice(name="Programming", value=2),
        discord.app_commands.Choice(name="CAD", value=3),
        discord.app_commands.Choice(name="Website", value=4),
        discord.app_commands.Choice(name="Notebook", value=5),
        discord.app_commands.Choice(name="Plan", value=6),
        discord.app_commands.Choice(name="Full Team", value=7),
        discord.app_commands.Choice(name="Team Bonding", value=8),
        discord.app_commands.Choice(name="Other", value=9)
    ])
    async def create(self, interaction, meetingType: discord.app_commands.Choice[int]):
        await interaction.response.send_message("Meeting created", ephemeral=True)


async def setup(client):
    client.tree.add_command(MeetingGroup(name="meeting", description=""))
