from MinHeap import MinHeap
from HeapElement import HeapElement

class Simulation: 
	
	def __init__(self, numUnits):
		self.availableUnits =  [True for i in range(numUnits)]
		self.triageQueue = MinHeap()
		self.eventQueue = MinHeap()

	def addToIncidentQueue(self, incident):
		self.eventQueue.add(HeapElement(incident), incident.getTimePriority())

	def nextAvailableUnit(self):
		indx = 0
		for x in self.availableUnits:
			if x:
				return indx
			indx += 1
		return -1

	def markUnitUnavailable(self,unit):
		self.availableUnits[unit] = False

	def markUnitAvailable(self,unit):
		self.availableUnits[unit] = True

	def logReport(self, time, reportIncident):
		print("Time " + str(time) + ": " + reportIncident.getIncidentTypeString() + " reported (duration: "+ str(reportIncident.getDuration()) + ")")

	def logDispatch(self, time, dispatchIncident):
		print ("Time " + str(time) + ": unit " + str(dispatchIncident.getDispatchUnit()) + " dispatched to the " 
			+ dispatchIncident.getIncidentTypeString() + " reported at time " + str(dispatchIncident.getReportTime()) + ";"
			+ " will be resolved at time " + str(dispatchIncident.getDispatchTime() + dispatchIncident.getDuration()))
	
	def logResolution(self, time, dispatchIncident):
		print("Time " + str(time) + ": unit " + str(dispatchIncident.getDispatchUnit()) + " resolved the " + dispatchIncident.getIncidentTypeString() + " reported at time "+ str(dispatchIncident.getReportTime()) + ")")

	def availUnits(self):
		availUnits = False
		for x in self.availableUnits:
			if x:
				availUnits = True
		return availUnits
	
	def run(self):
		time = 0
		while self.eventQueue.size != 0:
			if self.eventQueue.peek() == None:
				break
			resolutions = []
			reports = []
			i  = self.eventQueue.peek() #my curr incident HEAP ELEMENT
			
			#sort into resolutions and reports at time x
			while i.value.getReportTime() == time or i.value.getResolutionTime() == time:
				if i.value.getResolutionTime() > 0:
					toAdd = HeapElement(self.eventQueue.poll().value.value)
					resolutions.append(toAdd)
				else:
					toAdd = HeapElement(self.eventQueue.poll().value.value)
					
					reports.append(toAdd)

				i = self.eventQueue.peek()
				
				
				if i == None:
					break

			#do the reports
			
			for x in reports:
				self.triageQueue.add(x, x.value.getTriagePriority())
				self.logReport(time, x.value)
				

			#do the resolutions
			k = 0
			for x in resolutions:
				done = resolutions[k].value
				self.markUnitAvailable(done.getDispatchUnit())
				self.logResolution(time,done)
				k +=1
			
			# dispatch available units

			while self.availUnits() and self.triageQueue.size > 0:
				t = HeapElement(self.triageQueue.poll().value.value)
				unitNum = self.nextAvailableUnit()
				t.value.dispatch(time, unitNum)
				self.markUnitUnavailable(unitNum)
				self.logDispatch(time, t.value)
				self.eventQueue.add(t, t.value.getResolutionTime())
			
			time += 1
			
