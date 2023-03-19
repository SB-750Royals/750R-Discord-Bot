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


    # Status commands
    @client.command()
    async def status(ctx):
        ctx.message.content = ctx.message.content.lower().rstrip().lstrip()
        if len(ctx.message.content) > 128:
            await ctx.send(f'{ctx.message.author.mention} status too long')
        elif ctx.message.content[7:] == ' online':
            await client.change_presence(status=discord.Status.online)
        elif ctx.message.content[7:] == ' idle':
            await client.change_presence(status=discord.Status.idle)
        elif ctx.message.content[7:] == ' dnd':
            await client.change_presence(status=discord.Status.dnd)
        elif ctx.message.content[7:] == ' invisible':
            await client.change_presence(status=discord.Status.invisible)
        elif ctx.message.content[7:] == ' ping':
            await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
            await ctx.send(f'{ctx.message.author.mention} Latency: {(client.latency * 1000):.3f} ms')
        elif ctx.message.content[7:] == ' none':
            await client.change_presence(activity=discord.Game(''))
            await ctx.send(f'{ctx.message.author.mention} status changed to none')
        elif ctx.message.content[7:] == ' help' or ctx.message.content[7:] == '':
            await ctx.send(
                f'{ctx.message.author.mention} Use !ping followed by one of the paramters to set the bot\'s status:\n\t  - online\n\t - idle\n\t - dnd\n\t - invisible\n\t - ping\n\t - none\n\t - or a custom status\nUse !ping help to see this message')
        else:
            await client.change_presence(activity=discord.Game(ctx.message.content[7:]))
            await ctx.send(f'{ctx.message.author.mention} status changed to{ctx.message.content[7:]}')


    client.run(config.TOKEN)
