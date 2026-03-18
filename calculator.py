#just for creating a demo url for streamlit sharing
import streamlit as st

# We’re inviting the GUI toolbox friend to the party!
import tkinter as tk

# We also invite the font helper so we can make text look big and cool
from tkinter import font

#some more deployment stuff
st.title("My Python Demo")
st.write("Hello, world!")

# This is our main blueprint — like the instruction sheet to build a calculator toy
class Calculator:

    # This runs automatically every time someone creates a new Calculator
    def __init__(self, root):
        
        # We remember the main window forever — it's the house where everything lives
        self.root = root
        
        # We give the window a fun title that shows at the top
        self.root.title("Calculator")
        
        # We decide how big the window should be (width × height in pixels)
        self.root.geometry("400x500")
        
        # This empty string is our notepad — it will collect everything the user types
        self.expression = ""
        
        # ──────────────────────────────
        # Here we build the SCREEN (the display where numbers appear)
        # ──────────────────────────────
        
        # We create a text box (Entry) that acts as our calculator screen
        self.display = tk.Entry(root,
                                font=("Arial", 20),          # Big friendly font
                                justify="right",             # Numbers stick to the right like real calculators
                                bd=10)                       # Thick border for fancy look
        
        # We glue the screen to the top row, spanning all 4 columns
        self.display.grid(row=0, column=0, columnspan=4,
                          sticky="nsew", padx=5, pady=5)
        
        # ──────────────────────────────
        # Button treasure map! (tells us where each button goes)
        # ──────────────────────────────
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("←", 5, 1)   # Clear and Backspace at the bottom
        ]
        
        # For every button location in our map → build it!
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
        
        # Magic spell: make all rows and columns grow equally when window is resized
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    # Our button-building factory — makes one button + its brain
    def create_button(self, text, row, col):
        
        # This tiny brain decides what happens when the button is clicked
        def on_click():
            
            # If user pressed "C" → clear everything like magic
            if text == "C":
                self.expression = ""
                self.display.delete(0, tk.END)
            
            # If user pressed "=" → time for the big calculation!
            elif text == "=":
                try:
                    # Python's super-smart eval() does the math for us
                    result = eval(self.expression)
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                    # Save result so we can keep calculating from it
                    self.expression = str(result)
                except:
                    # If math goes wrong (like 5++3 or 1/0) → show friendly error
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
            
            # Backspace button ← removes last character
            elif text == "←":
                self.expression = self.expression[:-1]
                self.display.delete(0, tk.END)
                self.display.insert(0, self.expression)
            
            # For numbers, operators, decimal → just add to the notepad
            else:
                self.expression += text
                self.display.delete(0, tk.END)
                self.display.insert(0, self.expression)
        
        # Now we actually create the visible button
        btn = tk.Button(self.root,
                        text=text,
                        font=("Arial", 18),     # Nice big text on buttons
                        command=on_click)       # Connect the brain we made
        
        # Glue the button exactly where the map said
        btn.grid(row=row, column=col,
                 sticky="nsew", padx=2, pady=2)


# This is the starting spell — only runs if we run THIS file directly
if __name__ == "__main__":
    
    # Create the main window (the empty gray rectangle)
    root = tk.Tk()
    
    # Build our calculator inside that window using our blueprint
    calc = Calculator(root)
    
    # Start the infinite listening loop — now the window waits for clicks forever!
    root.mainloop()
