import json


class Weapon:

    def __init__(
        self,
        name,
        damage,
        range,
        max_ammo,
        fire_rate
    ):
        self.name = name
        self.damage = damage
        self.range = range
        self.max_ammo = max_ammo
        self.fire_rate = fire_rate

        self.ammo = max_ammo

    @classmethod
    def from_json(cls, filename, weapon_name):
        with open(filename, "r") as file:
            data = json.load(file)

        weapon_data = data[weapon_name]

        return cls(
            name=weapon_name,
            damage=weapon_data["damage"],
            range=weapon_data["range"],
            max_ammo=weapon_data["max_ammo"],
            fire_rate=weapon_data["fire_rate"]
        )

    def shoot(self):
        if self.ammo <= 0:
            return False

        self.ammo -= 1
        return True

    def reload(self):
        self.ammo = self.max_ammo


