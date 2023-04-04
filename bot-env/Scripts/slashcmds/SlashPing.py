import discord
from discord import app_commands

import config


class PingGroup(app_commands.Group):

    # TODO CREATE EMBED FOR PING MESSAGE
    @app_commands.command()
    async def ping(self, interaction):
        embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /ping',
                              color=discord.Color.gold())
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.add_field(name="Latency", value=f"{round(interaction.client.latency * 1000, 2)} ms", inline=False)

        await interaction.client.get_guild(703694008345559130).get_channel(config.CHANNEL_MODLOGS_750R).send(
            embed=embed)
        await interaction.response.send_message(
            f"{interaction.user.mention} Latency is {round(interaction.client.latency * 1000, 2)} ms", ephemeral=True)


async def setup(client):
    client.tree.add_command(PingGroup(name="ping", description="Pings the bot"))
