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
        await client.tree.sync()
        print(prfx + "Slash commands synced" + Fore.WHITE)

        # Post Initialization
        print(prfx + "Bot initialized" + Fore.YELLOW + client.user.name + Fore.WHITE + " is ready!")
        print(prfx + f'Latency: {(client.latency * 1000):.3f} ms')


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


    @client.tree.command(name="ping", description="Sends the bot's latency")
    async def ping(interaction):
        print(f'Pong! Latency is {client.latency}')
        await interaction.response.send_message(
            f"{interaction.user.mention} Latency is {round(client.latency * 1000, 2)} ms", ephemeral=True)


    # Asynch Listener for messages
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


    client.run(config.TOKEN)
