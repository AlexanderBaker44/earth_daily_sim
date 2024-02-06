import numpy as np

class Scenario:

    def __init__(self,
                ride_share_perc,
                ride_share_del_min,ride_share_del_mid,ride_share_del_max,
                launch_one_perc,
                launch_one_del_min,launch_one_del_mid,launch_one_del_max,
                launch_two_perc,
                launch_two_del_min,launch_two_del_mid,launch_two_del_max,
                initialization_perc_one,
                initialization_del_one_min,initialization_del_one_mid,initialization_del_one_max,
                initialization_perc_two,
                initialization_del_two_min,initialization_del_two_mid,initialization_del_two_max
                ):


        self.ride_share_perc = ride_share_perc
        self.ride_share_del_min = ride_share_del_min
        self.ride_share_del_mid = ride_share_del_mid
        self.ride_share_del_max = ride_share_del_max

        self.launch_one_perc = launch_one_perc
        self.launch_one_del_min = launch_one_del_min
        self.launch_one_del_mid = launch_one_del_mid
        self.launch_one_del_max = launch_one_del_max

        self.launch_two_perc = launch_two_perc
        self.launch_two_del_min = launch_two_del_min
        self.launch_two_del_mid = launch_two_del_mid
        self.launch_two_del_max = launch_two_del_max

        self.initialization_perc_one = initialization_perc_one
        self.initialization_del_one_min = initialization_del_one_min
        self.initialization_del_one_mid = initialization_del_one_mid
        self.initialization_del_one_max = initialization_del_one_max


        self.initialization_perc_two = initialization_perc_two
        self.initialization_del_two_min = initialization_del_two_min
        self.initialization_del_two_mid = initialization_del_two_mid
        self.initialization_del_two_max = initialization_del_two_max

        self.event_clock = 0


    def rideshare(self):
        ride_val = np.random.uniform(0,1)
        if ride_val <= self.ride_share_perc:
            delay=int(np.random.triangular(self.ride_share_del_min,self.ride_share_del_mid,self.ride_share_del_max))
        else:
            delay = 0
        return delay


    def launch(self,launch_perc,launch_del_min,launch_del_mid,launch_del_max):
        launch_val = np.random.uniform(0,1)
        if launch_val <= launch_perc:
            delay = int(np.random.triangular(launch_del_min,launch_del_mid,launch_del_max))
        else:
            delay = 0
        return delay


    def initialization(self,init_perc,init_del_min,init_del_mid,init_del_max):
        init_val = np.random.uniform(0,1)
        if init_val <= init_perc:
            delay = int(np.random.triangular(init_del_min,init_del_mid,init_del_max))
        else:
            delay = 0
        return delay




    def run_events(self, nlt_stats):
        sat_scenarios = []
        ride_delay = self.rideshare()

        launch_1_delay = self.launch(self.launch_one_perc,self.launch_one_del_min,self.launch_one_del_mid,self.launch_one_del_max)
        init_1_delay =self.initialization(self.initialization_perc_one,self.initialization_del_one_min,self.initialization_del_one_mid,self.initialization_del_one_max)

        total_1 = ride_delay + launch_1_delay + init_1_delay

        launch_2_delay = self.launch(self.launch_two_perc,self.launch_two_del_min,self.launch_two_del_mid,self.launch_two_del_max)
        init_2_delay = self.initialization(self.initialization_perc_two,self.initialization_del_two_min,self.initialization_del_two_mid,self.initialization_del_two_max)

        total_2 = ride_delay + launch_2_delay + init_2_delay
        scenario_results = [total_1,total_2]

        for nlt_stat in nlt_stats:

            if nlt_stat == True:
                sat_scenarios.append(total_1)
            else:
                sat_scenarios.append(total_2)
        return sat_scenarios, scenario_results
