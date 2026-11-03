
class ParkingLot:
    """Manage vehicle parking and available parking slots."""

    total_slots = 5

    def __init__(self, parking_name):
        """Initialize the parking lot."""
        self.parking_name = parking_name
        self.parked_vehicles = []

    def park_vehicle(self, vehicle_number):
        """Park a vehicle if a slot is available."""
        if vehicle_number in self.parked_vehicles:
            print("This vehicle is already parked!")
        elif len(self.parked_vehicles) >= self.total_slots:
            print("Parking lot is full!")
        else:
            self.parked_vehicles.append(vehicle_number)
            print("Vehicle parked successfully!")

    def remove_vehicle(self, vehicle_number):
        """Remove a vehicle using its registration number."""
        if vehicle_number in self.parked_vehicles:
            self.parked_vehicles.remove(vehicle_number)
            print("Vehicle removed successfully!")
        else:
            print("Vehicle not found!")

    def show_available_slots(self):
        """Display the number of available parking slots."""
        available = self.total_slots - len(self.parked_vehicles)
        print(f"Available Slots: {available}")

    def display_vehicles(self):
        """Display all currently parked vehicles."""
        print("\nParked Vehicles:")
        if not self.parked_vehicles:
            print("No vehicles are currently parked.")
        else:
            for vehicle in self.parked_vehicles:
                print(vehicle)


def main():
    """Run the parking lot management system."""
    parking = ParkingLot("Smart Parking System")

    print(f"Welcome to {parking.parking_name}!")

    while True:
        print("\n1. Park Vehicle")
        print("2. Remove Vehicle")
        print("3. Show Available Slots")
        print("4. Display Parked Vehicles")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle = input("Enter vehicle number: ").strip().upper()
            if vehicle:
                parking.park_vehicle(vehicle)
            else:
                print("Vehicle number cannot be empty!")

        elif choice == "2":
            vehicle = input("Enter vehicle number to remove: ").strip().upper()
            parking.remove_vehicle(vehicle)

        elif choice == "3":
            parking.show_available_slots()

        elif choice == "4":
            parking.display_vehicles()

        elif choice == "5":
            print("Thank you for using Smart Parking System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
