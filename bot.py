import discord
from discord import app_commands

from config import TOKEN

timeouts = {}


def run_discord_bot():
    # Set up Code
    intents = discord.Intents.default()
    intents.members = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        await client.get_channel(1072221045718798406).send("<@915063961777500180> The bot is online")

    client.run(TOKEN)
