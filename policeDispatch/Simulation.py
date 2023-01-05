import numpy as np

class Simulation: 
	
	def __init__(self, numUnits):
		self.availableUnits =  [True for i in range(numUnits)]
		self.triageQueue = Minheap(3000)
		self.eventQueue = Minheap(3000)

	def addToIncidentQueue(self, incident):
		self.eventQueue.insert(self, )