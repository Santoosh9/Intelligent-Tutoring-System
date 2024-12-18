import tkinter as tk
from tkinter import messagebox
import math

class IntelligentTutoringSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent Tutoring System - Geometry")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")  # Light blue background
        
        # Question label
        self.question_label = tk.Label(root, text="Welcome to Geometry ITS!", font=("Arial", 14), bg="#f0f8ff", fg="blue")
        self.question_label.pack(pady=10)
        
        # Options for shapes
        self.shapes = ["Square", "Rectangle", "Triangle", "Circle"]
        self.shape_label = tk.Label(root, text="Choose a shape to calculate its area:", bg="#f0f8ff", fg="black")
        self.shape_label.pack()
        
        self.shape_var = tk.StringVar(value=self.shapes[0])
        self.shape_menu = tk.OptionMenu(root, self.shape_var, *self.shapes, command=self.display_question)
        self.shape_menu.config(bg="white", fg="black", font=("Arial", 10, "bold"))
        self.shape_menu.pack(pady=5)
        
        # Input fields
        self.input_frame = tk.Frame(root, bg="#f0f8ff")
        self.input_frame.pack()
        
        self.input_label1 = tk.Label(self.input_frame, text="", bg="#f0f8ff", fg="black")
        self.input_label1.grid(row=0, column=0, padx=5, pady=5)
        self.input_entry1 = tk.Entry(self.input_frame, bg="white", fg="black")
        self.input_entry1.grid(row=0, column=1, padx=5, pady=5)
        
        self.input_label2 = tk.Label(self.input_frame, text="", bg="#f0f8ff", fg="black")
        self.input_label2.grid(row=1, column=0, padx=5, pady=5)
        self.input_entry2 = tk.Entry(self.input_frame, bg="white", fg="black")
        self.input_entry2.grid(row=1, column=1, padx=5, pady=5)
        
        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, bg="green", fg="white", font=("Arial", 10, "bold"))
        self.submit_button.pack(pady=10)
        
        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 10, "bold"), bg="#f0f8ff", fg="red")
        self.feedback_label.pack()

        # Initialize with default shape
        self.display_question(self.shapes[0])

    def display_question(self, shape):
        """Update input fields based on the chosen shape."""
        self.input_entry1.delete(0, tk.END)
        self.input_entry2.delete(0, tk.END)
        self.feedback_label.config(text="")
        
        if shape == "Square":
            self.input_label1.config(text="Side Length:")
            self.input_label2.config(text="")
            self.input_entry2.grid_remove()  # Hide second input field
        elif shape == "Rectangle":
            self.input_label1.config(text="Length:")
            self.input_label2.config(text="Width:")
            self.input_entry2.grid(row=1, column=1)  # Show second input field
        elif shape == "Triangle":
            self.input_label1.config(text="Base:")
            self.input_label2.config(text="Height:")
            self.input_entry2.grid(row=1, column=1)  # Show second input field
        elif shape == "Circle":
            self.input_label1.config(text="Radius:")
            self.input_label2.config(text="")
            self.input_entry2.grid_remove()  # Hide second input field
        
    def check_answer(self):
        """Validate user input and calculate area."""
        shape = self.shape_var.get()
        
        try:
            if shape == "Square":
                side = float(self.input_entry1.get())
                correct_answer = side ** 2
            elif shape == "Rectangle":
                length = float(self.input_entry1.get())
                width = float(self.input_entry2.get())
                correct_answer = length * width
            elif shape == "Triangle":
                base = float(self.input_entry1.get())
                height = float(self.input_entry2.get())
                correct_answer = 0.5 * base * height
            elif shape == "Circle":
                radius = float(self.input_entry1.get())
                correct_answer = math.pi * (radius ** 2)
            else:
                raise ValueError("Invalid shape selection")
            
            # Provide feedback
            messagebox.showinfo("Result", f"The correct area is: {correct_answer:.2f}")
            self.feedback_label.config(text=f"Area: {correct_answer:.2f}", fg="green")
        
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = IntelligentTutoringSystem(root)

    
    root.mainloop()