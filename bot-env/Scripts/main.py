import discord
from discord.ext import commands

import config

if __name__ == '__main__':
    client = discord.ext.commands.Bot(command_prefix='!', intents=discord.Intents.all())


    @client.event
    async def on_ready():
        print("Initializing bot...")
        await client.change_presence(
            activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
        print("Bot initialized")

        try:
            synced = await client.tree.sync()
            print(f'Synced {synced} commands')
        except Exception as e:
            print(f'Error syncing commands: {e}')
        print("Commands Initialized")

        print('\n' * 100)
        print('Bot is ready!')
        print(f'Logged in as {client.user.name} (ID: {client.user.id})')
        print(f'Latency: {(client.latency * 1000):.3f} ms')


    # Ping/Ping Commands
    @client.tree.command(name='ping', description='Responds with the latency of the bot')
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! Latency: {(client.latency * 1000):.3f} ms')


    # Status commands
    @client.command()  # TODO CREATE CUSTOM EMBED MESSAGE FOR PING MESSAGES
    async def status(ctx):
        ctx.message.content = ctx.message.content.rstrip().lstrip()
        if len(ctx.message.content.lower()) > 128:
            await ctx.send(f'{ctx.message.author.mention} status too long')
        elif ctx.message.content[7:].lower() == ' online':
            await client.change_presence(status=discord.Status.online)
        elif ctx.message.content[7:].lower() == ' idle':
            await client.change_presence(status=discord.Status.idle)
        elif ctx.message.content[7:].lower() == ' dnd':
            await client.change_presence(status=discord.Status.dnd)
        elif ctx.message.content[7:].lower() == ' invisible':
            await client.change_presence(status=discord.Status.invisible)
        elif ctx.message.content[7:].lower() == ' ping':
            await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
            await ctx.send(f'{ctx.message.author.mention} Latency: {(client.latency * 1000):.3f} ms')
        elif ctx.message.content[7:].lower() == ' none':
            await client.change_presence(activity=discord.Game(''))
            await ctx.send(f'{ctx.message.author.mention} status changed to none')
        elif ctx.message.content[7:].lower() == ' help' or ctx.message.content[7:].lower() == '':
            await ctx.send(
                f'{ctx.message.author.mention} Use !ping followed by one of the parameters to set the bot\'s status:\n\t  - online\n\t - idle\n\t - dnd\n\t - invisible\n\t - ping\n\t - none\n\t - or a custom status\nUse !ping help to see this message')
        else:
            await client.change_presence(activity=discord.Game(ctx.message.content[7:]))
            await ctx.send(f'{ctx.message.author.mention} status changed to{ctx.message.content[7:]}')


    # Meeting Commands

    client.run(config.TOKEN)
