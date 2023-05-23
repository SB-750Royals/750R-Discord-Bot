import time


class Meeting:

    def __init__(self, location, startTime, endTime, supposedAttendees, description, importance, meetingType):
        self.location = location
        self.startTime = startTime
        self.endTime = endTime
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
