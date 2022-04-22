'''Player / Monster defined as characters'''

class Character:
    def __init__(self, hp: int, atk: int):
        self.hp = hp
        self.ad = atk
        self.posx = 10
        self.posy = 10

    def move(self, direction):
        if direction == 'r':
            self.posx += 10

        elif direction == 'l':
            self.posx -= 10

        elif direction == 'u':
            self.posy += 10
    
        elif direction == 'd':
            self.posy -= 10

            