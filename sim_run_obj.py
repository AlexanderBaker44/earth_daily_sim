import numpy as np
from sat_obj import Satellite
from constel_obj import Constellation
from scenario_obj import Scenario

class SimulationRun:
    def __init__(self, const_params, scenario_params,nlt_thresh):
        self.const_params = const_params
        self.scenario_params = scenario_params
        self.nlt_thresh = nlt_thresh

    def constellation_run(self):
        const_obj = Constellation(self.const_params)
        const_obj.instan_const()
        sat_delays = const_obj.satel_const_delay()
        nlt_vals = const_obj.nlt_delay(self.nlt_thresh)
        return nlt_vals,sat_delays

    def scenario_run(self,nlt_vals):

        scenario = Scenario(
                    self.scenario_params[0],
                    self.scenario_params[1],
                    self.scenario_params[2],
                    self.scenario_params[3],
                    self.scenario_params[4],
                    self.scenario_params[5],
                    self.scenario_params[6],
                    self.scenario_params[7],
                    self.scenario_params[8],
                    self.scenario_params[9],
                    self.scenario_params[10],
                    self.scenario_params[11],
                    self.scenario_params[12],
                    self.scenario_params[13],
                    self.scenario_params[14],
                    self.scenario_params[15],
                    self.scenario_params[16],
                    self.scenario_params[17],
                    self.scenario_params[18],
                    self.scenario_params[19]
                   )



        scenario_delays,scenario_results = scenario.run_events(nlt_vals)
        return scenario_delays,scenario_results

    def run_sim(self):

        nlt_vals,sat_delays = self.constellation_run()
        event_delays,scenario_results = self.scenario_run(nlt_vals)

        return nlt_vals,sat_delays,event_delays,scenario_results
