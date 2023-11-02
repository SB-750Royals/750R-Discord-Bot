import discord
import config

from colorama import Fore, Style, Back
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import timedelta, datetime, time


if __name__ == '__main__':

    # Initialize bot
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    current_time = datetime.now()
    time_string = current_time.strftime("%H:%M:%S EST")
    prfx = (Back.LIGHTBLACK_EX + Fore.GREEN + time_string + Back.RESET + Fore.WHITE + Style.BRIGHT + " ")

    
    async def availibilities():
        print("Running weekly task")
        channel = client.get_channel(config.BOT_LOGS_750R) 


        now = datetime.utcnow()
        last_monday = now - timedelta(days=now.weekday())
        next_saturday = last_monday + timedelta(days=5)
        
        # Set the time to 12:00am for Monday and 11:59pm for Saturday
        start_of_week, end_of_week = int( datetime.combine(last_monday, time()).timestamp()), int(datetime.combine(next_saturday, time(23, 59)).timestamp())
        message_content = (
        f"<@&{config.ROLE_TEAMS_750R}> Availabilities for <t:{start_of_week}:D> - <t:{end_of_week}:D> "
        "Availabilities for this week. You are required to attend 1 meeting and the full team"
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
        await client.load_extension("slashcmds.SlashDev")

        # Initilalize Slash Commands
        await client.tree.sync(guild=client.get_guild(config.SERVER_750R))
        await client.tree.sync()

        print(prfx + "Slash commands synced" + Fore.WHITE)


        # Start weekly task
        scheduler = AsyncIOScheduler()
        scheduler.add_job(availibilities, CronTrigger(day_of_week='wed', hour=9, minute=7))
        scheduler.start()
        

        # Post Initialization Messages
        print(prfx + "Bot initialized " + Fore.YELLOW + client.user.name + Fore.WHITE + " is ready!")
        print(prfx + f'Latency: {(client.latency * 1000):.3f} ms')
        await client.get_guild(config.SERVER_750R).get_channel(config.CHANNEL_MODLOGS_750R).send(
            f"{client.user.name} is ready!")
        print(prfx + "Bot initialized, ready for use" + Fore.WHITE)

        # Set bot's name
        await client.user.edit(username="Teju")
        with open("assets/image.png", "rb") as f:
            await client.user.edit(avatar=f.read())


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        elif message.content.lower() == "hello all":
            await message.reply("Hello!")
        elif message.content.lower() == "hello":
            await message.reply("Hello!")
        elif message.content.lower() == "hi":
            await message.reply("Hi!")
        elif message.content.lower() == "hey all":
            await message.reply("HEY ALL!")
        elif message.content.lower().find("boba") != -1:
            await message.add_reaction("🧋")
            await message.add_reaction("🟰")
            await message.add_reaction("👎🏿")
        elif message.content.lower().find("expelliarmus") != -1:
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🔴")
            message = await message.reply("Protego!")
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🟣")
        elif message.content.lower().find("avada kedavra") != -1:
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🟢")
        elif message.content.lower().find("crucio") != -1:
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🟡")
        elif message.content.lower().find("imperio") != -1:
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🟠")
        elif message.content.lower().find("stupefy") != -1:
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🔵")
        elif message.content.lower().find("wingardium leviosa") != -1:
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🪶")
        elif message.content.lower().find("lumos") != -1:
            await message.add_reaction("🧙")
            await message.add_reaction("🪄")
            await message.add_reaction("🔦")
        elif message.content.lower().find("tej") != -1:
            with open("assets/image.png", "rb") as f:
                await message.channel.send(file=discord.File(f))
        elif message.content.lower().find("monkey") != -1:
            with open("assets\macaca_nigra_self-portrait-3e0070aa19a7fe36e802253048411a38f14a79f8-s1100-c50.jpg", "rb") as f:
                await message.channel.send(file=discord.File(f))
        elif message.content.lower().find("bye") != -1:
            await message.channel.send("bye")
        elif client.user.mentioned_in(message):
            await message.add_reaction("👀")
        


    client.run(config.TOKEN)

