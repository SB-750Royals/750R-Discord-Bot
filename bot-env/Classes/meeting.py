class Meeting:

    # Initialize the meeting object
    def __init__(self, location, startTime, endTime, date, supposedAttendees, description, importance, meetingType,
                 meetingID):
        # Custom variables
        self.meetingID = meetingID  # This is the meeting ID
        self.location = location  # Where is the meeting
        self.startTime = startTime  # This is a string
        self.endTime = endTime  # This is a string
        self.date = date  # This is a string
        self.attendees = supposedAttendees  # Who is required to be there
        self.description = description  # What is the meeting about
        self.importance = importance  # Fun (0), Normal (1), Required (2)
        self.meetingType = meetingType  # Research, Plan, Build, CAD, Programming, Driver, etc.

        # Calculated variables (These are calculated from the above variables)
        self.actualAttendees = []
        self.meetingNotes = "blank"
        self.adminApproval = False  # This is a boolean that is set to true when the admin approves the meeting
        self.pictureStatus = False  # This is a boolean that is set to true when the admin approves the pictures
        self.cleanUpStatus = False  # This is a boolean that is set to true when the admin approves the cleanup
        self.meetingNotesStatus = False  # This is a boolean that is set to true when the admin approves the meeting notes
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
