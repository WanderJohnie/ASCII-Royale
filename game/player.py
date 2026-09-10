class Player:
    def __init__(self, hp, x_pos, y_pos):
        self.hp = hp
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move_right(self):
        self.x_pos += 1

    def move_left(self):
        self.x_pos -= 1

    def move_up(self):
        self.y_pos -= 1

    def move_down(self):
        self.y_pos += 1
