class Car(object):
    def __init__(self,company,model,colour,speed):
        self.company = company
        self.model = model
        self.colour = colour
        self.speed = speed
    
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def acclerate(self):
        print("accelerating")

# Define some students
car1 = Car("BMW", "X3", "black", 300)
car2 = Car("Mercedes Benz", "class-8", "white", 360)

car1.speed