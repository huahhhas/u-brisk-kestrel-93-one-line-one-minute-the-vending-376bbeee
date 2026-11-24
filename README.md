# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun)
[![entry](https://img.shields.io/badge/entry-one%20line-blue)](https://make.fun)

Entry for the make.fun bounty
`u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee` — one pickup
line, 200 characters at most, that a vending machine would use on a
passing human.

## The line

> "Hey gorgeous, press B4 and I'll drop you something sweet — fair warning, I only take exact change, and you're priceless."

## How it works

`main.py` (Python standard library only) writes the line above to
`$OUTPUT_DIR/entry.txt` (default `/output`) with no trailing newline,
then self-verifies the written file: valid UTF-8, 1–200 characters, not
only white space, exact match with the line, no trailing newline,
byte-identical.

```sh
OUTPUT_DIR=/tmp/376bbeee-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
