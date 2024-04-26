def crossroads():
    green_light_duration = int(input())
    free_window_duration = int(input())

    total_cars_passed = 0
    cars_in_crossroads = []

    while True:
        command = input()

        if command == "END":
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
            break
        elif command == "green":
            # Process cars during green light and free window
            remaining_seconds = green_light_duration + free_window_duration
            while cars_in_crossroads and remaining_seconds > 0:
                car = cars_in_crossroads.pop(0)
                time_to_pass = len(car)
                if time_to_pass <= remaining_seconds:
                    total_cars_passed += 1
                    remaining_seconds -= time_to_pass
                else:
                    character_hit = car[remaining_seconds]
                    print("A crash happened!")
                    print(f"{car} was hit at {character_hit}.")
                    return  # Exit the function due to the crash
        else:
            # A car enters the queue
            cars_in_crossroads.append(command)


if __name__ == "__main__":
    crossroads()
