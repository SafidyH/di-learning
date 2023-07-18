from datetime import datetime

class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

class Airplane:
    def __init__(self, id, company):
        self.id = id
        self.current_location = None
        self.company = company
        self.next_flights = []

    def fly(self, destination):
        for flight in self.next_flights:
            if flight.destination == destination:
                print(f"Flight {flight.id} is taking off.")
                self.current_location = destination
                flight.land()
                self.next_flights.remove(flight)
                break
        else:
            print(f"No flight scheduled to {destination}.")

    def location_on_date(self, date):
        for flight in self.next_flights:
            if flight.date == date:
                return flight.destination.city
        return self.current_location.city if self.current_location else "Unknown"

    def available_on_date(self, date, location):
        if self.current_location and self.current_location.city != location.city:
            return False
        for flight in self.next_flights:
            if flight.date == date and flight.destination == location:
                return False
        return True

class Flight:
    def __init__(self, date, destination, origin, plane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{destination.city}-{plane.company.id}-{date}"

    def take_off(self):
        print(f"Flight {self.id} has taken off.")

    def land(self):
        print(f"Flight {self.id} has landed at {self.destination.city}.")
        self.plane.current_location = self.destination

class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, date):
        for plane in self.planes:
            if plane.available_on_date(date, self):
                flight = Flight(date, destination, self, plane)
                plane.next_flights.append(flight)
                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)
                print(f"Flight {flight.id} from {self.city} to {destination.city} scheduled on {date}.")
                return
        print(f"No available airplane found for the flight from {self.city} to {destination.city} on {date}.")

    def info(self, start_date, end_date):
        print(f"Flight information for {self.city} airport from {start_date} to {end_date}:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"Flight {flight.id} departs on {flight.date} to {flight.destination.city}.")
        for flight in self.scheduled_arrivals:
            if start_date <= flight.date <= end_date:
                print(f"Flight {flight.id} arrives on {flight.date} from {flight.origin.city}.")


# Testing the program
# Creating airlines
airline1 = Airline("AA", "Airline A")
airline2 = Airline("BB", "Airline B")

# Creating airplanes
plane1 = Airplane(1, airline1)
plane2 = Airplane(2, airline1)
plane3 = Airplane(3, airline2)

# Adding airplanes to airlines
airline1.planes.extend([plane1, plane2])
airline2.planes.append(plane3)

# Creating airports
airport1 = Airport("City A")
airport2 = Airport("City B")

# Adding airplanes to airports
airport1.planes.extend([plane1, plane2])
airport2.planes.append(plane3)

# Scheduling flights
airport1.schedule_flight(airport2, datetime(2023, 6, 14))
airport1.schedule_flight(airport2, datetime(2023, 6, 15))
airport2.schedule_flight(airport1, datetime(2023, 6, 15))

# Displaying flight information
airport1.info(datetime(2023, 6, 14), datetime(2023, 6, 15))
