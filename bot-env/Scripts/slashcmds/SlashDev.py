import discord
from discord import app_commands


class DevGroup(app_commands.Group):

    # TODO: Fix command on server
    @app_commands.command(name="exit", description="Terminates the bot")
    async def exit(self, interaction):
        """
        This function is used to terminate the bot. It checks if the user has the 'Admin' role and if so, sends a message to the server announcing the bot is shutting down, and then closes the bot. If the user does not have the 'Admin' role, it sends a message saying they do not have the necessary permissions to execute this command.

        Args:
            self: The instance of the class.
            interaction: The interaction object.

        Returns:
            None
        """
        if any(role.name == "Admin" for role in interaction.user.roles):
            embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /exit',
                                  color=discord.Color.gold())
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
            await interaction.response.send_message("Bot is shutting down")
            await interaction.client.get_guild(750_000_000_000_000_000).get_channel(750_000_000_000_000_000).send(
                embed=embed)
            await interaction.client.close()
        else:
            await interaction.response.send_message(
                "You do not have the necessary permissions to execute this command.")


async def setup(client):
    client.tree.add_command(DevGroup(name="dev", description="Developer commands"))
