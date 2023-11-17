from datetime import timedelta, datetime, time

import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from colorama import Fore, Style, Back
from discord.ext import commands

import config


if __name__ == '__main__':

    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    current_time = datetime.now()
    time_string = current_time.strftime("%H:%M:%S EST")
    prfx = (Back.LIGHTBLACK_EX + Fore.GREEN + time_string + Back.RESET + Fore.WHITE + Style.BRIGHT + " ")

    # Scheduler Functions
    async def availibilities():

        # Initialize
        channel = client.get_channel(704006958969127052)
        now = datetime.utcnow() + timedelta(days=1)
        last_monday = now - timedelta(days=now.weekday())
        next_saturday = last_monday + timedelta(days=5)

        # Description
        with open(
                r"assets\AvailibilitiesDescription.JSON",
                "r") as file:
            data = file.read()
            if data != "null":
                data = eval(data)
                message_content = data["description"]
            else:
                message_content = (
                    f"<@&{config.ROLE_TEAMS_750R}> Availabilities for <t:{start_of_week}:D> - <t:{end_of_week}:D> "
                    "Availabilities for this week. You are required to attend **1 meeting** and the full team"
                    "meeting on Friday. React with which days you are coming. Attendance for last week is posted"
                )
            with open(
                    r"assets\AvailibilitiesDescription.JSON",
                    "w") as file:
                file.write("null")

        # Create Message
        start_of_week, end_of_week = int(datetime.combine(last_monday, time()).timestamp()), int(
            datetime.combine(next_saturday, time(23, 59)).timestamp())
        message_content = (
            f"<@&{config.ROLE_TEAMS_750R}> Availabilities for <t:{start_of_week}:D> - <t:{end_of_week}:D> " + message_content
        )
        msg = await channel.send(message_content)

        with open(
                r"assets\AvailibilitiesData.JSON",
                "r") as file:
            data = file.read()
            if data != "null":
                data = eval(data)
                for day in data["days"]:
                    if day == "m":
                        await msg.add_reaction("🇲")
                    elif day == "t":
                        await msg.add_reaction("🇹")
                    elif day == "w":
                        await msg.add_reaction("🇼")
                    elif day == "r":
                        await msg.add_reaction("🇷")
                    elif day == "f":
                        await msg.add_reaction("🇫")
                    elif day == "s":
                        await msg.add_reaction("🇸")
                    elif day == "u":
                        await msg.add_reaction("🇺")
            else:
                await msg.add_reaction("🇲")
                await msg.add_reaction("🇹")
                await msg.add_reaction("🇼")
                await msg.add_reaction("🇷")
                await msg.add_reaction("🇫")
                await msg.add_reaction("🇸")
                await msg.add_reaction("🇺")
            with open(
                    r"assets\AvailibilitiesData.JSON",
                    "w") as file:
                file.write("null")

    async def christmas():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Merry Christmas!")
        await message.add_reaction("🎄")

    async def diwali():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy Diwali!")
        await message.add_reaction("🪔")

    async def halloween():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy Halloween!")
        await message.add_reaction("🎃")

    async def thanksgiving():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy Thanksgiving!")
        await message.add_reaction("🦃")
    
    async def newyear():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy New Year!")
        await message.add_reaction("🎉")

    async def easter():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy Easter!")
        await message.add_reaction("🐰")

    async def valentines():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy Valentine's Day!")
        await message.add_reaction("💖")

    async def mothersday():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy Mother's Day!")
        await message.add_reaction("👩")

    async def fathersday():
        channel = client.get_channel(config.CHANNEL_ANNOUNCEMENTS_750R)
        message = channel.send(f"<@&{config.ROLE_TEAMS_750R}> Happy Father's Day!")
        await message.add_reaction("👨")

    @client.event
    async def on_ready():

        # Initialization
        print(prfx + "Initializing bot..." + Fore.WHITE)
        await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
        print(prfx + "Status set to: " + Fore.YELLOW + f'Latency: {(client.latency * 1000):.3f} ms' + Fore.WHITE)

        # Load Slash Command extensions
        await client.load_extension("slashcmds.SlashStatus")
        await client.load_extension("slashcmds.SlashPing")
        await client.load_extension("slashcmds.SlashDev")
        await client.load_extension("slashcmds.SlashAvailibilities")
        await client.load_extension("slashcmds.SlashAttendance")
        await client.load_extension("slashcmds.SlashExpenses")
        # await client.load_extension("slashcmds.SlashAssignment")

        # Initilalize Slash (Uncomment to sync slash commands, comment when no changes to avoid rate limit)
        await client.tree.sync(guild=client.get_guild(config.SERVER_750R))
        await client.tree.sync()

        print(prfx + "Slash commands synced" + Fore.WHITE)

        # Start weekly task
        scheduler = AsyncIOScheduler()
        scheduler.add_job(availibilities, CronTrigger(day_of_week="sun", hour=0, minute=0, second=0))
        scheduler.add_job(christmas, CronTrigger(day=25, month=12, hour=0, minute=0))
        scheduler.add_job(diwali, CronTrigger(day=4, month=11, hour=0, minute=0))
        scheduler.add_job(halloween, CronTrigger(day=31, month=10, hour=0, minute=0))
        scheduler.add_job(thanksgiving, CronTrigger(day=25, month=11, hour=0, minute=0))
        scheduler.add_job(newyear, CronTrigger(day=1, month=1, hour=0, minute=0))
        scheduler.add_job(easter, CronTrigger(day=4, month=4, hour=0, minute=0))
        scheduler.add_job(valentines, CronTrigger(day=14, month=2, hour=0, minute=0))
        scheduler.add_job(mothersday, CronTrigger(day=9, month=5, hour=0, minute=0))
        scheduler.add_job(fathersday, CronTrigger(day=20, month=6, hour=0, minute=0))
        scheduler.start()



        # Post Initialization Messages
        print(prfx + "Bot initialized " + Fore.YELLOW + client.user.name + Fore.WHITE + " is ready!")
        print(prfx + f'Latency: {(client.latency * 1000):.3f} ms')
        embed = discord.Embed(title=f'{client.user.name} is ready!',
                              color=discord.Color.gold())
        embed.set_author(name=client.user.display_name, icon_url=client.user.avatar.url)
        embed.add_field(name="Latency", value=f"{(client.latency * 1000):.3f} ms", inline=False)
        await client.get_guild(config.SERVER_750R).get_channel(config.CHANNEL_MODLOGS_750R).send(embed=embed)

        print(prfx + "Bot initialized, ready for use" + Fore.WHITE)

        # Set bot's name
        # await client.user.edit(username="750Royals")
        # with open(
        #         r"C:\Users\Vigne\Downloads\8-5IDJn0IR0v1ecJx.png",
        #         "rb") as f:
        #     await client.user.edit(avatar=f.read())

    # TODO: Delete Meme Code
    @client.event
    async def on_reaction_add(reaction, user):
        if user.bot:
            return
        elif reaction.message.author.id == 1119326295701078157 or reaction.message.author.id == 915063961777500180:
            await reaction.remove(user)
            await reaction.message.channel.send(f"{user.mention} You cannot react to this message")


    # Detect when a slash command is used
    @client.event
    async def on_error(event, *args, **kwargs):
        print(prfx + Fore.RED + "An error has occurred" + Fore.WHITE)
        print(prfx + Fore.RED + f"Event: {event}" + Fore.WHITE)
        print(prfx + Fore.RED + f"Args: {args}" + Fore.WHITE)
        print(prfx + Fore.RED + f"Kwargs: {kwargs}" + Fore.WHITE)

        # Send an error message to modlogs
        embed = discord.Embed(title=f'An error has occurred',
                                color=discord.Color.red())
        embed.set_author(name=client.user.display_name, icon_url=client.user.avatar.url)
        embed.add_field(name="Event", value=f"{event}", inline=False)
        embed.add_field(name="Args", value=f"{args}", inline=False)
        embed.add_field(name="Kwargs", value=f"{kwargs}", inline=False)
        await client.get_guild(config.SERVER_750R).get_channel(config.CHANNEL_MODLOGS_750R).send(embed=embed)

        await client.get_guild(config.SERVER_750R).get_channel(config.CHANNEL_MODLOGS_750R).send(embed=embed)

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
        elif message.content.lower().find("bye") != -1:
            await message.channel.send("bye")
        elif client.user.mentioned_in(message):
            await message.add_reaction("👀")


    client.run(config.TOKEN)
