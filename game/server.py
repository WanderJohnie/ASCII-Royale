import socket
from player import Player

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(f"Server started on the port {PORT}")
print("Waiting for players...")

players = []

while True:
    client, address = server.accept()

    print(f"Player connected: {address}")

    player = Player(100, 0, 0)

    players.append(player)

    print(f"Players in game: {len(players)}")
