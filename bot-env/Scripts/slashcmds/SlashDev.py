from discord import app_commands


class DevGroup(app_commands.Group):

    @app_commands.command(name="exit", description="Terminates the bot")
    async def exit(self, interaction):
        await interaction.client.get_guild(703694008345559130).get_channel(1082361625073434636).send(
            "Bot is shutting down")
        await interaction.response.send_message("Bot is shutting down")

        await interaction.client.close()


async def setup(client):
    client.tree.add_command(DevGroup(name="dev", description="Developer commands"))
