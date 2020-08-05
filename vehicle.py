"""
A named vehicle with a sequence of pings.
"""
from position import Position, get_distance
from ping import Ping, seconds_between

class Vehicle(object):

    def __init__(self, name, start=1):
        self.name = name
        self.pings = []
        self.start = start

    def get_name(self):
        """
        The name of the vehicle.
        """
        return self.name

    def get_pings(self):
        """
        The pings for the vehicle, in chronological order (earliest first).
        """
        return self.pings
    
    def set_start(self, x):
        """
        This function sets the starting index for the timestamp.
        """
        self.start = x
        

    def get_total_distance(self):
        """
        Determines the total distance traveled by the vehicle.
        """
        return self.calc_total_distance()

    def get_time_between_pings(self):
        """
        Determines the total distance traveled by the vehicle.
        """
        return self.calc_time_between_pings()

    def get_average_speed(self):
        """
        Determines the average speed of the vehicle.
        """
        return self.calc_average_speed()
    
    def get_acceleration(self):
        """
        Determines the acceleration of vehicle between two sets of pings.
        Calls the calc_speed_changes_between_pings function, which calculates the increase / decrease
        in speed between a set of pings. this is taken as the acceleration assuming the 
        speed changes occur in 1 time unit.
        """
        return self.calc_speed_changes_between_pings()

    def __str__(self):
        return self.name + ": " + self.pings

    def calc_distance_between_pings(self):
        """
        Calculates the distance covered between pings.
        """
        dist = []
        for i in range(self.start, len(self.pings)-1):
            position1 = self.pings[i].get_position()
            position2 = self.pings[i-1].get_position()
            dist.append(get_distance(position1, position2))
        return dist

    def calc_time_between_pings(self):
        """
        Calculates the time between two pings.
         This is used to calculate speed instances between pings.
        """
        time = []
        for i in range(self.start, len(self.pings)-1):
            time.append(seconds_between(self.pings[i-1], self.pings[i]))
        return time


    def calc_total_distance(self):
        """[This function calls the calc_distances function and 
        returns the sum of distances of each trip]
        """
        return sum(self.calc_distance_between_pings())


    def calc_average_speed(self):
        """
            Determines the average speed of the vehicle.
        """
        total_dist = self.calc_total_distance()
        total_time = sum(self.calc_time_between_pings())
        if total_time != 0:
            return '%.*f' % (2, total_dist/total_time)
        else:
            return None

    def calc_speed_changes_between_pings(self):
        """
            Determines the changes in speed between two sets of pings.
            This will be taken as acceleration, assuming the time for speed changes is 1 time unit.
        """
        dist = self.calc_distance_between_pings()
        time = self.calc_time_between_pings()
        speed_instances = []
        speed_changes_list = []
        for i in range(1, len(dist)-1):
            if time[i] != 0:
                speed_instances.append(dist[i]/time[i])
        for i in range(1, len(speed_instances)-1):
            speed_changes_list.append('%.*f' % (2, (speed_instances[i]-speed_instances[i-1])))
        return speed_changes_list
