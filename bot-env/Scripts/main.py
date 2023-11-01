import discord

from colorama import Fore, Style, Back
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import timedelta, datetime, time

import config

if __name__ == '__main__':

    # Functions
    def get_week_duration():
        now = datetime.utcnow()
        last_monday = now - timedelta(days=now.weekday())
        next_saturday = last_monday + timedelta(days=5)
        
        # Set the time to 12:00am for Monday and 11:59pm for Saturday
        start_of_week = datetime.combine(last_monday, time()).timestamp()
        end_of_week = datetime.combine(next_saturday, time(23, 59)).timestamp()

        return int(start_of_week), int(end_of_week)

    # Initialize bot
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    current_time = datetime.now()
    time_string = current_time.strftime("%H:%M:%S EST")
    prfx = (Back.LIGHTBLACK_EX + Fore.GREEN + time_string + Back.RESET + Fore.WHITE + Style.BRIGHT + " ")

    
    async def availibilities():
        print("Running weekly task")
        channel = client.get_channel(703713168807035020) 

        start_of_week, end_of_week = get_week_duration()
        message_content = (
        f"<@&940086503466500117> Availabilities for <t:{start_of_week}:D> - <t:{end_of_week}:D> "
        "Availabilities for this week. You are required to attend 1 meeting and the full team "
        "meeting on Friday. React with which days you are coming."
        )

        msg = await channel.send(message_content)
        await msg.add_reaction("🇲")
        await msg.add_reaction("🇹")
        await msg.add_reaction("🇼")
        await msg.add_reaction("🇹")
        await msg.add_reaction("🇫")
        await msg.add_reaction("🇸")

    @client.event
    async def on_ready():

        # Initialization
        print(prfx + "Initializing bot..." + Fore.WHITE)
        await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
        print(prfx + "Status set to: " + Fore.YELLOW + f'Latency: {(client.latency * 1000):.3f} ms' + Fore.WHITE)

        # Initialize Slash Commands
        # TODO Make specific commands work in DMs
        client.tree.copy_global_to(guild=client.get_guild(config.SERVER_750R))

        # Load Slash Command extensions
        await client.load_extension("slashcmds.SlashStatus")
        await client.load_extension("slashcmds.SlashPing")
        await client.load_extension("slashcmds.SlashMeeting")
        await client.load_extension("slashcmds.SlashDev")

        # Initilalize Slash Commands
        await client.tree.sync(guild=client.get_guild(config.SERVER_750R))
        await client.tree.sync()

        print(prfx + "Slash commands synced" + Fore.WHITE)


        # Start weekly task
        scheduler = AsyncIOScheduler()
        trigger = CronTrigger(day_of_week='wed', hour=9, minute=7)
        scheduler.add_job(availibilities, trigger)
        scheduler.start()
        

        # Post Initialization Messages
        print(prfx + "Bot initialized " + Fore.YELLOW + client.user.name + Fore.WHITE + " is ready!")
        print(prfx + f'Latency: {(client.latency * 1000):.3f} ms')
        await client.get_guild(703694008345559130).get_channel(1082361625073434636).send(
            f"{client.user.name} is ready!")
        



    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        elif message.content.lower() == "hello all":
            await message.channel.send("HELLO ALL!")
        elif message.content.lower() == "hello":
            await message.channel.send("Hello!")
        elif message.content.lower() == "hi":
            await message.channel.send("Hi!")
        elif message.content.lower() == "hey":
            await message.content.send("Hey!")
        elif message.content.lower() == "hey all":
            await message.content("hihi!")
        elif message.content.lower() == "hihi":
            await message.content.send("Hihi!")
        elif message.content.lower().find("boba") != -1:
            await message.add_reaction("🧋")



    client.run(config.TOKEN)

