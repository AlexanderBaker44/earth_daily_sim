import numpy as np

class Satellite:

    def __init__(self,
                payload_perc,
                payload_del_min,payload_del_mid,payload_del_max,
                bus_perc,
                bus_del_min,bus_del_mid,bus_del_max,
                space_perc,
                space_del_min,space_del_mid,space_del_max,
                nlt_thresh
                ):

        self.internal_clock = 0

        self.payload_perc = payload_perc
        self.payload_del_min = payload_del_min
        self.payload_del_mid = payload_del_mid
        self.payload_del_max = payload_del_max

        self.bus_perc = bus_perc
        self.bus_del_min = bus_del_min
        self.bus_del_mid = bus_del_mid
        self.bus_del_max = bus_del_max

        self.space_perc = space_perc
        self.space_del_min = space_del_min
        self.space_del_mid = space_del_mid
        self.space_del_max = space_del_max

        self.nlt_thresh = nlt_thresh

    def payload(self):
        payload_val = np.random.uniform(0,1)
        if payload_val <= self.payload_perc:
            self.internal_clock += int(np.random.triangular(self.payload_del_min,self.payload_del_mid,self.payload_del_max))

    def bus(self):
        bus_val = np.random.uniform(0,1)
        if bus_val <= self.bus_perc:
            self.internal_clock += int(np.random.triangular(self.bus_del_min,self.bus_del_mid,self.bus_del_max))


    def space_craft(self):
        space_val = np.random.uniform(0,1)
        if space_val <= self.space_perc:
            self.internal_clock += int(np.random.triangular(self.space_del_min,self.space_del_mid,self.space_del_max))

    def operate(self):
        self.payload()
        self.bus()
        self.space_craft()
