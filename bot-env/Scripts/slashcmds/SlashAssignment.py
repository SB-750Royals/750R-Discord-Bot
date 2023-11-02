import discord
from discord import app_commands

import config

# Store the assignments in assignmnet.json and assignment log in assignment_log.json

class AssignmentGroup(app_commands.Group):

    @app_commands.command(name="create", description="create new assignment")
    async def create(self, interaction):
        pass

    @app_commands.command(name="delete", description="delete an assignment")
    async def delete(self, interaction):
        pass

    @app_commands.command(name="checkoff", description="Verify assignment you assigned")
    async def checkoff(self, interaction):
        pass

    @app_commands.command(name="mine", description="list all your active assignments")
    async def mine(self, interaction):
        pass

    @app_commands.command(name="all", description="list all active assignments for the server")
    async def all(self, interaction):
        pass

    @app_commands.command(name="submit", description="submit an assignment")
    async def submit(self, interaction):
        pass


async def setup(client):
    client.tree.add_command(AssignmentGroup(name="assignment", description="assignment commands"))




    
