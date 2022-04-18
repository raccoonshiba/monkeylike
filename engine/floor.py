'''Floor class, a collection of rooms'''

from engine.room import Room

class Floor:
    def __init__(self, seed, number, property):
        self.number = number
        self.property = property
        self.rooms = []
        for i in range(seed):
            self.rooms.append(Room(property))

            