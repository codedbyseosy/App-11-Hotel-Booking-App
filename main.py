import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str}) # dtype loads all the values in the id col as strings


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id # 'self.hotel_id' is a property and 'hotel_id' is an instance variable
        self.name =  df.loc[df["id"] == self.hotel_id, "name"].squeeze() # get corresponding name for each id

    def book(self): 
        """This method books a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = 'no' # change field from 'yes' to 'no'
        df.to_csv("hotels.csv", index=False) # overwrite the current csv file with the new changes

    def available(self): 
        """This method checks if the hotel is available"""
        availabilty = df.loc[df["id"] == self.hotel_id, "available"].squeeze() # return the 'available' field that corresponds to the entered 'id' field
        if availabilty == "yes":
            return True
        else:
            return False
    

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name # 'self.customer_name' is a property and 'customer_name' is an instance variable
        self.hotel = hotel_object # 'self.hotel' is a property and 'hotel_object' is an instance variable


    def generate(self): # 'generate' method
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
"""
        return content

print("Hi there! Please see the list of our hotels and their availbility status below")
print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID) # create an instance of the object/class 'Hotel'

if hotel.available(): # calling the 'available' method, if hotel.available returns 'True'
    hotel.book() # calling the 'book' method
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel) # create an instance of the object/class 'ReservationTicket'
    print(reservation_ticket.generate()) # calling the 'generate' method
else:
    print("Hotel is not available")