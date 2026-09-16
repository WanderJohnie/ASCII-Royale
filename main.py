import sys
import termios
import tty

from game.world import World
from game.player import Player
from game.weapon import Weapon


def clear_screen():
    print("\033[H\033[J", end="")


def get_key():

    old_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setcbreak(sys.stdin.fileno())
        key = sys.stdin.read(1)

    finally:
        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            old_settings
        )

    return key.lower()


def draw_world(world, player):

    visible_area = world.get_visible_area(
        player.x_pos,
        player.y_pos,
        radius=10
    )

    player_screen_x = 10
    player_screen_y = 10

    for y, row in enumerate(visible_area):

        row = list(row)

        if y == player_screen_y:
            row[player_screen_x] = "@"

        print("".join(row))


def main():

    # Welt laden
    world = World("data/map.json")

    # Spieler laden
    player = Player.from_json("data/players.json")

    # Startwaffe laden
    weapon = Weapon.from_json(
        "data/weapons.json",
        player.starting_weapon
    )

    while True:

        clear_screen()

        print("================================")
        print("          ASCII ROYALE")
        print("================================")
        print()

        print(f"HP: {player.hp}/{player.max_hp}")
        print(f"Waffe: {weapon.name}")
        print(f"Munition: {weapon.ammo}/{weapon.max_ammo}")
        print(f"Position: {player.x_pos}, {player.y_pos}")

        print()
        print("WASD = bewegen")
        print("Q   = beenden")
        print()

        draw_world(world, player)

        print()

        command = get_key()

        match command:

            case "q":
                print("\nSpiel beendet.")
                break

            case "w":
                player.move_up(world)

            case "s":
                player.move_down(world)

            case "a":
                player.move_left(world)

            case "d":
                player.move_right(world)


if __name__ == "__main__":
    main()
