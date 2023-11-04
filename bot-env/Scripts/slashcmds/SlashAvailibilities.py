import discord
from discord import app_commands

import config


class AvailibilitiesGroup(app_commands.Group):

    @app_commands.command(name="set-next-week", description="Determine which days are available for next week")
    async def setNextWeek(self, interaction, message: str):
        days = []
        for char in message.lower():
            if char in "mtwrfsu":
                days.append(char)
        if len(days) == "none":
            days = None

        # Clear all data in assets\AvailibilitiesData.JSON and write the new data
        with open(
                r"C:\Users\Vigne\OneDrive\Documents\Programing Master\Python\Github Projects\750R-Discord-Bot\assets\macaca_nigra_self-portrait-3e0070aa19a7fe36e802253048411a38f14a79f8-s1100-c50.jpg",
                "w") as file:
            file.write(f'{{"days": {days}}}')

        # Send a message to the modlogs channel
        embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /setNextWeek',
                              color=discord.Color.gold())
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.add_field(name="Days", value=f"{days}", inline=False)

        await interaction.client.get_guild(config.SERVER_750R).get_channel(config.CHANNEL_MODLOGS_750R).send(
            embed=embed)

        await interaction.response.send_message(f"Set next week's availibilities to {days}", ephemeral=True)


async def setup(client):
    client.tree.add_command(AvailibilitiesGroup(name="availbilities", description="availbilities commands"))
