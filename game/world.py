import json


class World:

    def __init__(self, map_file):

        with open(map_file, "r") as file:
            self.data = json.load(file)

        self.width = self.data["width"]
        self.height = self.data["height"]

        self.tiles = self.data["tiles"]
        self.map = self.data["map"]

    def get_tile(self, x, y):

        if x < 0 or x >= self.width:
            return None

        if y < 0 or y >= self.height:
            return None

        return self.map[y][x]

    def get_tile_info(self, x, y):

        tile = self.get_tile(x, y)

        if tile is None:
            return None

        return self.tiles[tile]

    def is_walkable(self, x, y):

        tile = self.get_tile(x, y)

        if tile is None:
            return False

        return self.tiles[tile]["walkable"]

    def get_visible_area(self, player_x, player_y, radius=10):

        visible_area = []

        for y in range(
            player_y - radius,
            player_y + radius + 1
        ):

            row = ""

            for x in range(
                player_x - radius,
                player_x + radius + 1
            ):

                if (
                    x < 0
                    or x >= self.width
                    or y < 0
                    or y >= self.height
                ):
                    row += " "
                    continue

                row += self.map[y][x]

            visible_area.append(row)

        return visible_area

    def print_map(self):

        for row in self.map:
            print(row)


