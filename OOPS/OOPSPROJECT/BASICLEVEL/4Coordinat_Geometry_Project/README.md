# 📐 2D Coordinate Geometry - Python OOP Project

This project demonstrates the core principles of **Object-Oriented Programming (OOP)** in Python using real-world mathematical applications from **2D Coordinate Geometry**.

---

## 📚 Modules Covered

### 1. ✅ Point Class
- Represents a point in 2D space.
- **Features:**
  - Distance between two points
  - Midpoint
  - Slope between points
  - String representation using `__str__` and `__repr__`
  - Operator overloading (`==`, `<`, `>`, etc.)

---

### 2. ✅ Line Class
- Represents a line segment defined by two points.
- **Features:**
  - Line equation in form `y = mx + c`
  - Slope and y-intercept calculation
  - Midpoint of the line
  - Check if a point lies on the line
  - Distance from a point to the line
  - Custom string formatting for equations

---

### 3. ✅ Circle Class
- Represents a circle in 2D space.
- **Features:**
  - Equation in standard and general form
  - Area and circumference calculation
  - Point containment check (inside, outside, or on circle)
  - Relation with another circle (touching, intersecting, etc.)
  - Optional visualization with `matplotlib`

---

### 4. ✅ Triangle Class
- Represents a triangle using three points.
- **Features:**
  - Area (using Heron’s Formula)
  - Perimeter
  - Centroid
  - Type classification (equilateral, isosceles, scalene, right-angled)

---

## 🔁 Unified Test File: `zgeometry_test.py`
- Demonstrates and tests functionality from all modules.
- Provides real-time outputs and comparisons using hardcoded examples.
- Acts as a reference for using each class and method.

---

---

## 🧱 Modules Included

| Module         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `PointClassModule.py` | Defines a 2D point and operations like distance, midpoint, and slope.          |
| `BLineClass2D.py`     | Models a line using two points. Supports slope, y-intercept, and point-check. |
| `CircleClass2D.py`    | Models a circle with center and radius. Computes area, circumference, and position relation. |
| `TriangleClass.py`    | Models a triangle with 3 points. Computes area, perimeter, centroid, type.     |
| `zgeometry_test.py`   | A unified test script to demonstrate all functionality from the modules.       |

---





