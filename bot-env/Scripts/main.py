import asyncio

import discord
from discord.ext import commands

import config

if __name__ == '__main__':
    client = discord.ext.commands.Bot(command_prefix='!', intents=discord.Intents.all())


    @client.event
    async def on_ready():
        print("Initializing bot...")
        await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
        print("Bot initialized")
        print('\n' * 100)
        print('Bot is ready!')
        print(f'Logged in as {client.user.name} (ID: {client.user.id})')
        print(f'Latency: {(client.latency * 1000):.3f} ms')


    # Ping Command Groups
    @client.slash_command(description="Sends the bot's latency.")  # this decorator makes a slash command
    async def ping(ctx):  # a slash command will be created with the name "ping"
        await ctx.respond(f"Pong! Latency is {client.latency}")


    # Status Command Group
    status = client.create_group("status", "Change the bot's status")

    @status.command(description="Sets the bot's status to online")
    async def online(ctx, message: str):
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message))
        await ctx.respond("Status set to Online with message: " + message)

    @status.command(description="Sets the bot's status to idle")
    async def idle(ctx, message: str):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(message))
        await ctx.respond("Status set to idle with message: " + message)

    @status.command(description="Sets the bot's status to dnd")
    async def dnd(ctx, message: str):
        await client.change_presence(status=discord.Status.dnd, activity=discord.Game(message))
        await ctx.respond("Status set to dnd with message: " + message)

    @status.command(description="Sets the bot's status to invisible")
    async def invisible(ctx, message: str):
        await client.change_presence(status=discord.Status.invisible, activity=discord.Game(message))
        await ctx.respond("Status set to invisible with message: " + message)

    @status.command(description="Sets the bot's status to ping")
    async def latency(ctx):
        await client.change_presence(status=discord.Status.online,
                                     activity=discord.Game(f"Latency is {client.latency}"))
        await ctx.respond("Status set to ping")
        while True:
            await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
            await asyncio.sleep(60 * 60)

    @status.command(description="Clear the bots status")
    async def none(ctx):
        await client.change_presence(status=discord.Status.online, activity=discord.Game(""))
        await ctx.respond("Status Cleared")


    async def statusHelp(ctx):  # TODO CREATE CUSTOM EMBED MESSAGE FOR PING MESSAGES
        await ctx.respond(
            "Use !status followed by one of the parameters to set the bot's status:\n\t  - online\n\t - idle\n\t - dnd\n\t - invisible\n\t - ping\n\t - none\n\t - or a custom status\nUse !status help to see this message")


    # Left off on: https://guide.pycord.dev/interactions/application-commands/slash-commands

    # Meetings Command Group
    meetings = client.create_group("meetings", "meetings related commands")


    @meetings.command(
        description="Creates a new meeting")  # TODO: add options, add error handling, add custom embed, add permissions, create new meeting.py object, store to a file, add to a list, implement functionality
    async def new(ctx, location: str, starttime: str, endtime: str, date: str, description: str, importance: int,
                  meetingtype: str, meetingname: str):
        await ctx.respond(
            f"New meeting created at {location} from {starttime} to {endtime} with description {description} with importance {importance} of type {meetingtype} with name {meetingname} on the date {date}")


    @meetings.command(
        description="Edit an existing meeting")  # TODO: add options, add error handling, add custom embed, add permissions, create new meeting.py object, store to a file, add to a list
    async def edit(ctx, meetingname: str, location: str, starttime: str, endtime: str, date: str, description: str,
                   importance: int, meetingtype: str):
        await ctx.respond(
            f"Meeting {meetingname} edited to {location} from {starttime} to {endtime} with description {description} with importance {importance} of type {meetingtype} on the date {date}")


    @meetings.command(
        description="Delete an existing meeting")  # TODO: add options, add error handling, add custom embed, add permissions, create new meeting.py object, store to a file, add to a list, implement functionality
    async def delete(ctx, meetingname: str):
        await ctx.respond(f"Meeting {meetingname} deleted")


    # Attendance Command Group
    # Spending's Command group
    # Events Command Group
    # Help Command Group

    client.run(config.TOKEN)
