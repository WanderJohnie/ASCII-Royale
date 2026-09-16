import json


class Player:

    def __init__(
        self,
        max_hp,
        x_pos,
        y_pos,
        speed,
        starting_weapon
    ):
        self.max_hp = max_hp
        self.hp = max_hp

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.speed = speed
        self.starting_weapon = starting_weapon

    @classmethod
    def from_json(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        player_data = data["default"]

        return cls(
            max_hp=player_data["max_hp"],
            x_pos=player_data["start_x"],
            y_pos=player_data["start_y"],
            speed=player_data["speed"],
            starting_weapon=player_data["starting_weapon"]
        )

    def move_right(self, world):
        new_x = self.x_pos + self.speed

        if world.is_walkable(new_x, self.y_pos):
            self.x_pos = new_x
            return True

        return False

    def move_left(self, world):
        new_x = self.x_pos - self.speed

        if world.is_walkable(new_x, self.y_pos):
            self.x_pos = new_x
            return True

        return False

    def move_up(self, world):
        new_y = self.y_pos - self.speed

        if world.is_walkable(self.x_pos, new_y):
            self.y_pos = new_y
            return True

        return False

    def move_down(self, world):
        new_y = self.y_pos + self.speed

        if world.is_walkable(self.x_pos, new_y):
            self.y_pos = new_y
            return True

        return False


