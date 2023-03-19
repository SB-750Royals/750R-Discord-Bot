import discord
from discord.ext import commands

import config

if __name__ == '__main__':
    client = discord.ext.commands.Bot(command_prefix='!', intents=discord.Intents.all())


    @client.event
    async def on_ready():
        await client.change_presence(
            activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))  # Latency in seconds
        print('Bot is ready!')


    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! Latency: {(client.latency * 1000):.3f} ms')


    client.run(config.TOKEN)
