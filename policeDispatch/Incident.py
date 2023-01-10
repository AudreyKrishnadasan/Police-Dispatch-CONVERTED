from IncidentType import IncidentType

class Incident:

    def __init__(self, userReportTime, userIncidentType, userDuration):
        self.reportTime = userReportTime
        self.incidentType = userIncidentType
        self.duration = userDuration
        self.dispatchTime = -1
        self.dispatchedUnit = -1

    def dispatch(self, currentTime, unit):
        self.dispatchTime = currentTime
        self.dispatchedUnit = unit

    def dispatched(self):
        return self.dispatchTime != -1 and self.dispatchedUnit != -1

    def getReportTime(self):
        return self.reportTime

    def getDuration(self):
        return self.duration

    def getIncidentType(self):
        return self.incidentType

    def getDispatchTime(self):
        return self.dispatchTime

    def getDispatchUnit(self):
        return self.dispatchedUnit

    def getResolutionTime(self):
        if self.dispatched():
            return self.dispatchTime + self.duration
        else:
            return -1

    def getTimePriority(self):
        if self.dispatched():
            return self.getResolutionTime()
        else:
            return self.reportTime

    def getTriagePriority(self):
        multiplier = 0
        if self.incidentType == IncidentType.WELLNESS_CHECK:
            multiplier = 3
        elif self.incidentType == IncidentType.TRAFFIC_COLLISION:
            multiplier = 2
        elif self.incidentType == IncidentType.ROBBERY:
            multiplier = 1
        elif self.incidentType == IncidentType.MURDER:
            multiplier = 0
        return multiplier * 200000 + self.reportTime

    def getIncidentTypeString(self):
        if self.incidentType == IncidentType.WELLNESS_CHECK:
            return "wellness check"
        elif self.incidentType == IncidentType.TRAFFIC_COLLISION:
            return "traffic collision"
        elif self.incidentType == IncidentType.ROBBERY:
            return "robbery"
        elif self.incidentType == IncidentType.MURDER:
            return "murder"
        return ""

    def toString(self):
        return ("Incident("
            + str(self.reportTime) + ", "
            + self.getIncidentTypeString() + ", "
            + str(self.duration) + ", "
            + str(self.dispatchTime) + ", "
            + str(self.dispatchedUnit)
            + ")")

