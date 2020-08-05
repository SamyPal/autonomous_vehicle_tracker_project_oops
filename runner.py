from warehouse_server import WarehouseServer


def main():
    # Initialize WarehouseServer instance.
    warehouse_server = WarehouseServer()
    warehouse_server.initialize_server("warehouse_pings.csv")
    print("~~~WarehouseServer is initialized.")
    print("")

    print("Average Speeds: " + str(warehouse_server.get_average_speeds()))
    print("The Vehicle M has not travelled, since installation of tracking device.")
    print("")

    print("The 3 most traveled vehicles since 1553273158 are: ")
    print(warehouse_server.get_most_traveled_since(3, 1553273158))
    print("")

    print("Vehicles possibly damaged: ")

    possibly_damaged_vehicle = warehouse_server.check_for_damage()
    print(f"Vehicle Collision History:")
    print(f"Vehicles involved in collision: {possibly_damaged_vehicle[1]}")
    print(f"Vehicles collision details [location(x,y) @ timestamp]: {possibly_damaged_vehicle[0]}")
    print(f"Most travelled vehicle [vehicle name, distance]{possibly_damaged_vehicle[3]}")
    print(f"Count of vehicles accelerated > 0.5 dist/time^2 units [vehicle name, count]{possibly_damaged_vehicle[2]}")
    
    # Feel free to put any print statements below for testing and debugging
    print("")
    print(f"NOTE: Position of Vehicle C at timestamp 1553273156 was modified to test for collision scenario")


if (__name__ == "__main__"):
    main()
