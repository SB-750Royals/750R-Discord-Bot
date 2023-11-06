import json
from fractions import Fraction

import discord
import gspread
from discord import app_commands
from oauth2client.service_account import ServiceAccountCredentials

# Channels
SERVER_750R = 703694008345559130
CHANNEL_MODLOGS_750R = 1082361625073434636

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
MEMBER_ABHAYA_750R = ["abhaya_", "Abhaya"]
MEMBERS = [MEMBER_NICK_750R, MEMBER_ANUSHREE_750R, MEMBER_HARI_750R, MEMBER_ARJUN_750R, MEMBER_ANIKA_750R,
           MEMBER_TEJAS_750R, MEMBER_VIGNESH_750R, MEMBER_VIVEK_750R, MEMBER_VIHAAN_750R, MEMBER_YEGNA_750R,
           MEMBER_RAKSHNA_750R, MEMBER_ESHA_750R, MEMBER_ABHAYA_750R]

# Credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    r'750R-Discord-Bot/assets/credentials.json',
    scope)
client = gspread.authorize(creds)
sheet_url = 'https://docs.google.com/spreadsheets/d/1gR150DNFLcbYqfVO4tfAwFQ-Tjquxvb3Xd5mm9_e9Zg/edit?usp=sharing'


def get_all_sheet_data(url):
    """
    Retrieves all data from a Google Sheets worksheet and returns it as a list of dictionaries.

    Args:
        url (str): The URL of the Google Sheets worksheet.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row of data from the worksheet.
    """
    output = []

    try:
        worksheet = client.open_by_url(url).sheet1
        sheet_data = worksheet.get_all_records()  # Returns a list of dictionaries
        for row in sheet_data:
            output.append(row)
        return output

    except Exception as e:
        output.append(None)


class AttendanceGroup(app_commands.Group):

    # Only @admin can use this command
    @app_commands.command(name="attendees", description="shows who attended meetings in the past week")
    async def attendees(self, interaction):
        pass

    @app_commands.command(name="show", description="shows the attendance of the person who used the command")
    async def show(self, interaction):
        """
        Shows the attendance of the person who used the command.
        """
        # Look up the real name of the user from config.MEMBERS
        global name
        username = interaction.user.name
        name = None

        for member in MEMBERS:
            if str(username) == str(member[0]):
                name = member[1]
                break

                # If name is still None, the user is not a member of 750R
        if name is None:
            await interaction.response.send_message("You are not a member of 750R.", ephemeral=True)
            return
        else:
            data = get_all_sheet_data(sheet_url)

            # Error handling
            if not data:
                await interaction.response.send_message("Could not load attendance data. Please try again later.",
                                                        ephemeral=True)
                modlog_channel = interaction.client.get_guild(SERVER_750R).get_channel(CHANNEL_MODLOGS_750R)
                await modlog_channel.send("Error: Attendance data could not be retrieved.")
                return

            # Set data to the array with the name of the user
            for row in data:
                if row['First Name'] == name:
                    data = row
                    break

            data_dict = json.loads(
                str(data).replace("'", '"'))  # replace single quotes with double quotes for valid JSON

            # Construct the embed
            embed = discord.Embed(title="📚 Student Information", color=0x1abc9c)  # A more vibrant teal color

            # Use the dictionary to add fields to the embed with some Markdown for styling
            embed.add_field(
                name="**👤 Name**",
                value=f'*{data_dict.get("First Name", "N/A")} {data_dict.get("Last Name", "N/A")}*',
                inline=False
            )
            embed.add_field(name="**🆔 Student ID**", value=str(data_dict.get("Student ID", "N/A")), inline=True)
            embed.add_field(name="**📊 Grade**", value=str(data_dict.get("Grade", "N/A")), inline=True)
            embed.add_field(name="**🎖 Position**", value=data_dict.get("Position", "N/A"), inline=True)
            embed.add_field(name="**🚻 Gender**", value=data_dict.get("Gender", "N/A"), inline=True)
            embed.add_field(name="**⚠ Penalties**", value=str(data_dict.get("Penalties", "N/A")), inline=True)
            embed.add_field(name="**🔢 Percentage**", value=f"{data_dict.get('Percentage', 'N/A')}%", inline=True)

            # Construct the attendance record string based on dates and values with enhanced styling
            attendance_records = ""
            missed_sessions = ""
            count = 0
            for key, value in data_dict.items():
                if key in ['Club', 'Advisors', 'Last Name', 'First Name', 'Student ID', 'Grade', 'PTP', 'Position',
                           'Gender', 'Penalties', 'Percentage']:
                    continue
                elif key == '':
                    value = "N/A + 💤"
                    attendance_records += f"**{key:<10}**: {value:>5}" + "\n"
                else:
                    try:
                        if float(Fraction(value)) == 0:
                            emoji = " ❌"
                        elif float(Fraction(value)) < 1:
                            emoji = " ⚠️"
                        else:
                            emoji = " ✅"
                        attendance_records += f"**{key:<10}**: {float(Fraction(value)):>5.2f}" + emoji + "\n"
                    except ValueError:
                        attendance_records += f"**{key:<10}**: {value:>5}\n"

            if attendance_records:
                embed.add_field(name="**📅 Attendance Record**", value=attendance_records, inline=False)

            # Send the embed
            await interaction.response.send_message(embed=embed, ephemeral=True)

        # Mod log
        await interaction.client.get_guild(SERVER_750R).get_channel(CHANNEL_MODLOGS_750R).send(embed=embed)

    # TODO: Add checkin and checkout commands
    @app_commands.command(name="checkin", description="check in to the meeting happening that day")
    async def checkin(self, interaction):
        # reply to the user saying under construction
        await interaction.response.send_message("This command is under construction.", ephemeral=True)

    # Return "you're bad" if they haven't checked in first
    @app_commands.command(name="checkout", description="check out of the meeting happening that day")
    async def checkout(self, interaction):
        # reply to the user saying under construction
        await interaction.response.send_message("This command is under construction.", ephemeral=True)


async def setup(bot):
    bot.tree.add_command(AttendanceGroup(name="attendance", description="attendance commands"))
