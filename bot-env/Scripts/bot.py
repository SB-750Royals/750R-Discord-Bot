import discord
from discord.ext import commands
from discord_slash import SlashCommand

from config import TOKEN

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='/', intents=intents)
slash = SlashCommand(client, sync_commands=True)


def run_discord_bot():
    # Initialize the bot
    @client.event
    async def on_ready():
        print('Bot is ready.')
        await client.get_channel(1072221045718798406).send(f'Pong! {round(client.latency * 1000)}ms')
        await client.change_presence(activity=discord.Game('Dead'))

    # Meeting Slash Commands
    @slash.slash(name="meeting", description="Create a new meeting")
    async def _meeting(ctx):
        await ctx.send("Meeting command")

    client.run(TOKEN)
