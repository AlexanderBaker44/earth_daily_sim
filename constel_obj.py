from sat_obj import Satellite

class Constellation:
    def __init__(self,const_params):
        self.const_clock = []
        self.const_params = const_params

    def instan_const(self):
        sat_const = []
        for o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13 in self.const_params:
            satellite = Satellite(o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13)
            sat_const.append(satellite)
        return sat_const

    def satel_const_delay(self):
        self.delay_thresh = []

        sat_const = self.instan_const()
        for i in sat_const:
            i.operate()
            full_sat_delay = i.internal_clock
            nlt_val = i.nlt_thresh
            self.delay_thresh.append(nlt_val+i.internal_clock)
            self.const_clock.append(full_sat_delay)
        return self.delay_thresh


    def nlt_delay(self,nlt_thresh):
        nlt_stats = []
        for nlt_val in self.delay_thresh:
            if nlt_thresh >= nlt_val:
                nlt_stats.append(True)
            else:
                nlt_stats.append(False)
        return nlt_stats
