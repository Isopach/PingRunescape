# PingRunescape

Ping Runescape 3 servers using the [pythonping](https://github.com/alessandromaggio/pythonping) library.

Tested with Python 3.8.4.

## Usage

All arguments are optional. By default, it will ping Members' worlds 4 times with 64 bytes.

Ping Non-Members' / F2p Worlds:

```bash
$ python3 runescape_ping.py f2p
$ python3 runescape_ping.py free
$ python3 runescape_ping.py non-members
```

Ping Members' / P2P Worlds:

```bash
$ python3 runescape_ping.py p2p
$ python3 runescape_ping.py 
```

Example output:

```bash
$ python3 runescape_ping.py f2p
Welcome to Runescape 3 World Pinger by Isopach!
Please add 'f2p' or 'free' or 'non-members' as argument to ping Non-Members' Worlds.

World 3: 117ms
World 7: 184ms
World 8: 128ms
World 11: 221ms
World 17: 232ms
World 19: 231ms
World 20: 130ms
World 29: 185ms
World 33: 181ms
World 34: 183ms
World 38: 119ms
World 41: 121ms
World 43: 121ms
World 55: 128ms
World 57: 142ms
World 61: 191ms
World 80: 224ms
World 81: 228ms
World 94: 182ms
World 101: 182ms
World 120: 223ms
World 122: 249ms
World 135: 252ms
World 136: 225ms
World 141: 188ms
```
