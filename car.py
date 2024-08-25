#set up Car class
class Car:
    def __init__(self, name="", location="", kms="", engine="", transmission="", price="", link="", car_id=0):
        self.name = name
        self.location = location
        self.kms = kms
        self.engine = engine
        self.transmission = transmission
        self.price = price
        self.link = link
        self.car_id = car_id
    #remove all the unwanted text from the car text
    def from_text(self, car_text):
        lines = car_text.splitlines()
        lines = [line for line in lines if "Listed within the last 7 days" not in line]
        count = 0

        for line in lines:
            if count == 0:
                self.name = line
                count += 1
            elif count == 1 and "," in line:
                self.location = line
                count += 1
            if "km" in line:
                self.kms = line
            if "Automatic" in line or "Manual" in line:
                self.transmission = line
            if "cc" in line:
                self.engine = line
            if "$" in line:
                self.price = line

        return self
    #convert the car object to a dictionary
    def to_dict(self):
        return {
            "ID": self.car_id,
            "Name": self.name,
            "Location": self.location,
            "KMs": self.kms,
            "Engine Size": self.engine,
            "Transmission": self.transmission,
            "Price": self.price,
            "Link": self.link
        }
