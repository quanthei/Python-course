drivers_names = ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
drivers_distance_from_client_in_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

def find_driver_most_closer_to_client(drivers_names_list: list, drivers_distance_list: list):
    # Find the more closer distance
    distance_min = drivers_distance_list[0]
    for distance in range(1, len(drivers_distance_list)):
        if drivers_distance_list[distance] < distance_min:
            distance_min = drivers_distance_list[distance]
            closest_driver = drivers_names_list[distance]  # fetch the corresponding driver
    return closest_driver, distance_min

driver_infos = find_driver_most_closer_to_client(drivers_names, drivers_distance_from_client_in_km)
print(f"{driver_infos[0]} se trouve à {driver_infos[1]}km") 