from datetime import datetime

class Customer:
    def __init__(self, name="", email="", phone="", credit_card_info=""):
        self.__name = ""
        self.__email = ""
        self.__phone = ""
        self.__credit_card_info = ""
        self.__reservations = []

    # Getter and Setter methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_credit_card_info(self):
        return self.__credit_card_info

    def set_credit_card_info(self, info):
        self.__credit_card_info = info

    def add_reservation(self, reservation):
        self.__reservations.append(reservation)

    def get_reservations(self):
        return self.__reservations

    # Enter Personal Details
    def enter_personal_details(self):
        # Set personal details directly
        self.set_name("Hamad Almarri")
        self.set_email("hamad.almarri@example.com")
        self.set_phone("555-5678")
        self.set_credit_card_info("Mastercard (ending in 9904)")

    # Make Reservation
    def make_reservation(self, hotel):
        # Search for Available Rooms
        available_rooms = hotel.search_available_rooms()
        if len(available_rooms) == 0:
            print("No rooms available for the selected dates.")
            return None
        # Select the first available room
        room = available_rooms[0]
        # Enter Personal Details
        self.enter_personal_details()
        # Create reservation
        reservation_number = "15549850358"
        check_in_date = datetime(2010, 8, 22, 15, 0)
        check_out_date = datetime(2010, 8, 24, 12, 0)
        reservation = Reservation(reservation_number, self, room, check_in_date, check_out_date)
        # Process Payment
        amount = reservation.calculate_total_cost()
        payment = Payment("GeneratedPaymentID", amount, self.get_credit_card_info(), datetime.now())
        payment.process_payment()
        # Receive Confirmation
        reservation.generate_confirmation()
        self.add_reservation(reservation)
        print("Reservation made successfully!")
        return reservation

class Room:
    def __init__(self, room_number, room_type, bed_type, smoking_allowed, rate_per_night):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__bed_type = bed_type
        self.__smoking_allowed = smoking_allowed
        self.__rate_per_night = rate_per_night
        self.__availability = True

    # Getter and Setter methods
    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_bed_type(self):
        return self.__bed_type

    def set_bed_type(self, bed_type):
        self.__bed_type = bed_type

    def get_smoking_allowed(self):
        return self.__smoking_allowed

    def set_smoking_allowed(self, smoking_allowed):
        self.__smoking_allowed = smoking_allowed

    def get_rate_per_night(self):
        return self.__rate_per_night

    def set_rate_per_night(self, rate_per_night):
        self.__rate_per_night = rate_per_night

    def check_availability(self):
        return self.__availability

    def reserve(self):
        self.__availability = False

    def release(self):
        self.__availability = True

class Reservation:
    def __init__(self, reservation_number, customer, room, check_in_date, check_out_date):
        self.__reservation_number = reservation_number
        self.__customer = customer
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__total_nights = (check_out_date - check_in_date).days
        self.__total_cost = 0.0
        self.__confirmation_number = ""

    # Getter and Setter methods
    def get_reservation_number(self):
        return self.__reservation_number

    def set_reservation_number(self, reservation_number):
        self.__reservation_number = reservation_number

    def get_customer(self):
        return self.__customer

    def set_customer(self, customer):
        self.__customer = customer

    def get_room(self):
        return self.__room

    def set_room(self, room):
        self.__room = room

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, date):
        self.__check_in_date = date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, date):
        self.__check_out_date = date

    def get_total_nights(self):
        return self.__total_nights

    def calculate_total_cost(self):
        self.__total_cost = self.__total_nights * self.__room.get_rate_per_night()
        return self.__total_cost

    def get_total_cost(self):
        return self.__total_cost

    # Receive Confirmation
    def generate_confirmation(self):
        self.__confirmation_number = "52523687"
        print("Confirmation sent to", self.__customer.get_email())

    def get_confirmation_number(self):
        return self.__confirmation_number

class Payment:
    def __init__(self, payment_id, amount, payment_method, payment_date):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__payment_method = payment_method
        self.__payment_date = payment_date

    # Getter and Setter methods
    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, method):
        self.__payment_method = method

    def get_payment_date(self):
        return self.__payment_date

    def set_payment_date(self, date):
        self.__payment_date = date

    # Process Payment
    def process_payment(self):
        print("Processing payment of $", self.__amount, "using", self.__payment_method)
        print("Payment processed successfully.")

class Hotel:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__rooms = []

    # Getter and Setter methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def add_room(self, room):
        self.__rooms.append(room)

    def search_available_rooms(self):
        available_rooms = []
        for room in self.__rooms:
            if room.check_availability():
                available_rooms.append(room)
        return available_rooms

# Create hotel
hotel = Hotel("Comfort Inn & Suites Los Alamos", "2455 Trinity Drive, Los Alamos, NM 87544", "505-661-1110")

# Create room and add to hotel
room = Room(101, "2 Queen Beds", "No Smoking Desk/Safe Coffee Maker in Room Hair Dryer", False, 89.55)
hotel.add_room(room)

# Create customer
customer = Customer()

# Customer makes a reservation
reservation = customer.make_reservation(hotel)

# Display reservation details
print()
print("Your Reservation Is Confirmed")
print("Thank you for your reservation. Please print your hotel receipt and show it at check-in.")
print("Your Name:", customer.get_name())
print("Your Email:", customer.get_email())
print("Priceline Trip Number:", reservation.get_reservation_number())
print("Hotel Confirmation Number:", reservation.get_confirmation_number())
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
if room.get_smoking_allowed():
    smoking_status = "Smoking"
else:
    smoking_status = "No Smoking"
print("Smoking Allowed:", smoking_status)
print("Summary of Charges")
print("Billing Name:", customer.get_name())
print("Credit Card:", customer.get_credit_card_info())
print("Room Cost: $", room.get_rate_per_night(), "per room, per night")
print("Rooms: 1")
print("Nights:", reservation.get_total_nights())
room_subtotal = reservation.calculate_total_cost()
print("Room Subtotal: $", room_subtotal)
taxes_and_fees = 21.58
print("Taxes and Fees: $", taxes_and_fees)
total_charges = room_subtotal + taxes_and_fees
print("Total Charges: $", total_charges)
