from utils.console import clear_console
from utils.poo import Vehicle, Person, Student
# from utils.env_variables import get_env_variables

clear_console()

# print(get_env_variables())

# ************************* POO *************************
vehicle = Vehicle()
vehicle.say_hi()

print(vehicle.state())
print(
    f"Wheels: {vehicle.wheels} / LC: {vehicle.chasis_large} cm / WC: {vehicle.chasis_width} cm / Started: {vehicle.started}"
)
vehicle.start()

print(vehicle.state())
print(
    f"Wheels: {vehicle.wheels} / LC: {vehicle.chasis_large} cm / WC: {vehicle.chasis_width} cm / Started: {vehicle.started}"
)

print("!!!!!!!!!!!!!! PERSON !!!!!!!!!!!!!!")
p1 = Person("Rodrigo", "Castro", "M")
print(p1.get_data())

# p1.first_name = "Tota" (It shouldn't be possible, That's why we need encapsulation)
# print(p1.get_data())

p1.__first_name = "Tota"  # Now, protected attribute would not change its value
p1.set_age(-5) # Print Error
p1.set_age(30) # Stablish this new age ...
print(p1.get_data())

print("!!!!!!!!!!!!!! STUDENTS !!!!!!!!!!!!!!")
student1 = Student("Emanuel", "Irusta", 'M', 'Ema School')
print(student1.get_data())
student2 = Student("Damaris", "Irusta", 'F', 'Dami School')
print(student2.get_data())
print(student2.study())