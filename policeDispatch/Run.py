from MinHeap import MinHeap
from HeapElement import HeapElement
from Simulation import Simulation
from Incident import Incident
from IncidentType import IncidentType
from tkinter import*


class Run:
    root = Tk()
    root.title("Police Dispatch Simulation")

    def firstClick():
        numUnits = e.get()
        top = Toplevel()
        top.title('Enter Event Details')
        
        explainLbl = Label(top, text = "Enter event details here, once you have finalized your details for that event, click submit event button. Continue entering events until you are ready to watch your simulation unfold and hit run simulation!")
        explainLbl.pack()

        reportTimeLbl = Label(top, text = "Enter the report time (ex: 0, 43, 277)")
        reportTimeLbl.pack()

        eReportTime = Entry(top, width = 20)
        eReportTime.pack()

        typeLbl = Label(top, text="Select the type of Event")
        typeLbl.pack()

        durationLbl = Label(top, text = "Enter the duration of the event")
        durationLbl.pack()

        eDuration = Entry(top, width = 20)
        eDuration.pack()


        submitEventBtn = Button(top, text="submit event")
        submitEventBtn.pack()
        runSimBtn = Button(top, text = "Run Simulation")
        runSimBtn.pack()
        return

    welcomeLabel = Label(root, text="Welcome to the Police Dispatch Simulator!")
    welcomeLabel.pack()

    numUnitsLbl = Label(root, text="Enter the number of Police Units in your simulation")
    numUnitsLbl.pack()

    global e
    e = Entry(root, width = 20)
    e.pack()
    
    button1 = Button(root, text="continue", command=firstClick)
    button1.pack()
    

    mainloop()

    sim = Simulation(4)
    sim.addToIncidentQueue(Incident(339, IncidentType.ROBBERY, 97))
    sim.addToIncidentQueue(Incident(331, IncidentType.TRAFFIC_COLLISION, 97))
    sim.addToIncidentQueue(Incident(314, IncidentType.ROBBERY, 33))
    sim.addToIncidentQueue(Incident(301, IncidentType.TRAFFIC_COLLISION, 46))
    sim.addToIncidentQueue(Incident(294, IncidentType.ROBBERY, 80))
    sim.addToIncidentQueue(Incident(280, IncidentType.WELLNESS_CHECK, 21))
    sim.addToIncidentQueue(Incident(280, IncidentType.MURDER, 118))
    sim.addToIncidentQueue(Incident(274, IncidentType.ROBBERY, 96))
    sim.addToIncidentQueue(Incident(273, IncidentType.TRAFFIC_COLLISION, 53))
    sim.addToIncidentQueue(Incident(272, IncidentType.WELLNESS_CHECK, 58))
    sim.addToIncidentQueue(Incident(272, IncidentType.ROBBERY, 119))
    sim.addToIncidentQueue(Incident(269, IncidentType.WELLNESS_CHECK, 16))
    sim.addToIncidentQueue(Incident(261, IncidentType.MURDER, 80))
    sim.addToIncidentQueue(Incident(253, IncidentType.ROBBERY, 76))
    sim.addToIncidentQueue(Incident(242, IncidentType.TRAFFIC_COLLISION, 45))
    sim.addToIncidentQueue(Incident(236, IncidentType.MURDER, 45))
    sim.addToIncidentQueue(Incident(230, IncidentType.WELLNESS_CHECK, 30))
    sim.addToIncidentQueue(Incident(228, IncidentType.ROBBERY, 24))
    sim.addToIncidentQueue(Incident(212, IncidentType.MURDER, 53))
    sim.addToIncidentQueue(Incident(205, IncidentType.TRAFFIC_COLLISION, 80))
    sim.addToIncidentQueue(Incident(204, IncidentType.TRAFFIC_COLLISION, 71))
    sim.addToIncidentQueue(Incident(193, IncidentType.TRAFFIC_COLLISION, 81))
    sim.addToIncidentQueue(Incident(191, IncidentType.TRAFFIC_COLLISION, 118))
    sim.addToIncidentQueue(Incident(181, IncidentType.MURDER, 105))
    sim.addToIncidentQueue(Incident(179, IncidentType.WELLNESS_CHECK, 16))
    sim.addToIncidentQueue(Incident(171, IncidentType.WELLNESS_CHECK, 103))
    sim.addToIncidentQueue(Incident(158, IncidentType.TRAFFIC_COLLISION, 42))
    sim.addToIncidentQueue(Incident(125, IncidentType.TRAFFIC_COLLISION, 92))
    sim.addToIncidentQueue(Incident(121, IncidentType.WELLNESS_CHECK, 118))
    sim.addToIncidentQueue(Incident(117, IncidentType.TRAFFIC_COLLISION, 109))
    sim.addToIncidentQueue(Incident(96, IncidentType.ROBBERY, 64))
    sim.addToIncidentQueue(Incident(70, IncidentType.MURDER, 38))
    sim.addToIncidentQueue(Incident(53, IncidentType.MURDER, 24))
    sim.addToIncidentQueue(Incident(52, IncidentType.TRAFFIC_COLLISION, 61))
    sim.addToIncidentQueue(Incident(42, IncidentType.ROBBERY, 99))
    sim.addToIncidentQueue(Incident(41, IncidentType.TRAFFIC_COLLISION, 89))
    sim.addToIncidentQueue(Incident(28, IncidentType.TRAFFIC_COLLISION, 41))
    sim.addToIncidentQueue(Incident(25, IncidentType.TRAFFIC_COLLISION, 62))
    sim.addToIncidentQueue(Incident(16, IncidentType.MURDER, 58))
    sim.addToIncidentQueue(Incident(10, IncidentType.ROBBERY, 108))
            
    sim.run()




   
