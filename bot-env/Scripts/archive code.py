# # DM People funny stuff
# @client.event
# async def on_message(message):
#     if message.author == client.user:  # Ignore messages from the bot itself
#         return
#     if message.content.startswith('!dm ') and message.channel.id == 1091807880879026257:
#         try:
#             user_id, msg = message.content[4:].split(' ', 1)
#             user_id.replace('[', '').replace(']', '')
#             msg.replace('[', '').replace(']', '')
#             print(user_id, msg)
#             user = await client.fetch_user(int(user_id))
#             await user.send(msg)
#             await message.channel.send(f'Message sent to {user.name}.')
#         except ValueError:
#             await message.channel.send('Invalid command usage. Try !dm [user ID] [message].')
#         except discord.Forbidden:
#             await message.channel.send(f"Could not send message to {user.name}.")
#     else:
#         # if the message is a dm then send f'{message.author.name}: {message.content}' to the channel with id 1091772044603035770
#         if isinstance(message.channel, discord.DMChannel):
#             channel = client.get_channel(1091807880879026257)
#             await channel.send(f'New DM from {message.author.name}: {message.content}')
#         print(f'New DM from {message.author.name}: {message.content}')


# Old bot
import asyncio
import pickle

import discord
import discord.ext.commands

import config

if __name__ == '__main__':

    # Pickle Data
    try:
        with open("state.bin", "rb") as f:
            state = pickle.load(f)
            meetingsList = state[0]
            attendance = state[1]
            expenses = state[2]
            events = state[3]
            taskScheduler = state[4]
            polls = state[5]
    except FileNotFoundError:
        meetingsList = []
        attendance = []
        expenses = []
        events = []
        taskScheduler = []
        polls = []

    client = discord.ext.commands.Bot(command_prefix='!', intents=discord.Intents.all())


    @client.event
    async def on_ready():
        print("Initializing bot...")
        await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
        print("Bot initialized")
        print('\n' * 1)
        print('Bot is ready!')
        print(f'Logged in as {client.user.name} (ID: {client.user.id})')
        print(f'Latency: {(client.latency * 1000):.3f} ms')


    # Ping Command Groups
    @client.command(description="Sends the bot's latency.")  # this decorator makes a slash command
    async def ping(ctx):  # a slash command will be created with the name "ping"
        await ctx.respond(f"Pong! Latency is {client.latency}")


    @client.event
    async def on_message(message):
        if message.content.startswith("I'm a leaving"):
            member_id = 915063961777500180
            member = await message.guild.fetch_member(member_id)
            await member.kick()


    # Status Command Group
    @client.group()
    async def status(self, ctx):
        pass


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

    # Meetings Command Group # TODO ADD TO meetings channel with custom embed
    @client.group(invoke_without_command=True)
    async def meeting(self, ctx):
        pass


    @meeting.command(
        description="Creates a new meeting")  # TODO: add options, add error handling, add custom embed, add permissions, create new meeting.py object, store to a file, add to a list, implement functionality
    async def new(ctx, location: str, starttime: str, endtime: str, date: str, description: str, importance: int,
                  meetingtype: str, meetingname: str):
        await ctx.respond(
            f"New meeting created at {location} from {starttime} to {endtime} with description {description} with importance {importance} of type {meetingtype} with name {meetingname} on the date {date}")
        pickler()


    @meeting.command(
        description="Edit an existing meeting")  # TODO: add options, add error handling, add custom embed, add permissions, create new meeting.py object, store to a file, add to a list
    async def edit(ctx, meetingname: str, location: str, starttime: str, endtime: str, date: str, description: str,
                   importance: int, meetingtype: str):
        await ctx.respond(
            f"Meeting {meetingname} edited to {location} from {starttime} to {endtime} with description {description} with importance {importance} of type {meetingtype} on the date {date}")


    @meeting.command(
        description="Delete an existing meeting")  # TODO: add options, add error handling, add custom embed, add permissions, create new meeting.py object, store to a file, add to a list, implement functionality
    async def delete(ctx, meetingname: str):
        await ctx.respond(f"Meeting {meetingname} deleted")


    # Attendance Command Group
    # Spending's Command group
    # Events Command Group
    # Help Command Group

    client.run(config.TOKEN)


# Method Definitions

def pickler():
    information = [meetingsList, attendance, expenses, events, taskScheduler, polls]
    with open("state.bin", "wb") as ff:
        pickle.dump(information, ff)
