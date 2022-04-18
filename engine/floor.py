'''Floor class, a colleciton of rooms'''
from pandas import array
from engine.room import Room

class Floor:
    def __init__(self, roomList: list):
        
        self.rooms = roomList #list of rooms within a floor tbd if useful

