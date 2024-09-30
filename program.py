from datetime import datetime

class Customer:
    def __init__(self, name, email, phone, credit_card_info):
        self.name = name
        self.email = email
        self.phone = phone
        self.credit_card_info = credit_card_info

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_credit_card_info(self):
        return self.credit_card_info

class Room:
    def __init__(self, room_number, room_type, bed_type, smoking_allowed, rate_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.bed_type = bed_type
        self.smoking_allowed = smoking_allowed
        self.rate_per_night = rate_per_night

    def get_room_number(self):
        return self.room_number

    def get_room_type(self):
        return self.room_type

    def get_bed_type(self):
        return self.bed_type

    def get_smoking_allowed(self):
        return self.smoking_allowed

    def get_rate_per_night(self):
        return self.rate_per_night

class Reservation:
    def __init__(self, reservation_number, confirmation_number, customer, room, check_in_date, check_out_date):
        self.reservation_number = reservation_number
        self.confirmation_number = confirmation_number
        self.customer = customer
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_nights = (check_out_date - check_in_date).days
        self.total_cost = self.total_nights * room.get_rate_per_night()

    def get_reservation_number(self):
        return self.reservation_number

    def get_confirmation_number(self):
        return self.confirmation_number

    def get_customer(self):
        return self.customer

    def get_room(self):
        return self.room

    def get_check_in_date(self):
        return self.check_in_date

    def get_check_out_date(self):
        return self.check_out_date

    def get_total_nights(self):
        return self.total_nights

    def get_total_cost(self):
        return self.total_cost

class Hotel:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

# Create customer
customer = Customer("Hamad Almarri", "hamad.almarri@example.com", "555-5678", "Mastercard (ending in 9904)")

# Create room
room = Room(101, "2 Queen Beds", "No Smoking Desk/Safe Coffee Maker in Room Hair Dryer", False, 89.55)

# Create hotel
hotel = Hotel("Comfort Inn & Suites Los Alamos", "2455 Trinity Drive, Los Alamos, NM 87544", "505-661-1110")

# Create reservation
reservation_number = "15549850358"
confirmation_number = "52523687"
check_in_date = datetime(2010, 8, 22, 15, 0)  
check_out_date = datetime(2010, 8, 24, 12, 0)  

reservation = Reservation(reservation_number, confirmation_number, customer, room, check_in_date, check_out_date)

# Display reservation details
print("Your Reservation Is Confirmed")
print("Thank you for your reservation. Please print your hotel receipt and show it at check-in.")
print()
print("Your Name:", customer.get_name())
print("Your Email:", customer.get_email())
print("Priceline Trip Number:", reservation.get_reservation_number())
print("Hotel Confirmation Number:", reservation.get_confirmation_number())
print()
print(hotel.get_name())
print(hotel.get_address())
print("Phone:", hotel.get_phone())
print("Check-In:", reservation.get_check_in_date())
print("Check-Out:", reservation.get_check_out_date())
print("Number of Nights:", reservation.get_total_nights())
print("Number of Rooms: 1")
print()
print("Room 1:", customer.get_name())
print("Room Type:", room.get_room_type())
print("Bed Type:", room.get_bed_type())

# Determine smoking status
if room.get_smoking_allowed() == True:
    smoking_status = "Smoking"
else:
    smoking_status = "No Smoking"

print("Smoking Allowed:", smoking_status)
print()
print("Summary of Charges")
print()
print("Billing Name:", customer.get_name())
print("Credit Card:", customer.get_credit_card_info())
print()
print("Room Cost: $", room.get_rate_per_night(), "per room, per night")
print("Rooms: 1")
print("Nights:", reservation.get_total_nights())
room_subtotal = reservation.get_total_cost()
print("Room Subtotal: $", room_subtotal)
print()
taxes_and_fees = 21.58
print("Taxes and Fees: $", taxes_and_fees)
print()
total_charges = room_subtotal + taxes_and_fees
print("Total Charges: $", total_charges)
