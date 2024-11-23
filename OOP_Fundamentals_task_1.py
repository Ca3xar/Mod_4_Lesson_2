class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner update to: {self.owner}")

vehicle1 = Vehicle("B15F17", "Chevy Sedan", "Joe Dillard")
vehicle2 = Vehicle("H95V23", "Ford Suv", "Sarah Smith")

print(f"Vehicle 1 - Reg Number: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2 - Reg Number: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

vehicle1.update_owner("Albert Stan")

print(f"Updated Vehicle 1 - Reg No: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")

vehicle2.update_owner("Caroline Beth")

print(f"Updated Vehicle 2 - Reg No: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")