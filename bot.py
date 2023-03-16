import discord
from discord import app_commands
from discord.ext import commands

from config import TOKEN

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)


def run_discord_bot():
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        channel = client.get_channel(1072221045718798406)
        if channel:
            await channel.send("<@915063961777500180> The bot is online")
        else:
            print("Channel not found")

        try:
            synced = await tree.sync()
            print(f"synced {len(synced)} commands(s)")
        except Exception as e:
            print(e)

    @tree.command(name="hello")
    async def hello(interaction: discord.Interaction):
        await interaction.channel.send(f"Hey {interaction.user.mention}! First Slash command")

    client.run(TOKEN)

# TODO
# Create Slash Commands
# Create Custom Embed format
# Create Custom Attendance Sheet
# Link Custom Attendance Sheet to a google sheets
# TODO
# Create a custom event scheduler
# Schedule Custom Attendance Sheet to automatically display unless specifically turned off for that week
#
