import pandas

df = pandas.read_csv("hotels.csv")

class Hotel:
    def __init__(self, id):
        pass

    def book(self): # 'book' method
        pass

    def available(self): # 'available' method
        pass

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self): # 'generate' method
        content = f"Name of the customer hotel"
        return content

print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id) # create an instance of the object/class 'Hotel'
if hotel.available(): # calling the 'available' method
    hotel.book() # calling the 'book' method
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel) # create an instance of the object/class 'ReservationTicket'
    print(reservation_ticket.generate()) # calling the 'generate' method
else:
    print("Hotel is not available")