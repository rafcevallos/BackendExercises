class Bike():

    def __init__(self, handlebars=1, seat=1):
        self.type = "standard non-electric bike"
        self.handlebars = handlebars
        self.wheels = 2
        self.gears = 2
        self.pedals = 2
        self.seat = seat
        self.frame = "aluminum"
        self.brakes = 2
        self.electric = "0 watt"

class Bucket(Bike):

    def __init__(self):
        super().__init__()
        self.bucket = True

class Customized():

        def __init__(self, type, bike_instance):
            self.type = type
            self.bike_instance = bike_instance

        def add_bucket(self, bucket):
            self.bucket = bucket

# regular_bike = Bike()
# print(regular_bike.handlebars)

# customized = Customized()
# print(customized.handlebars)
# print(customized.seat)

# regular_bike = Bike()
# regular_bike.customized.add_bucket(1)
# print
# bucket_bike = Bucket()
# print(bucket_bike.bucket)

new_bucket = Customized("bucket", Bike())
new_bucket.add_bucket(1)

print("Bucket", new_bucket)