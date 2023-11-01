import discord
from discord import app_commands


# Server
SERVER_750R = 703694008345559130

# Role IDs
ROLE_ADMIN_750R = 703704798884790342
ROLE_ALUMNI_750R = 703699518230757428
ROLE_HEADPROG_750R = 1087136859693527050
ROLE_BOTDEVELOPER_750R = 1169396374291357748

# Channels IDs
CHANNEL_MODLOGS_750R = 1082361625073434636

# Permission Array
permissionArray = [ROLE_ADMIN_750R, ROLE_HEADPROG_750R, ROLE_BOTDEVELOPER_750R]


class StatusGroup(app_commands.Group):
    """
    A class representing a group of slash commands for setting the bot's status.
    """

    @app_commands.command(name="online", description="Set the bot's status to online")
    async def online(self, interaction, message: str):
        """
        A slash command that sets the bot's status to online.

        Parameters:
        interaction (discord.Interaction): The interaction object representing the user's interaction with the command.
        message (str): The message to be displayed as the bot's activity.

        Returns:
        None
        """
        # Check if the user has a role in permissionArray
        if not any(role.id in permissionArray for role in interaction.user.roles):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return
        else:
            embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /status',
                              color=discord.Color.gold())
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
            embed.add_field(name="New Status", value=str(discord.Status.online).capitalize(), inline=False)
            embed.add_field(name="New Message", value=message, inline=False)

            await interaction.client.get_guild(SERVER_750R).get_channel(CHANNEL_MODLOGS_750R).send(
                embed=embed)
            await interaction.client.change_presence(status=discord.Status.online, activity=discord.Game(name=message))
            await interaction.response.send_message(f"Status set to Online with message: {message}", ephemeral=True)
        

    @app_commands.command(name="offline", description="Set the bot's status to offline")
    async def idle(self, interaction, message: str):
        """
        A slash command that sets the bot's status to offline.

        Parameters:
        interaction (discord.Interaction): The interaction object representing the user's interaction with the command.
        message (str): The message to be displayed as the bot's activity.

        Returns:
        None
        """
        if not any(role.id in permissionArray for role in interaction.user.roles):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return
        else:
            embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /status',
                              color=discord.Color.gold())
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
            embed.add_field(name="New Status", value=str(discord.Status.idle).capitalize(), inline=False)
            embed.add_field(name="New Message", value=message, inline=False)

            await interaction.client.get_guild(703694008345559130).get_channel(CHANNEL_MODLOGS_750R).send(
                embed=embed)
            await interaction.client.change_presence(status=discord.Status.idle, activity=discord.Game(name=message))
            await interaction.response.send_message(f"Status set to idle with message: {message}", ephemeral=True)
        

    @app_commands.command(name="dnd", description="Set the bot's status to dnd")
    async def dnd(self, interaction, message: str):
        """
        A slash command that sets the bot's status to do not disturb (dnd).

        Parameters:
        interaction (discord.Interaction): The interaction object representing the user's interaction with the command.
        message (str): The message to be displayed as the bot's activity.

        Returns:
        None
        """
        if not any(role.id in permissionArray for role in interaction.user.roles):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return
        else:
            embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /status',
                                color=discord.Color.gold())
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
            embed.add_field(name="New Status", value=str(discord.Status.dnd).capitalize(), inline=False)
            embed.add_field(name="New Message", value=message, inline=False)

            await interaction.client.get_guild(703694008345559130).get_channel(CHANNEL_MODLOGS_750R).send(
                embed=embed)
            await interaction.client.change_presence(status=discord.Status.dnd, activity=discord.Game(name=message))
            await interaction.response.send_message(f"Status set to dnd with message: {message}", ephemeral=True)

    @app_commands.command(name="invisible", description="Set the bot's status to invisible")
    async def invisible(self, interaction):
        """
        A slash command that sets the bot's status to invisible.

        Parameters:
        interaction (discord.Interaction): The interaction object representing the user's interaction with the command.

        Returns:
        None
        """
        if not any(role.id in permissionArray for role in interaction.user.roles):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return
        else:
            embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /status',
                                color=discord.Color.gold())
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
            embed.add_field(name="New Status", value=str(discord.Status.invisible).capitalize(), inline=False)

            await interaction.client.get_guild(703694008345559130).get_channel(CHANNEL_MODLOGS_750R).send(
                embed=embed)
            await interaction.client.change_presence(status=discord.Status.invisible)
            await interaction.response.send_message("Status set to invisible", ephemeral=True)

    @app_commands.command(name="latency", description="Set the bot's status to latency")
    async def latency(self, interaction):
        """
        A slash command that sets the bot's status to latency.

        Parameters:
        interaction (discord.Interaction): The interaction object representing the user's interaction with the command.

        Returns:
        None
        """
        if not any(role.id in permissionArray for role in interaction.user.roles):
            await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
            return
        else:
            if interaction.client.status == discord.Status.invisible: 
                await interaction.client.change_presence(status=discord.Status.online)
            embed = discord.Embed(title=f'{discord.utils.escape_markdown(interaction.user.display_name)} Used /status',
                                color=discord.Color.gold())
            embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
            embed.add_field(name="New Status", value=str(interaction.client.status).capitalize(), inline=False)
            embed.add_field(name="New Message", value="Latency", inline=False)

            await interaction.client.get_guild(703694008345559130).get_channel(CHANNEL_MODLOGS_750R).send(
                embed=embed)
            await interaction.client.change_presence(
                activity=discord.Game(name=f"Latency: {(interaction.client.latency * 1000):.3f} ms"))
            await interaction.response.send_message("Status set to latency", ephemeral=True)


async def setup(client):
    client.tree.add_command(StatusGroup(name="status", description="bot status commands"))