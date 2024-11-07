class Animal():
    def __init__(self,eyes=2,legs=0):
        self.eyes = eyes
        self.legs = legs
    def fly(self):
        return False
class Monkey(Animal):
    def __init__(self):
        super().__init__(eyes=2,legs=2)
        self.hands = 2
    def __repr__(self):
        return f"Monkey <eyes: {self.eyes}, legs: {self.legs}, hands: {self.hands}>"
class Squirrel(Animal):
    def __init__(self):
        super().__init__(eyes=2, legs=4)

    def __repr__(self):
        return f"Squirrel <eyes: {self.eyes}, legs: {self.legs}>"

class Pigeon(Animal):
    def __init__(self):
        super().__init__(eyes=2, legs=2)
        self.wings = 2

    def fly(self):
        return True

    def __repr__(self):
        return f"Pigeon <fly: {self.fly()}, eyes: {self.eyes}, legs: {self.legs}, wings: {self.wings}>"

class Eagle(Animal):
    def __init__(self):
        super().__init__(eyes=2, legs=2)
        self.wings = 2

    def fly(self):
        return True

    def __repr__(self):
        return f"Eagle <fly: {self.fly()}, eyes: {self.eyes}, legs: {self.legs}, wings: {self.wings}>"
class Ladder:
    def __init__(self):
        # Dictionary to map rungs to animals
        self.rungs = {
            3: Monkey(),
            5: Squirrel(),
            8: Pigeon(),
            15: Eagle(),
            17: Monkey()
        }

    def animal_at_rung(self, rung):
        """Returns the animal at a given rung."""
        return self.rungs.get(rung, None)

    def get_animals_count(self):
        """Returns the total number of different animals on the ladder."""
        return len(self.rungs)

    def hop(self, rung):
        """Moves the animal from the given rung to the next available rung."""
        if rung in self.rungs:
            next_rung = rung + 1
            if next_rung in self.rungs:
                print("Not Empty")
            else:
                self.rungs[next_rung] = self.rungs[rung]
                self.rungs.pop(rung)
        else:
            print("None")
