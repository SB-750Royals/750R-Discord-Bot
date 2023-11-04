from discord import app_commands


# Store the assignments in assignmnet.json and assignment log in assignment_log.json

class AssignmentGroup(app_commands.Group):

    # TODO: Under Construction
    @app_commands.command(name="create", description="create new assignment")
    async def create(self, interaction):
        await interaction.response.send_message("Under Construction", ephemeral=True)

    # TODO: Under Construction
    @app_commands.command(name="delete", description="delete an assignment")
    async def delete(self, interaction):
        await interaction.response.send_message("Under Construction", ephemeral=True)

    # TODO: Under Construction
    @app_commands.command(name="checkoff", description="Verify assignment you assigned")
    async def checkoff(self, interaction):
        await interaction.response.send_message("Under Construction", ephemeral=True)

    # TODO: Under Construction
    @app_commands.command(name="mine", description="list all your active assignments")
    async def mine(self, interaction):
        await interaction.response.send_message("Under Construction", ephemeral=True)

    # TODO: Under Construction
    @app_commands.command(name="all", description="list all active assignments for the server")
    async def all(self, interaction):
        await interaction.response.send_message("Under Construction", ephemeral=True)

    @app_commands.command(name="submit", description="submit an assignment")
    async def submit(self, interaction):
        await interaction.response.send_message("Under Construction", ephemeral=True)


async def setup(client):
    client.tree.add_command(AssignmentGroup(name="assignment", description="assignment commands"))
