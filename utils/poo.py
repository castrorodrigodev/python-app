class Vehicle:
    wheels = 4
    chasis_large = 260  # cm
    chasis_width = 130  # cm
    started = False

    def say_hi(self):
        print("Hello from vehicle")

    def start(self):
        self.started = True

    def state(self):
        if self.started:
            return "Vehicle is working"
        else:
            return "Vehicle is stoped"


class Person:
    __first_name = ""
    last_name = ""
    __age = 0
    gender = "No definition"

    def __init__(self, f_name, l_name, gender):
        self.__first_name = f_name
        self.last_name = l_name
        self.gender = gender

    def set_age(self, age):
        if age < 0:
            print("Negative age is impossible")
        else:
            self.__age = age

    def speak(self):
        return f"Person with name {self.__first_name} is speaking"

    def walk(self):
        return f"Person with name {self.__first_name} is walking"

    def get_data(self):
        return f"Name: {self.__first_name} / Last: {self.last_name} / Age: {self.__age} / Gender: {self.gender}"


class Student(Person):
    def __init__(self, f_name, l_name, gender, school):
        super().__init__(f_name, l_name, gender)
        self.school = school

    def study(self):
        return "I am studying"

    def get_data(self):
        return super().get_data() + " / "+ f"School: {self.school}"
