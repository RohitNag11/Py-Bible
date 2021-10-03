class Robot:
    # create a constructor:
    # (need to add self to any constructor)
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    # create a method:
    # (need to add self to any method)
    def introduce(self):
        print("My name is " + self.name)


class Person():
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False


# Creting objects:
r1 = Robot("tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

p1 = Person("Alice", "aggressive", False, r1)
p2 = Person("Becky", "talkative", True, r2)

# Running a method:
r1.introduce()  # here, self refers to r1
r2.introduce()  # here, self refers to r2
p2.stand_up()
print(p2.isSitting)
