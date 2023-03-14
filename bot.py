import discord
from datetime import datetime, timedelta

timeouts = {}
TOKEN = 'MTA2OTY3OTYzNjk3NzU0OTQzMg.GHkaTq.O9C43OOpL69wklXMs0NXzZlhBJL6YZgRU8_XEg'


def run_discord_bot():
    # Set up Code
    intents = discord.Intents.default()
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Break up each part of the message
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if username != "750R#4477":
            await message.channel.send("We are going to worlds!!")

    client.run(TOKEN)
