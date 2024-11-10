class Plane:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            return f"Passenger {name} has been successfully booked"
        else:
            return f"Sorry, the plane is full. Booking unsuccessful for {name}"

    def list_passengers(self):
        return self.passengers

# Creating Plane instances with specified capacities
plane_cesna = Plane(4)
plane_chopper = Plane(2)

# Adding passengers to plane_cesna
print(plane_cesna.add_passenger("John"))
print(plane_cesna.add_passenger("Mary"))
print(plane_cesna.add_passenger("Luke"))
print(plane_cesna.add_passenger("Sam"))

# Listing passengers in plane_cesna
print(plane_cesna.list_passengers())