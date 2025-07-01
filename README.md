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

## Running in Visual Studio Code

If you're using VS Code, you can start the server directly from the integrated
terminal:

1. Open the repository in VS Code.
2. Open the integrated terminal with <kbd>Ctrl</kbd>+<kbd>`</kbd> or from the
   *Terminal* menu.
3. Run `python3 -m game.server` in the terminal.
4. In a second terminal window (this can be another VS Code terminal or any
   system shell) connect to the server with `telnet localhost 12345`.

From there you can begin issuing game commands as shown above.
