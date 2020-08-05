import csv
from ping import Ping
from vehicle import Vehicle

class WarehouseServer(object):

    def __init__(self):
        # vehicles is a list of vehicle instances
        self.vehicles = []
        self.collision_car_list = []
        self.accident_map={}
        self.collision_details=[]

    def get_average_speeds(self):
        """
        Returns a dictionary from vehicle name to that vehicle's average speed
        for all vehicles.
        """
        avg_speeds = {}
        for vehicle in self.vehicles:
            avg_speeds[vehicle.get_name()] = vehicle.get_average_speed()  
        return avg_speeds

    def binary_search(self, ping_times, left, right, timestamp):
        '''
        This is a search function that uses the binary search algorithm.
        This function requires that array to be sorted.
        It returns the index value of a particular item in an array.
        It takes an array, left and right indices as boundaries for the search, and x - an item to search.
        '''
        if left <= right:
            mid = left + (right-left)//2
            if ping_times[mid] == timestamp:
                return mid
            elif ping_times[mid] < timestamp:
                return self.binary_search(ping_times, mid+1, right, timestamp)
            else:
                return self.binary_search(ping_times, left, mid-1, timestamp)
        else:
            return left + (right-left)//2
    
    def get_time_list(self):
        ping_times = []
        for vehicle in self.vehicles:
            ping_list = vehicle.pings
            for i in range(0, len(ping_list)-1):
                ping_times.append(ping_list[i].get_timestamp())
        return ping_times

    def get_most_traveled_since(self, max_results, timestamp):
        """
        Returns a sorted list of size max_results of vehicle names
        corresponding to the vehicles that have traveled the most distance since
        the given timestamp. # check binary heap.
        """
        total_dist = {}

        #Using Binary Search
        ping_times = self.get_time_list()
        for vehicle in self.vehicles:
            left = 0
            right = len(ping_times)
            index = self.binary_search(ping_times, left, right, timestamp)
            vehicle.set_start(index+1)
            
            # Using Python's Index Function
            # index = ping_times.index(timestamp, 0, len(ping_times)-1)
            # vehicle.set_start(index+1)
        
            # Using Linear Search
            # for i in range(0, len(ping_list)-1):
            #     time1 = ping_list[i].get_timestamp()
            #     if (time1-timestamp) > 0:
            #         vehicle.set_start(i)
            #         break

            total_dist[vehicle.get_name()] = vehicle.get_total_distance()
        sorted_total_dist = sorted(total_dist.items(), key= lambda x: x[1], reverse=True)
        return [sorted_total_dist[i] for i in range(max_results)]
    
    def check_for_collision(self):
        for vehicle in self.vehicles:
            ping_list = vehicle.pings
            for i in range(len(ping_list)):
                if str(ping_list[i]) in self.accident_map.keys():
                    print('Collision has Occurred')
                    if len(self.accident_map[str(ping_list[i])]) == 1:
                        self.collision_car_list.append(self.accident_map[str(ping_list[i])][0])
                    self.accident_map[str(ping_list[i])].append(vehicle.get_name())
                    self.collision_car_list.append(vehicle.get_name())
                else:
                    self.accident_map[str(ping_list[i])] = [vehicle.get_name()]

        for k,v in self.accident_map.items():
            if len(v)>1:
                self.collision_details.append(k)
        return(self.collision_details, self.collision_car_list)
        

    def check_for_damage(self):
        """
        Returns a list of names identifying vehicles that might have been damaged
        through any number of risky behaviors, including collision with another
        vehicle and excessive acceleration.
        """
        collision_details, collision_car_list = self.check_for_collision()
        vehicle_acceleration_list = {}
        high_acceleration_trip_count = {}
        for vehicle in self.vehicles:
            vehicle_acceleration_list[vehicle.get_name()] = vehicle.get_acceleration()
            for key, values in vehicle_acceleration_list.items():
                #Vehicle is flagged if it exceeds acceleration > 0.7 units/sec^2 is considered high speed
                high_acceleration_trip_count[key]=len([abs(float(value)) for value in values if abs(float(value)) > 0.5])
        high_accelerated_trip_count_sorted = sorted(high_acceleration_trip_count.items(), key= lambda x: x[1], reverse=True)
        most_travelled_vehicle = self.get_most_traveled_since(1, 0)
        return [collision_details, collision_car_list, high_accelerated_trip_count_sorted, most_travelled_vehicle]


    def initialize_server(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for parsed_line in reader:
                self.process_ping(
                            parsed_line[0],
                            float(parsed_line[1]),
                            float(parsed_line[2]),
                            int(parsed_line[3]))

    def process_ping(self, vehicle_name, x, y, timestamp):
        ping = Ping(x, y, timestamp)
        if len(self.vehicles) == 0 or vehicle_name != self.vehicles[-1].get_name():
            self.vehicles.append(Vehicle(vehicle_name))
        self.vehicles[-1].get_pings().append(ping)
        # if len(self.timestamps) == 0 or timestamp != self.timestamps[-1].get_name():
        #     self.vehicles.append(Vehicle(vehicle_name))
