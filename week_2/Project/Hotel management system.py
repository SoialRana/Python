class Room:
    def __init__(self,nunber,capacity,price) -> None:
        self.number=nunber
        self.capacity=capacity
        self.price=price
        self.is_occupied=False

class Hotel:
    def __init__(self,name) -> None:
        self.name=name
        self.rooms=[]

    def add_room(self,room):
        self.rooms.append(room)
        print(f'Room number {room.number} is added succesfully')

    def remove_room(self,room):
        if room in self.rooms:
            self.rooms.remove(room)
            print(f'Room {room.number} is removed from the hotel')
        else:
            print(f'Roome {room.number} is not available in the hotel')

    def check_in(self,room):
        if not room.is_occupied:
            room.is_occupied=True
            print(f'Check into room {room.number}')
        else:
            print(f'Room {room.number} is already occupied')

    def check_out(self,room):
        if room.is_occupied:
            room.is_occupied=False
            print(f'Roome number {room.number} is check Out')
        else:
            print(f'Romm {room.number} is not occupied')


    def search_available_room(self,capacity,max_price):
        available_rooms=[]
        for room in self.rooms:
            if room.capacity>=capacity and room.price<=max_price and not room.is_occupied:
                available_rooms.append(room)
        if available_rooms:
            print('Available rooms are:')
            for room in available_rooms:
                print(f'Room: {room.number} Capacity: {room.capacity} Price:{room.price}')
        else:
            print('No available room is matching for this criteria')


    def display_all_rooms(self):
        print('All room are here in the hotel')
        for room in self.rooms:
            status='Occupied' if room.is_occupied else 'Available'
            print(f'Room : {room.number} Capacity : {room.capacity} Price : {room.price}')


# create object for Room 
room1=Room(101,2,3000)
room2=Room(102,2,2000)
room3=Room(103,4,5000)

#create object for hotel
hotel=Hotel('My hotel')

# Add rooom in the hotel
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

#Display all rooms in the hotel
hotel.display_all_rooms()

#search for available room
hotel.search_available_room(4,5000)


#check into a room 
hotel.check_in(room1)
hotel.check_in(room2)
hotel.check_in(room3)

# Check-out a room
hotel.check_out(room1)
hotel.check_out(room2)

# romove a room from the hotel 
hotel.remove_room(room2)

#Display all rooms in the hotel
hotel.display_all_rooms()
