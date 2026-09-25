#vacuum cleaner
room_a=input("Room A: ")
room_b=input("Room B: ")
current_room="A"
while room_a == "dirty" or room_b == "dirty":
    print("Current room: A")
    if room_a == "dirty":
        print("Cleaning Room A in progress")
        print("Room A is clean")
        room_a = "clean"
    if room_b == "dirty":
        print("Moving to Room B")
        print("Cleaning Room B in progress")
        print("Room B is clean")
        room_b = "clean"
    
print("Both rooms are clean")
