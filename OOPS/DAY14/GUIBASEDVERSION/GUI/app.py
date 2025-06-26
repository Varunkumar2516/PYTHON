
import sys
import os

# Add the parent folder (Coordinat_Geometry_Project_Test) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox


from Geometry.PointModule import Point
from Geometry.LineModule import Line

def compute_line_data():
    try:
        # 1. Get text input
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())

        # 2. Create Point and Line
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        line = Line(p1, p2)

        # 3. Calculate and show result
        slope = line.lineslope()
        intercept = line.y_intercept()
        messagebox.showinfo("Result", f"Slope: {slope}\nY-Intercept: {intercept}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


root = tk.Tk()
root.title("Geometry App")
root.geometry("400x200")

tk.Label(root, text="Point 1 (x1, y1):").grid(row=0, column=0)
entry_x1 = tk.Entry(root)
entry_y1 = tk.Entry(root)
entry_x1.grid(row=0, column=1)
entry_y1.grid(row=0, column=2)

tk.Label(root, text="Point 2 (x2, y2):").grid(row=1, column=0)
entry_x2 = tk.Entry(root)
entry_y2 = tk.Entry(root)
entry_x2.grid(row=1, column=1)
entry_y2.grid(row=1, column=2)

tk.Button(root, text="Calculate Line", command=compute_line_data).grid(row=2, column=1)
root.mainloop()
