# Python Calculator – Revision & Interview Weapon

Minimal but viciously complete calculator written in pure Python  
→ Perfect for quickly revising:  
  - functions  
  - exception handling  
  - control flow  
  - input validation  
  - recursion vs iteration  
  - operator precedence parsing  
  - different ways to structure CLI programs

Use this code to remember important patterns fast before exams/interviews.

## Features that actually matter for revision

- Four basic operations (+ − × ÷)
- Power (`**`) and percentage operations
- Parentheses support (via recursive descent or `eval` version)
- Clean modular structure (good for showing OOP/functional style)
- Proper error handling (ZeroDivision, invalid input, etc.)
- Two versions: safe (no eval) vs dangerous-but-convenient (uses eval)

## Quick Navigation – What to Revise Today

| File / Section             | Most Important Revision Topics                          | Exam/Interview Likelihood |
|----------------------------|------------------------------------------------------------------|----------------------------|
| `calculator_safe.py`       | Operator precedence, recursion, parsing, stack usage     | ★★★★★                      |
| `calculator_eval.py`       | eval() dangers, when it's acceptable in contests         | ★★★★                       |
| `main()` loop              | while True + try-except, input validation patterns       | ★★★★★                      |
| `calculate()` function     | Function decomposition, return values, single responsibility| ★★★★                       |
| Exception handling         | Specific exceptions vs bare except, custom messages      | ★★★★★                      |

## Files in this repo

```text
calculator/
├── calculator_safe.py      ← recommended version – no eval()
├── calculator_eval.py      ← shorter but teaches security trade-offs
├── README.md               ← you're reading it
└── examples.txt            ← copy-paste test cases
