# base class
class Vehicle():


    def __init__(self, v_type="vehicle"): #color="red"
        # definition of a vehicle
        self.name = "Vehicle"

    def add_wheels(self, wheels_num):
        self.wheels = wheels_num

    def __str__(self):
        print(f"This vehicle's name is {self.name}")


car = Vehicle()

print("car's name", car)


class Car(Vehicle):

    def __init__(self, price, ab_count, material="cloth"):
        self.price = price
        self.seat_material = material
        self.airbag_cout = ab_count
        super().__init__(v_type="passenger car") #SUPER passes up ONE LEVEL

    def calc_payments(self, months, rate):
        return f'Your payments for a purchase price of ${self.price} over {months} at {rate} would be too high.
        Buy something cheaper.'

tesla = Car("90,000", 12)

print(tesla.calc_payments(60, "7%"))
print("tesla")



class ColorPicker():
    def __init__(self, primary_color, **kwargs):
        self.primary_color = primary_color
        for key in kwargs: #KWARGS is a DICTIONARY
            setattr(self, key + "_color", kwargs[key]) #SETATTR sets an attribute on SELF

    def get_colors(self):
        return { k:v for k,v in self.__dict__.items() if 'color' in key} #__dict__ turns the INSTANCE into a DICTIONARY which has key:value pairs)

tesla_colors = ColorPicker("red", interior = "black", pinstripe = "goldenrod") #this is an INSTANCE of ColorPicker
color_scheme = tesla_colors.get_colors()
print("tesla colors scheme", color_scheme)

tesla.color_scheme = color_scheme
print(color_scheme)