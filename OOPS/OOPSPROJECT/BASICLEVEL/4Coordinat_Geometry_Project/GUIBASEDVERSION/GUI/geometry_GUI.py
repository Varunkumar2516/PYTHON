import PySimpleGUI as sg
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Geometry.PointModule import Point
from Geometry.LineModule import Line
from Geometry.Circlemodule import Circle

import matplotlib.pyplot as plt
# --- GUI Theme ---
sg.theme('DarkAmber')


# --- Make Sure Save Directory Exists ---
os.makedirs("results", exist_ok=True)

# --- Line Section Layout ---
line_layout = [
    [sg.Text("Point 1 (x1, y1):"), sg.Input(size=(6,1), key='x1'), sg.Input(size=(6,1), key='y1')],
    [sg.Text("Point 2 (x2, y2):"), sg.Input(size=(6,1), key='x2'), sg.Input(size=(6,1), key='y2')],
    [sg.Button("Compute Line", key='line_compute'), sg.Button("Plot Line", key='line_plot'), sg.Button("Save Line", key='line_save')],
    [sg.Text("Line Result:"), sg.Text("", size=(40,1), key='line_result')],
]

# --- Circle Section Layout ---
circle_layout = [
    [sg.Text("Center (x, y):"), sg.Input(size=(6,1), key='cx'), sg.Input(size=(6,1), key='cy')],
    [sg.Text("Radius:"), sg.Input(size=(6,1), key='radius')],
    [sg.Button("Compute Circle", key='circle_compute'), sg.Button("Plot Circle", key='circle_plot'), sg.Button("Save Circle", key='circle_save')],
    [sg.Text("Circle Result:"), sg.Text("", size=(45,1), key='circle_result')],
]

# --- Main Layout ---
layout = [
    [sg.TabGroup([[
        sg.Tab("Line Tools", line_layout),
        sg.Tab("Circle Tools", circle_layout),
        sg.Tab("Triangle Tools", [[sg.Text("Coming Soon!")]])
    ]])],
    [sg.Button("Exit")]
]

# --- Create Window ---
window = sg.Window("Geometry Visual Tool", layout, finalize=True, size=(600, 300))

# --- Event Loop ---
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    # === Line Tools ===
    if event == 'line_compute':
        try:
            p1 = Point(float(values['x1']), float(values['y1']))
            p2 = Point(float(values['x2']), float(values['y2']))
            line = Line(p1, p2)
            slope = line.lineslope()
            y_int = line.y_intercept()
            window['line_result'].update(f"Slope: {slope:.2f}, Y-Intercept: {y_int:.2f}")
        except Exception as e:
            window['line_result'].update(f"Error: {e}")

    if event == 'line_plot':
        try:
            x1, y1 = float(values['x1']), float(values['y1'])
            x2, y2 = float(values['x2']), float(values['y2'])
            plt.figure()
            plt.plot([x1, x2], [y1, y2], 'b-o', label="Line")
            plt.title("Line Between Points")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.grid(True)
            plt.legend()
            plt.show()
        except Exception as e:
            sg.popup_error("Plot Error:", e)

    if event == 'line_save':
        try:
            p1 = Point(float(values['x1']), float(values['y1']))
            p2 = Point(float(values['x2']), float(values['y2']))
            line = Line(p1, p2)
            slope = line.lineslope()
            y_int = line.y_intercept()
            with open("results/line_results.txt", "w") as f:
                f.write(f"Point 1: {p1}\nPoint 2: {p2}\n")
                f.write(f"Slope: {slope}\nY-Intercept: {y_int}\n")
            sg.popup("Saved", "Line data saved to results/line_results.txt")
        except Exception as e:
            sg.popup_error("Save Error:", e)

    # === Circle Tools ===
    if event == 'circle_compute':
        try:
            center = Point(float(values['cx']), float(values['cy']))
            r = float(values['radius'])
            circle = Circle(center, r)
            area = circle.Area()
            circum = circle.Circumference()
            Equation=circle.Equation()
            window['circle_result'].update(f"Area: {area:.2f}, Circumference: {circum:.2f}.Equation:{Equation}")
        except Exception as e:
            window['circle_result'].update(f"Error: {e}")

    if event == 'circle_plot':
        try:
            center = Point(float(values['cx']), float(values['cy']))
            r = float(values['radius'])
            fig, ax = plt.subplots()
            circle_plot = plt.Circle((center.abscissa, center.ordinate), r, fill=False, color='green')
            ax.add_patch(circle_plot)
            ax.set_xlim(center.abscissa - r - 2, center.abscissa + r + 2)
            ax.set_ylim(center.ordinate - r - 2, center.ordinate + r + 2)
            ax.set_aspect('equal', adjustable='datalim')
            plt.title("Circle Visualization")
            plt.grid(True)
            plt.show()
        except Exception as e:
            sg.popup_error("Plot Error:", e)

    if event == 'circle_save':
        try:
            center = Point(float(values['cx']), float(values['cy']))
            r = float(values['radius'])
            circle = Circle(center, r)
            area = circle.area()
            circum = circle.circumference()
            with open("results/circle_results.txt", "w") as f:
                f.write(f"Center: {center}\nRadius: {r}\n")
                f.write(f"Area: {area}\nCircumference: {circum}\n")
            sg.popup("Saved", "Circle data saved to results/circle_results.txt")
        except Exception as e:
            sg.popup_error("Save Error:", e)

window.close()
