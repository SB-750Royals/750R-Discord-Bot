import time

import discord
from colorama import Fore, Style, Back
from discord.ext import commands

import config

if __name__ == '__main__':
    client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
    prfx = (Back.LIGHTBLACK_EX + Fore.GREEN + time.strftime("%H:%M:%S EST",
                                                            time.localtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT + " ")

    @client.event
    async def on_ready():
        # Initialization
        print(prfx + "Initializing bot..." + Fore.WHITE)
        await client.change_presence(activity=discord.Game(f'Latency: {(client.latency * 1000):.3f} ms'))
        print(prfx + "Status set to: " + Fore.YELLOW + f'Latency: {(client.latency * 1000):.3f} ms' + Fore.WHITE)

        # Initialize Slash Commands
        client.tree.copy_global_to(guild=client.get_guild(config.SERVER_750R))
        await client.load_extension("slashcmds.SlashStatus")
        await client.load_extension("slashcmds.SlashPing")
        await client.tree.sync(guild=client.get_guild(config.SERVER_750R))
        print(prfx + "Slash commands synced" + Fore.WHITE)

        # Post Initialization
        print(prfx + "Bot initialized" + Fore.YELLOW + client.user.name + Fore.WHITE + " is ready!")
        print(prfx + f'Latency: {(client.latency * 1000):.3f} ms')


    # TODO ORGANIZE COMMANDS INTO SEPARATE FILES
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
            await message.content("Hey all!")


    @client.command(aliases=["stop", "exit", "quit", "abort"])
    async def shutdown(ctx):
        if ctx.author.id != 915063961777500180:
            await ctx.send("You do not have permission to use this command")
            return
        else:

            embed = discord.Embed(  # TODO: Improve Embed
                title=f"{client.user.name} is shutting down",
                description=f"Current time is {time.strftime('%H:%M:%S EST', time.localtime())}",
                color=discord.Color.green()
            )
            embed.set_footer(text=f"Authorization from {ctx.author.name}")
            await ctx.send(embed=embed)
            await client.close()
            print(prfx + "Bot has been shut down.")
            exit()

    client.run(config.TOKEN)

