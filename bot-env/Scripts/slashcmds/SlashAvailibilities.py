import discord
from discord import app_commands

import config

ROLE_ADMIN_750R = 703704798884790342
MEMBER_YEGNA_750R = 991121214120661053


class AvailibilitiesGroup(app_commands.Group):

    @app_commands.command(name="set-next-week", description="Determine which days are available for next week")
    async def setNextWeek(self, interaction, message: str):
        """
        Sets the available days for the next week based on the message parameter.
        The available days are written to a JSON file and a message is sent to the modlogs channel.

        Parameters:
        interaction (discord.Interaction): The interaction object.
        message (str): A string containing the available days for the next week.

        Returns:
        None
        """
        # Permission Check
        if not any(role.id == ROLE_ADMIN_750R for role in
                   interaction.user.roles) and interaction.user.id != MEMBER_YEGNA_750R:
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return

        days = []
        for char in message.lower():
            if char in "mtwrfsu":
                days.append(char)
        if len(days) == "none":
            days = None

        # Clear all data in assets\AvailibilitiesData.JSON and write the new data
        with open(
                r"C:\Users\Vigne\OneDrive\Documents\Programing Master\Python\Github Projects\750R-Discord-Bot\assets\AvailibilitiesData.JSON",
                "w") as file:
            file.write(f'{{"days": {days}}}')

        # Send a message to the modlogs channel
        embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /setNextWeek',
                              color=discord.Color.gold())
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.add_field(name="Days", value=f"{days}", inline=False)

        await interaction.response.send_message(f"Set next week's availibilities to {days}", ephemeral=True)
        await interaction.client.get_guild(config.SERVER_750R).get_channel(config.CHANNEL_MODLOGS_750R).send(
            embed=embed)


async def setup(client):
    client.tree.add_command(AvailibilitiesGroup(name="availbilities", description="availbilities commands"))
