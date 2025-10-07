from collections import deque

# Node class for Linked List
class PassengerNode:
    def __init__(self, name, age, gender, train_no, seat_pref):
        self.name = name
        self.age = age
        self.gender = gender
        self.train_no = train_no
        self.seat_pref = seat_pref
        self.next = None

# Railway Reservation System
class RailwayReservationSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.head = None  # Head of linked list (booked passengers)
        self.waiting_list = deque()  # Queue for waiting passengers

    # Function to add passenger
    def add_passenger(self, name, age, gender, train_no, seat_pref):
        if self.available_seats > 0:
            # Book ticket directly (add to linked list)
            new_node = PassengerNode(name, age, gender, train_no, seat_pref)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

            self.available_seats -= 1
            print(f"Ticket booked for {name}. Seat allocated successfully!")
        else:
            # No seats → Add to waiting list
            self.waiting_list.append((name, age, gender, train_no, seat_pref))
            print(f"No seats available. {name} added to waiting list.")

    # Function to cancel ticket
    def cancel_ticket(self, name):
        if self.head is None:
            print("No bookings to cancel.")
            return

        temp = self.head
        prev = None

        # Search for the passenger in linked list
        while temp and temp.name != name:
            prev = temp
            temp = temp.next

        # Passenger not found
        if temp is None:
            print(f"No booking found under name: {name}")
            return

        # Passenger found → remove from linked list
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next

        print(f"Ticket cancelled for {name}.")
        self.available_seats += 1

        # Allocate seat to first waiting passenger (if any)
        if self.waiting_list:
            next_person = self.waiting_list.popleft()
            self.add_passenger(*next_person)
            print(f"Seat allocated to {next_person[0]} from waiting list.")

    # Function to display booked passengers
    def display_booked(self):
        if self.head is None:
            print("No confirmed bookings yet.")
            return

        print("\n--- Confirmed Bookings ---")
        temp = self.head
        count = 1
        while temp:
            print(f"{count}. Name: {temp.name}, Age: {temp.age}, Gender: {temp.gender}, "
                  f"Train No: {temp.train_no}, Seat Pref: {temp.seat_pref}")
            temp = temp.next
            count += 1
        print(f"Available Seats: {self.available_seats}/{self.total_seats}")

    # Function to display waiting list
    def display_waiting(self):
        if not self.waiting_list:
            print("Waiting list is empty.")
            return

        print("\n--- Waiting List ---")
        for i, person in enumerate(self.waiting_list, start=1):
            print(f"{i}. Name: {person[0]}, Age: {person[1]}, Gender: {person[2]}, "
                  f"Train No: {person[3]}, Seat Pref: {person[4]}")


# Main Menu Driven Program

def main():
    print("Welcome to Railway Reservation System")
    total_seats = int(input("Enter total number of seats available: "))
    system = RailwayReservationSystem(total_seats)

    while True:
        print("\n===== MENU =====")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Display Booked Tickets")
        print("4. Display Waiting List")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter passenger name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            train_no = input("Enter train number: ")
            seat_pref = input("Enter seat preference (Window/Middle/Aisle): ")
            system.add_passenger(name, age, gender, train_no, seat_pref)

        elif choice == '2':
            name = input("Enter passenger name to cancel: ")
            system.cancel_ticket(name)

        elif choice == '3':
            system.display_booked()

        elif choice == '4':
            system.display_waiting()

        elif choice == '5':
            print("Thank you for using Railway Reservation System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
