import time

class DomoticHouse:
    def __init__(self):
        self.door_open = False
        self.sprinkler_on = False
        self.lights = {
            "Living Room": False,
            "Kitchen": False,
            "Bathroom": False,
            "Bedroom 1": False,
            "Bedroom 2": False,
            "Bedroom 3": False
        }

    # Accés a la porta 
    def open_door(self):
        if self.door_open:
            print(" Door is already open.")
        else:
            self.door_open = True
            print(" Door opened successfully.")

    def close_door(self):
        if not self.door_open:
            print(" Door is already closed.")
        else:
            self.door_open = False
            print(" Door closed successfully.")

    def show_door_state(self):
        state = "OPEN" if self.door_open else "CLOSED"
        print(f" Door state: {state}")

    # Controlador del aspersor
    def turn_on_sprinkler(self):
        if self.sprinkler_on:
            print(" Sprinkler is already ON.")
        else:
            self.sprinkler_on = True
            print(" Sprinkler turned ON manually.")

    def turn_off_sprinkler(self):
        if not self.sprinkler_on:
            print(" Sprinkler is already OFF.")
        else:
            self.sprinkler_on = False
            print(" Sprinkler turned OFF manually.")

    # Aspersor format de les 9:00 AM
    def simulate_automatic_sprinkler(self):
        print(" It's 9:00 AM. Sprinkler activating automatically for 1 hour..")
        self.sprinkler_on = True
        self.show_sprinkler_state()
        time.sleep(2)
        self.sprinkler_on = False
        print(" One hour passed. Sprinkler turned OFF automatically.")
        self.show_sprinkler_state()

    def show_sprinkler_state(self):
        state = "ON" if self.sprinkler_on else "OFF"
        print(f" Sprinkler state: {state}")

    # Control de llums
    def control_room_light(self, room, state):
        """Turn on/off light for an specific room."""
        if room not in self.lights:
            print(" Invalid room name.")
            return
        current_state = self.lights[room]
        if state == "on":
            if current_state:
                print(f" {room} light is already ON.")
            else:
                self.lights[room] = True
                print(f" {room}: Light turned ON successfully.")
        elif state == "off":
            if not current_state:
                print(f" {room} light is already OFF.")
            else:
                self.lights[room] = False
                print(f" {room}: Light turned OFF successfully.")
        else:
            print(" Invalid state. Use 'on' or 'off'.")

    def control_all_lights(self, state):
        """Turn on/off all lights."""
        if state == "on":
            for room in self.lights:
                self.lights[room] = True
            print(" All room lights turned ON successfully.")
        elif state == "off":
            for room in self.lights:
                self.lights[room] = False
            print(" All room lights turned OFF successfully.")
        else:
            print(" Invalid state. Use 'on' or 'off'.")

    def show_all_lights(self):
        print("\n LIGHTS STATUS:")
        for room, state in self.lights.items():
            print(f"  {room}: {'ON' if state else 'OFF'}")


# MENU
def main_menu():
    house = DomoticHouse()
    while True:
        print("\n MENU")
        print("1. Door control")
        print("2. Sprinkler control")
        print("3. Lights control")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                door_menu(house)
            elif choice == 2:
                sprinkler_menu(house)
            elif choice == 3:
                lights_menu(house)
            elif choice == 4:
                print(" Exiting system.")
                break
            else:
                print(" Invalid option. Try again.")
        except ValueError:
            print(" Please enter a number (1–4).")

    # Porta sub-menu
def door_menu(house):
    while True:
        print("\n DOOR CONTROL")
        print("1. Open door")
        print("2. Close door")
        print("3. Show door state")
        print("4. Back to main menu")
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                house.open_door()
            elif option == 2:
                house.close_door()
            elif option == 3:
                house.show_door_state()
            elif option == 4:
                break
            else:
                print(" Invalid option.")
        except ValueError:
            print(" Enter a valid number.")

    # Aspersor sub-menu
def sprinkler_menu(house):
    while True:
        print("\n SPRINKLER CONTROL")
        print("1. Turn ON manually")
        print("2. Turn OFF manually")
        print("3. Simulate 9:00 automatic activation")
        print("4. Show sprinkler state")
        print("5. Back to main menu")
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                house.turn_on_sprinkler()
            elif option == 2:
                house.turn_off_sprinkler()
            elif option == 3:
                house.simulate_automatic_sprinkler()
            elif option == 4:
                house.show_sprinkler_state()
            elif option == 5:
                break
            else:
                print(" Invalid option.")
        except ValueError:
            print(" Enter a valid number.")

    # Llums sub-menu
def lights_menu(house):
    while True:
        print("\n LIGHTS CONTROL")
        print("1. Control a specific room")
        print("2. Control all rooms")
        print("3. Show state of all lights")
        print("4. Back to main menu")

        try:
            option = int(input("Choose an option: "))
            if option == 1:
                print("Available rooms: Living Room, Kitchen, Bathroom, Bedroom 1, Bedroom 2, Bedroom 3")
                room = input("Enter the room name exactly as shown: ")
                state = input("Turn light 'on' or 'off': ").lower()
                house.control_room_light(room, state)
            elif option == 2:
                state = input("Turn all lights 'on' or 'off': ").lower()
                house.control_all_lights(state)
            elif option == 3:
                house.show_all_lights()
            elif option == 4:
                break
            else:
                print(" Invalid option.")
        except ValueError:
            print(" Enter a valid number.")

if __name__ == "__main__":
    main_menu()
