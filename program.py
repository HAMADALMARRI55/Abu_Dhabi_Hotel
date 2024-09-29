from datetime import datetime

class Customer:
    def __init__(self, name="", email="", phone="", credit_card_info=""):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__credit_card_info = credit_card_info
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

    # Include: Enter Personal Details
    def enter_personal_details(self):
        """
        Collects personal details from the customer.
        """
        self.__name = input("Enter your full name: ")
        self.__email = input("Enter your email: ")
        self.__phone = input("Enter your phone number: ")
        self.__credit_card_info = input("Enter your credit card info: ")

    # Extends: Make Reservation
    def make_reservation(self, hotel):
        """
        Allows the customer to make a reservation.
        Extends the search for available rooms.
        """
        # Extends: Search for Available Rooms
        available_rooms = hotel.search_available_rooms()
        if not available_rooms:
            print("No rooms available for the selected dates.")
            return
        # For simplicity, select the first available room
        room = available_rooms[0]
        # Include: Enter Personal Details
        self.enter_personal_details()
        # Create reservation
        reservation_number = "15549850358"  # Example reservation number
        check_in_date = datetime(2010, 8, 22, 15, 0)  # Aug 22, 2010, 3 PM
        check_out_date = datetime(2010, 8, 24, 12, 0)  # Aug 24, 2010, 12 PM
        reservation = Reservation(
            reservation_number=reservation_number,
            customer=self,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )
        # Include: Process Payment
        payment = Payment(
            payment_id="GeneratedPaymentID",
            amount=reservation.calculate_total_cost(),
            payment_method=self.__credit_card_info,
            payment_date=datetime.now()
        )
        payment.process_payment()
        # Include: Receive Confirmation
        reservation.generate_confirmation()
        self.add_reservation(reservation)
        print("Reservation made successfully!")
        return reservation

    def modify_reservation(self):
        """
        Allows the customer to modify an existing reservation.
        """
        pass  # Implement modification logic

    def cancel_reservation(self):
        """
        Allows the customer to cancel an existing reservation.
        """
        pass  # Implement cancellation logic

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
        """
        Checks if the room is available.
        """
        return self.__availability

    def reserve(self):
        """
        Marks the room as reserved.
        """
        self.__availability = False

    def release(self):
        """
        Marks the room as available.
        """
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
        self.__confirmation_number = None

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
        """
        Calculates the total cost of the reservation.
        """
        self.__total_cost = self.__total_nights * self.__room.get_rate_per_night()
        return self.__total_cost

    def get_total_cost(self):
        return self.__total_cost

    # Include: Receive Confirmation
    def generate_confirmation(self):
        """
        Generates and sends a confirmation number.
        """
        self.__confirmation_number = "52523687"  # confirmation number
        # sending confirmation via email
        print(f"Confirmation sent to {self.__customer.get_email()}")

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

    # Include: Process Payment
    def process_payment(self):
        """
        Processes the payment.
        """
        print(f"Processing payment of ${self.__amount:.2f} using {self.__payment_method}")
        # Simulate payment processing
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
        """
        Searches and returns a list of available rooms.
        """
        available_rooms = [room for room in self.__rooms if room.check_availability()]
        return available_rooms

# Create hotel
hotel = Hotel(
    name="Comfort Inn & Suites Los Alamos",
    address="2455 Trinity Drive, Los Alamos, NM 87544",
    phone="505-661-1110"
)

# Create room and add to hotel
room = Room(
    room_number=101,
    room_type="2 Queen Beds",
    bed_type="No Smoking Desk/Safe Coffee Maker in Room Hair Dryer",
    smoking_allowed=False,
    rate_per_night=89.55
)
hotel.add_room(room)

# Create customer
customer = Customer()
# For demonstration, we set the details directly
customer.set_name("Ted Vera")
customer.set_email("tever@mac.com")
customer.set_phone("555-1234")
customer.set_credit_card_info("Mastercard (ending in 9904)")

# Customer makes a reservation
reservation = customer.make_reservation(hotel)

# Display reservation details
print("\nYour Reservation Is Confirmed")
print("Thank you for your reservation. Please print your hotel receipt and show it at check-in.\n")
print(f"Your Name: {customer.get_name()}")
print(f"Your Email: {customer.get_email()}")
print(f"Priceline Trip Number: {reservation.get_reservation_number()}")
print(f"Hotel Confirmation Number: {reservation.get_confirmation_number()}\n")
print(f"{hotel.get_name()}")
print(f"{hotel.get_address()}")
print(f"Phone: {hotel.get_phone()}")
print(f"Check-In: {reservation.get_check_in_date().strftime('%a, %b %d, %Y - %I:%M %p')}")
print(f"Check-Out: {reservation.get_check_out_date().strftime('%a, %b %d, %Y - %I:%M %p')}")
print(f"Number of Nights: {reservation.get_total_nights()}")
print(f"Number of Rooms: 1\n")
print(f"Room 1: {customer.get_name()}")
print(f"Room Type: {room.get_room_type()} {room.get_bed_type()} {'Smoking' if room.get_smoking_allowed() else 'No Smoking'}\n")
print("Summary of Charges\n")
print(f"Billing Name: {customer.get_name()}")
print(f"Credit Card: {customer.get_credit_card_info()}\n")
print(f"Room Cost: ${room.get_rate_per_night()} per room, per night")
print(f"Rooms: 1")
print(f"Nights: {reservation.get_total_nights()}")
room_subtotal = room.get_rate_per_night() * reservation.get_total_nights()
print(f"Room Subtotal: ${room_subtotal:.2f}\n")
taxes_and_fees = 21.58  
print(f"Taxes and Fees: ${taxes_and_fees}\n")
total_charges = room_subtotal + taxes_and_fees
print(f"Total Charges: ${total_charges:.2f}")
