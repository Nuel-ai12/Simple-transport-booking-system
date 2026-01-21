transport_bookings = []

def book_transport():
    passenger = input("Enter passenger name: ")
    route = input("Enter route: ")
    transport_bookings.append({"passenger": passenger, "route": route})
    print("Transport booked successfully")

def view_bookings():
    if not transport_bookings:
        print("No bookings available")
    else:
        for booking in transport_bookings:
            print(booking["passenger"], "- Route:", booking["route"])

def main():
    while True:
        print("1. Book Transport")
        print("2. View Bookings")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_transport()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
