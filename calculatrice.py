import tkinter as tk

class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self.geometry("300x400")
        self.configure(bg="lightgray")
        
        self.entry = tk.Entry(self, font=("Arial", 18), bd=10, relief=tk.FLAT, bg="white", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            (".", 4, 1), ("0", 4, 0), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, font=("Arial", 18), relief=tk.GROOVE, width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(4, weight=1)
    
    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erreur")
        elif value == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)

if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
