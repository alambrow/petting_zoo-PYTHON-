class Walking:

    def __init__(self):
        self.walk_speed = 0
        self.legs = 0
        self.walking = True

    def run(self):
        print("The animal walks")

class Swimming:

    def __init__(self):
        self.swim_speed = 0
        self.maximum_depth = 0
        self.swimming = True

    def swim(self):
        print("The animal swims")

class Slithering:

    def __init__(self):
        self.slither_speed = 0
        self.length = 0
        self.slithering = True

    def slither(self):
        print("The animal slithers")
