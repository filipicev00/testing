# Simple Multiplayer D&D-style Game

This repository contains a very small multiplayer role-playing game that can
be played over a TCP connection. Players connect to a server, choose a name and
can issue commands to attack other players.

## Running the server

```
python3 -m game.server
```

By default the server listens on port `12345`. You can connect using `telnet`
or `nc` (netcat) from another terminal:

```
telnet localhost 12345
```

Once connected you can use the following commands:

- `stats` – show your hit points
- `attack <name>` – attack another connected player
- `quit` – leave the game

## Testing

Run the unit tests with:

```
python3 -m unittest
```
