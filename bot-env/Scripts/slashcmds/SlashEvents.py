import discord
from discord import app_commands


class EventsGroup(app_commands.Group):

    pass

async def setup(client):
    client.tree.add_command(EventsGroup(name="Events", description="Event commands"))