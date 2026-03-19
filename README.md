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

| Sin                        | Severity | Quote you'll hear in viva/interview                                      |
|----------------------------|----------|--------------------------------------------------------------------------|
| Naked `eval()`             | Nuclear  | "So... you just let users run arbitrary Python code?"                    |
| Zero input validation      | High     | "What happens if I paste `__import__('os').system('calc')`?"             |
| Broad `except:`            | Medium   | "You catch everything and say 'Error'. Very informative."                |
| No keyboard binding        | Medium   | "So this is mouse-only in 2026?"                                         |
| No operator precedence explanation | Low | "You know eval does all the work, right?"                                |

## How to actually use this security nightmare in 2025–2026

### Easiest way (the zip/executable route most people will take)

1. Download the ZIP file  
2. Extract the folder anywhere (Desktop, Downloads, your mom's laptop, whatever)  
3. Open the extracted folder  
4. Go into the `dist` subfolder  
5. Double-click the `.exe` (probably named `calculator.exe` or something equally creative)  

Boom. Runs without Python installed, no terminal, no pip hell.  
You just became the guy who sends sketchy .exe files in the group chat. Congrats.

### Old-school nerd way (if you hate convenience)

```bash
# You still need Python + tkinter installed
python calculator.py
# or whatever tragic filename you chose
