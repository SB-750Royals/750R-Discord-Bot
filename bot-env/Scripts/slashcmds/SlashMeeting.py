import pickle
import time
from datetime import datetime

from discord import app_commands

# Load meetings from file
try:
    with open("meetings.pkl", "rb") as file:
        meetings = pickle.load(file)
except FileNotFoundError:
    meetings = []


# TODO: Create embeds for commands
# TODO: Only allow certain people to use these commands
# TODO: Only allow commands to work in 750R server
# TODO: Create modlog embeds for commands

class MeetingGroup(app_commands.Group):

    # TODO: add roles/people as option to supposedattendees

    async def new(self, interaction, location: str, date: str, starttime: str, endtime: str, supposedattendees: str,
                  description: str):

        # Check inputs and set default values
        if starttime == "":
            starttime = "16:00:00"
        if endtime == "":
            endtime = "18:00:00"
        if description == "":
            description = "Standard meeting"
        if location == "":
            location = "23 Aster WayDayton, NJ 08810"
        if date == "" or supposedattendees == "":
            await interaction.response.send_message("Fill in the date/people attending", ephemeral=True)
            return

        # Check if the date and time are valid
        try:
            date_obj = datetime.strptime(date, '%d-%m-%Y')
            start_time_obj = datetime.strptime(starttime, '%d-%m-%Y %H:%M:%S')
            end_time_obj = datetime.strptime(endtime, '%d-%m-%Y %H:%M:%S')

            meetings.append(Meeting(location, date_obj, start_time_obj, end_time_obj, supposedattendees, description))

        except ValueError:
            await interaction.response.send_message(
                "Invalid date or time format. Please provide the date in the format DD-MM-YYYY and time in the format DD-MM-YYYY HH:MM:SS.",
                ephemeral=True)
            return

        meetings.append(Meeting(location, date, starttime, endtime, supposedattendees, description))
        with open("meetings.pkl", "wb") as file1:
            pickle.dump(meetings, file1)

        # reply to user with meeting ID
        await interaction.response.send_message(f"Meeting created with ID {meetings[-1].getMeetingID()}",
                                                ephemeral=True)

        # TODO: CREATE MESSAGE IN MEETING LOGS CHANNEL
        # TODO: make that message upadte in realtime with changes to meeting


async def setup(client):
    client.tree.add_command(MeetingGroup(name="meetingss", description="meeting commandss"))


class Meeting:

    def __init__(self, location, date, startTime, endTime, supposedAttendees, description):
        self.location = location
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.attendees = supposedAttendees
        self.description = description

        self.meetingID = int(time.time())
        self.actualAttendees = []
        self.meetingNotes = "blank"
        self.adminApproval = False
        self.pictureStatus = False
        self.cleanUpStatus = False
        self.meetingNotesStatus = False
        self.duration = self.endTime - self.startTime

    # Create getter methods for each attribute
    def getLocation(self):
        return self.location

    def getDate(self):
        return self.date

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getAttendees(self):
        return self.attendees

    def getDescription(self):
        return self.description

    def getMeetingID(self):
        return self.meetingID

    def getActualAttendees(self):
        return self.actualAttendees

    def getMeetingNotes(self):
        return self.meetingNotes

    def getAdminApproval(self):
        return self.adminApproval

    def getPictureStatus(self):
        return self.pictureStatus

    def getCleanUpStatus(self):
        return self.cleanUpStatus

    def getMeetingNotesStatus(self):
        return self.meetingNotesStatus

    def getDuration(self):
        return self.duration

    def __delete__(self, instance):
        del self
