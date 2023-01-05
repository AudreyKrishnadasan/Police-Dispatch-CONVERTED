class Incident:

    reportTime = 0
    incidentType = WELLNESS_CHECK
    duration = 0

    def __init__(self, userReportTime, userIncidentType, userDuration):
        self.reportTime = userReportTime
        self.indcidentType = userIncidentType
        self.duration = userDuration
        self.dispatchTime = -1
        self.dispatchedUnit = -1

    def dispatch(self, currentTime, unit):
        self.dispatchTime = currentTime
        self.dispatchedUnit = unit

    def dispatched(self):
        return self.dispatchTime != -1 && self.dispatchedUnit != -1

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
        if dispatched(self):
            return self.dispatchTime + self.duration
        else:
            return -1

    def getTimePriority():
        if dispatched(self):
            return getResolutionTime(self)
        else:
            return self.reportTime

    def getTriagePriority():
        multiplier = 0
        if self.incidentType == IncidentType.WELLNESS_CHECK:
            multiplier = 3
        else if self.incidentType == IncidentType.TRAFFIC_COLLISION:
            multiplier = 2
        else if self.incidentType == IncidentType.ROBBERY:
            multiplier = 1
        else if self.incidentType == IncidentType.MURDER:
            multiplier = 0
        return multiplier * 200000 + self.reportTime

    def getIncidentTypeString():
        if self.incidentType == IncidentType.WELLNESS_CHECK:
            return "wellness check"
        else if self.incidentType == IncidentType.TRAFFIC_COLLISION:
            return "traffic collision"
        else if self.incidentType == IncidentType.ROBBERY:
            return "robbery"
        else if self.incidentType == IncidentType.MURDER:
            return "murder"
        return ""

    def toString():
        return ("Incident("
            + self.reportTime + ", "
            + getIncidentTypeString(self) + ", "
            + self.duration + ", "
            + self.dispatchTime + ", "
            + self.dispatchedUnit
            + ")")
