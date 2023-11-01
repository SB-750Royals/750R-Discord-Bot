from discord import app_commands
from discord.ext import commands  # Import the commands extension

# TODO: Create embeds for commands
# TODO: Only allow certain people to use these commands
# TODO: Create modlog embeds for commands

class DevGroup(app_commands.Group):

    @app_commands.command(name="exit", description="Terminates the bot")
    async def exit(self, interaction):
        # Check if the user has the Admin role and respond accordingly
        if any(role.name == "Admin" for role in interaction.user.roles):
            await interaction.response.send_message("Bot is shutting down")
            await interaction.client.close()
        else:
            await interaction.response.send_message("You do not have the necessary permissions to execute this command.")

        

async def setup(client):
    client.tree.add_command(DevGroup(name="dev", description="Developer commands"))
