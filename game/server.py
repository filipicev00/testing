import asyncio
from typing import Dict
from .models import Character

WELCOME = (
    "Welcome to the simple Dungeons & Dragons server!\n"
    "Commands: attack <target>, stats, quit\n"
)

players: Dict[str, Character] = {}

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    writer.write(b"Enter your name: ")
    await writer.drain()
    name = (await reader.readline()).decode().strip()
    player = Character(name=name, hp=20, attack_bonus=2, armor_class=12)
    player.writer = writer
    players[name] = player
    writer.write(WELCOME.encode())
    await writer.drain()
    broadcast(f"{name} has joined the game.\n")
    try:
        while player.is_alive():
            writer.write(b"> ")
            await writer.drain()
            data = await reader.readline()
            if not data:
                break
            command = data.decode().strip()
            if command == "quit":
                break
            elif command == "stats":
                writer.write(f"HP: {player.hp}\n".encode())
            elif command.startswith("attack"):
                parts = command.split()
                if len(parts) < 2:
                    writer.write(b"Usage: attack <target>\n")
                else:
                    target_name = parts[1]
                    target = players.get(target_name)
                    if not target:
                        writer.write(b"No such target.\n")
                    else:
                        result = player.attack(target)
                        writer.write((result + "\n").encode())
                        broadcast(result + "\n", exclude=writer)
                        if not target.is_alive():
                            broadcast(f"{target.name} has fallen!\n")
            else:
                writer.write(b"Unknown command.\n")
    finally:
        writer.close()
        await writer.wait_closed()
        players.pop(name, None)
        broadcast(f"{name} has left the game.\n")


def broadcast(message: str, exclude: asyncio.StreamWriter | None = None):
    for p_name, char in list(players.items()):
        writer = char.writer if hasattr(char, 'writer') else None
        if writer and writer != exclude:
            writer.write(message.encode())
            try:
                asyncio.create_task(writer.drain())
            except RuntimeError:
                pass

async def main(host: str = '0.0.0.0', port: int = 12345):
    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Server shutting down.')
