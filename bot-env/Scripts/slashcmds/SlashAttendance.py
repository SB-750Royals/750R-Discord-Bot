# import discord
# from discord import app_commands

# import config

# # Store ths week's attendance in a file in assets directory (use JSON)
# # At the end of the week Output file to some archive channel and delete from file

# class AttendanceGroup(app_commands.Group):

#     # Only @admin can use this command
#     @app_commands.command(name="attendees", description="shows who attended meetings in the past week")
#     async def attendees(self, interaction):
#         pass

#     # Use API to get attendance of the person who used the command from google sheets
#     @app_commands.command(name="show", description="shows the attendance of the person who used the command")
#     async def show(self, interaction):
#         pass

#     @app_commands.command(name="checkin", description="check in to the meeting happening that day")
#     async def checkin(self, interaction):
#         pass

#     # Return "you're bad" if they haven't checked in first
#     @app_commands.command(name="checkout", description="check out of the meeting happening that day")
#     async def checkout(self, interaction):
#         pass
