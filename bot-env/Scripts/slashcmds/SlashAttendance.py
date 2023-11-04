import json

import discord
import gspread
from discord import app_commands
from oauth2client.service_account import ServiceAccountCredentials

# Variables
# Members
MEMBER_NICK_750R = ["nk2023_", "Nicholas"]
MEMBER_ANUSHREE_750R = ["anuuu_0", "Anushree"]
MEMBER_HARI_750R = ["ThReT0(training arc)#7974", "Hari"]
MEMBER_ARJUN_750R = ["moon401", "Arjun"]
MEMBER_ANIKA_750R = ["hwisnfocnv", "Anika"]
MEMBER_TEJAS_750R = ["tejasr", "Tejas"]
MEMBER_VIGNESH_750R = ["vigneshs", "Vignesh"]
MEMBER_VIVEK_750R = ["hunter4420", "Vivek"]
MEMBER_VIHAAN_750R = ["thesurvivorx", "Vihaan"]
MEMBER_YEGNA_750R = ["yegna", "Yegna"]
MEMBER_RAKSHNA_750R = ["rockyroad7559", "Rakshna"]
MEMBER_ESHA_750R = ["eshavesha", "Esha"]
MEMBERS = [MEMBER_NICK_750R, MEMBER_ANUSHREE_750R, MEMBER_HARI_750R, MEMBER_ARJUN_750R, MEMBER_ANIKA_750R,
           MEMBER_TEJAS_750R, MEMBER_VIGNESH_750R, MEMBER_VIVEK_750R, MEMBER_VIHAAN_750R, MEMBER_YEGNA_750R,
           MEMBER_RAKSHNA_750R, MEMBER_ESHA_750R]

# Credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    r'C:\Users\Vigne\OneDrive\Documents\Programing Master\Python\Github Projects\750R-Discord-Bot\assets\credentials.json',
    scope)
client = gspread.authorize(creds)
sheet_url = 'https://docs.google.com/spreadsheets/d/1gR150DNFLcbYqfVO4tfAwFQ-Tjquxvb3Xd5mm9_e9Zg/edit?usp=sharing'


def get_all_sheet_data(url):
    output = []

    try:
        worksheet = client.open_by_url(url).sheet1
        sheet_data = worksheet.get_all_records()  # Returns a list of dictionaries
        for row in sheet_data:
            output.append(row)
        return output

    except Exception as e:
        output.append(None)
        print(e)


class AttendanceGroup(app_commands.Group):

    # Only @admin can use this command
    @app_commands.command(name="attendees", description="shows who attended meetings in the past week")
    async def attendees(self, interaction):
        pass

    # TODO: Remove debug code
    # TODO: Add better ero
    # TODO: Weekly attendance formatting
    @app_commands.command(name="show", description="shows the attendance of the person who used the command")
    async def show(self, interaction):

        # Look up the real name of the user from config.MEMBERS
        global name
        username = interaction.user.name
        name = None
        for member in MEMBERS:
            print(member[0], username, str(username) == str(member[0]))

            # Check if the current member's first element matches username
            if str(username) == str(member[0]):
                name = member[1]  # If a match is found, assign the second element of the member to name
                print("Name found:", name)
                break  # Exit the loop since we found a match

        # If name is still None, the user is not a member of 750R
        if name is None:
            await interaction.response.send_message("You are not a member of 750R.", ephemeral=True)
            return
        else:
            # Get the attendance data from Google Sheets
            data = get_all_sheet_data(sheet_url)

            # Set data to the array with the name of the user
            print(data, type(data))
            for row in data:
                if row['First Name'] == name:
                    data = row
                    break

            data_dict = json.loads(
                str(data).replace("'", '"'))  # replace single quotes with double quotes for valid JSON

            # Construct the embed
            embed = discord.Embed(title="Student Information", color=discord.Color.blue())

            # Use the dictionary to add fields to the embed
            embed.add_field(name="Club", value=data_dict.get("Club", "N/A"), inline=True)
            embed.add_field(name="Advisors", value=data_dict.get("Advisors", "N/A"), inline=True)
            embed.add_field(name="Name",
                            value=f'{data_dict.get("First Name", "N/A")} {data_dict.get("Last Name", "N/A")}',
                            inline=False)
            embed.add_field(name="Student ID", value=str(data_dict.get("Student ID", "N/A")), inline=True)
            embed.add_field(name="Grade", value=str(data_dict.get("Grade", "N/A")), inline=True)
            embed.add_field(name="Position", value=data_dict.get("Position", "N/A"), inline=True)
            embed.add_field(name="Gender", value=data_dict.get("Gender", "N/A"), inline=True)
            embed.add_field(name="Penalties", value=str(data_dict.get("Penalties", "N/A")), inline=True)
            embed.add_field(name="Percentage", value=f"{data_dict.get('Percentage', 'N/A')}%", inline=True)

            # Construct the attendance record string based on dates and values
            attendance_records = ""
            missed_sessions = ""
            for key, value in data_dict.items():
                if key in ['Club', 'Advisors', 'Last Name', 'First Name', 'Student ID', 'Grade', 'PTP', 'Position',
                           'Gender', 'Penalties', 'Percentage']:
                    continue  # skip non-date fields
                elif value == 1:
                    attendance_records += f"{key}: ✅\n"
                elif value == '':
                    missed_sessions += f"{key}: ❌\n"

            if attendance_records:
                embed.add_field(name="Attendance Record", value=attendance_records, inline=False)
            if missed_sessions:
                embed.add_field(name="Missed Sessions", value=missed_sessions, inline=False)

            # Send the embed
            await interaction.response.send_message(embed=embed, ephemeral=True)


# @app_commands.command(name="checkin", description="check in to the meeting happening that day")
#     async def checkin(self, interaction):
#         pass
#
#     # Return "you're bad" if they haven't checked in first
#     @app_commands.command(name="checkout", description="check out of the meeting happening that day")
#     async def checkout(self, interaction):
#         pass

async def setup(bot):
    bot.tree.add_command(AttendanceGroup(name="attendance", description="attendance commands"))
