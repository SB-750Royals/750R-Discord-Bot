import time


class Meeting:

    def __init__(self, location, startTime, endTime, date, supposedAttendees, description, importance, meetingType):
        self.location = location
        self.startTime = startTime
        self.endTime = endTime
        self.date = date
        self.attendees = supposedAttendees
        self.description = description
        self.importance = importance
        self.meetingType = meetingType

        self.meetingID = int(time.time())
        self.actualAttendees = []
        self.meetingNotes = "blank"
        self.adminApproval = False
        self.pictureStatus = False
        self.cleanUpStatus = False
        self.meetingNotesStatus = False
        self.duration = self.endTime - self.startTime

    def __delete__(self, instance):
        del self

    # Meeting functions
    def addAttendee(self, attendee):
        self.attendees.append(attendee)

    def removeAttendee(self, attendee):
        self.attendees.remove(attendee)

    def addActualAttendee(self, attendee):
        self.actualAttendees.append(attendee)

    def removeActualAttendee(self, attendee):
        self.actualAttendees.remove(attendee)

    def editMeetingNotes(self, notes):
        self.meetingNotes = notes

    def pictureStatus(self, status):
        self.pictureStatus = status

    def cleanUpStatus(self, status):
        self.cleanUpStatus = status

    def editLocation(self, location):
        self.location = location

    def editStartTime(self, date):
        self.startTime = date
        duration = self.endTime - self.startTime

    def editEndTime(self, time):
        self.endTime = time
        duration = self.endTime - self.startTime

    def addSupposedAttendee(self, attendees):
        self.attendees = attendees

    def removeSupposedAttendee(self, attendees):
        self.actualAttendees = attendees

    # Getters
    def getMeetingID(self):
        return self.meetingID

    def getLocation(self):
        return self.location

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getAttendees(self):
        return self.attendees

    def getDescription(self):
        return self.description

    def getImportance(self):
        return self.importance

    def getMeetingType(self):
        return self.meetingType

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
