# Tkinter Trash-Calculator 3000

The most generic, eval()-poisoned, college-assignment-style calculator ever made in Python.  
Made in like 45 minutes while half-watching a YouTube tutorial.  
It works. Barely. Don't deploy it anywhere serious.

## What this actually is

- 4-function calculator (+ − × ÷) with decimal point
- Parentheses? Nope (eval handles them but good luck typing them fast)
- Power? Nope
- Percentage? Nope
- Memory (M+, MR)? Nope
- History? Nope
- Keyboard input? Nope (click only, enjoy your RSI)
- Backspace & Clear buttons? Yes — small mercy

## Features you're proud of (and should be)

- Resizable window that doesn't look like absolute garbage
- Grid weights → buttons stretch nicely
- Backspace button (many noobs skip this)
- Class-based structure instead of 300 lines in global scope

## Features that will get you clowned in 2026

| Sin                     | Severity | Quote you'll hear in viva/interview                           |
|-------------------------|----------|----------------------------------------------------------------|
| Naked `eval()`          | Nuclear  | "So... you just let users run arbitrary Python code?"         |
| Zero input validation   | High     | "What happens if I paste `__import__('os').system('calc')`?"   |
| Broad `except:`         | Medium   | "You catch everything and say 'Error'. Very informative."     |
| No keyboard binding     | Medium   | "So this is mouse-only in 2026?"                               |
| No operator precedence explanation | Low   | "You know eval does all the work, right?"                      |

## How to run this disaster

```bash
# You need tkinter (comes with most Python installs)
python calculator.py
# or whatever you named the file
