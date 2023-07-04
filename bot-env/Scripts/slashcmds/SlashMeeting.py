import time

from discord import app_commands

meetings = []


class MeetingGroup(app_commands.Group):

    @app_commands.command(name="new", description="Create a new meeting")
    async def new(self, interaction, location: str, date: str, starttime: int, endtime: int, supposedattendees: str,
                  description: str):
        meetings.append(Meeting(location, date, starttime, endtime, supposedattendees, description))
        await interaction.response.send_message("Meeting Created", ephemeral=True)


async def setup(client):
    client.tree.add_command(MeetingGroup(name="meeting", description="meeting commands"))


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
