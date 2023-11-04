from discord import app_commands

class ExpensesGroup(app_commands.Group):

    @app_commands.command(name="expenses", description="get spendings spreadsheet link")
    async def create(self, interaction):
        await interaction.response.send_message("https://docs.google.com/spreadsheets/d/1Lq1HU4udJPLt5BSk2sk89DRRWghRD6QIWxLBMrSEcXI/edit?usp=sharing", ephemeral=True)


async def setup(client):
    client.tree.add_command(ExpensesGroup(name="expenses", description="expenses commands"))
