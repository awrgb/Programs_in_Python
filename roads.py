import random
import time

def loading():
    print("Loading...")
    time.sleep(2)

def print_traffic_data():
    for road, (road_name, traffic) in roads_traffic.items():
        print(f"{road_name}: {traffic}")

def update_traffic_light(user_input, selected_roads):
    if user_input == 'green':
        print("Traffic lights switched to GREEN for selected roads:", ', '.join(selected_roads))
        for road in selected_roads:
            roads_traffic[road] = (roads_traffic[road][0], 0)
    elif user_input == 'red':
        print("Traffic lights switched to RED for selected roads:", ', '.join(selected_roads))
        for road in selected_roads:
            roads_traffic[road] = (roads_traffic[road][0], 100)
    else:
        print("Invalid input. Please select 'green' or 'red'.")

def main():
    loading()
    while True:
        print_traffic_data()
        user_input = input("Select the traffic lights (green/red) or type 'exit' to quit: ").lower()
        if user_input == 'exit':
            print("Exiting program.")
            break
        elif user_input in ['green', 'red']:
            selected_roads = []
            while True:
                road_input = input("Enter the road name or type 'done' to finish selecting roads: ").capitalize()
                if road_input == 'Done':
                    break
                elif road_input in roads_traffic:
                    selected_roads.append(road_input)
                else:
                    print("Invalid road name.")
            if selected_roads:
                update_traffic_light(user_input, selected_roads)
            else:
                print("No roads selected.")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    roads_traffic = {
        "East": ("East Road Traffic", random.randint(1, 100)),
        "West": ("West Road Traffic", random.randint(1, 100)),
        "North": ("North Road Traffic", random.randint(1, 100)),
        "South": ("South Road Traffic", random.randint(1, 100))
    }
    main()
