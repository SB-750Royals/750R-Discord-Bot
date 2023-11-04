import discord
from discord import app_commands

SERVER_750R = 703694008345559130
CHANNEL_MODLOGS_750R = 1082361625073434636


class ExpensesGroup(app_commands.Group):

    @app_commands.command(name="expenses", description="get spendings spreadsheet link")
    async def create(self, interaction):
        await interaction.response.send_message(
            "https://docs.google.com/spreadsheets/d/1Lq1HU4udJPLt5BSk2sk89DRRWghRD6QIWxLBMrSEcXI/edit?usp=sharing",
            ephemeral=True)
        # Create an embed for modlogs
        embed = discord.Embed(title="Expenses Spreadsheet Link",
                              color=discord.Color.gold())
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        embed.add_field(name="User", value=interaction.user.mention, inline=False)
        embed.add_field(name="Channel", value=interaction.channel.mention, inline=False)
        embed.add_field(name="Message", value=interaction.message.content, inline=False)
        embed.add_field(name="Response",
                        value="https://docs.google.com/spreadsheets/d/1Lq1HU4udJPLt5BSk2sk89DRRWghRD6QIWxLBMrSEcXI/edit?usp=sharing",
                        inline=False)
        embed.set_footer(text=f"User ID: {interaction.user.id}")
        await interaction.client.get_guild(SERVER_750R).get_channel(CHANNEL_MODLOGS_750R).send(embed=embed)


async def setup(client):
    client.tree.add_command(ExpensesGroup(name="expenses", description="expenses commands"))
