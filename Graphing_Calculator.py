
!pip install numpy matplotlib sympy pandas ipywidgets

import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

import pandas as pd

x, y = symbols("x y")


# ==========================================
# GRAPH SETTINGS
# ==========================================

GRAPH_MIN = -10
GRAPH_MAX = 10
DENSITY = 5


# ==========================================
# 1. GRAPH A FUNCTION AND DISPLAY A TABLE
# ==========================================

def table_and_graph():

    x, y = symbols("x y")

    eq = input("Enter equation for y (example: x**2 + 2*x + 1): ")
    expr = parse_expr(eq)

    xlo = GRAPH_MIN
    xhi = GRAPH_MAX

    x_inputs = np.linspace(xlo, xhi, (xhi - xlo) * DENSITY + 1)

    function = lambdify(x, expr, modules=["numpy"])

    y_outputs = np.array(function(x_inputs), dtype=float)

    # Remove invalid values for plotting
    valid = np.isfinite(y_outputs)

    # Generate table
    rows = []

    for i in range(xlo, xhi + 1):
        value = float(expr.evalf(subs={x: i}))
        rows.append([i, round(value, 2) if np.isfinite(value) else "Undefined"])

    df = pd.DataFrame(rows, columns=["x", "y"])

    print("\nTABLE OF VALUES")
    print(df.to_string(index=False))

    # Plot graph
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x_inputs[valid], y_outputs[valid], label=f"y = {eq}")

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Graph of y = {eq}")

    ax.grid(True)
    ax.legend()

    plt.show()


# ==========================================
# 2. SOLVE A SYSTEM OF EQUATIONS
# ==========================================

def solve_system_of_equations():

    x, y = symbols("x y")

    eq1 = input("First equation (enter expression equal to zero): ")
    eq2 = input("Second equation (enter expression equal to zero): ")

    solutions = solve(
        [parse_expr(eq1), parse_expr(eq2)],
        [x, y],
        dict=True
    )

    if solutions:
        print("\nEquations intersect at:")

        for solution in solutions:
            print(
                f"x = {solution[x]}, y = {solution[y]}"
            )
    else:
        print("No unique intersection found.")


# ==========================================
# 3. GRAPH TWO EQUATIONS AND THEIR INTERSECTION
# ==========================================

def equations_intercept():

    x, y = symbols("x y")

    eq1 = input("First equation (enter expression equal to zero): ")
    eq2 = input("Second equation (enter expression equal to zero): ")

    expr1 = parse_expr(eq1)
    expr2 = parse_expr(eq2)

    solutions = solve([expr1, expr2], [x, y], dict=True)

    if not solutions:
        print("Equations do not have a unique intersection.")
        return

    xlo = GRAPH_MIN
    xhi = GRAPH_MAX

    x_inputs = np.linspace(xlo, xhi, 500)

    # Solve each equation for y
    y_solver1 = solve(expr1, y)
    y_solver2 = solve(expr2, y)

    if not y_solver1 or not y_solver2:
        print("Unable to express both equations as y = f(x).")
        return

    function1 = lambdify(x, y_solver1[0], modules=["numpy"])
    function2 = lambdify(x, y_solver2[0], modules=["numpy"])

    y_outputs1 = np.array(function1(x_inputs), dtype=float)
    y_outputs2 = np.array(function2(x_inputs), dtype=float)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x_inputs, y_outputs1, label="Equation 1")
    ax.plot(x_inputs, y_outputs2, label="Equation 2")

    for solution in solutions:

        xi = float(solution[x])
        yi = float(solution[y])

        print(f"Intersection: ({xi:.4f}, {yi:.4f})")

        ax.scatter(xi, yi, color="red", s=80, zorder=5)

        ax.annotate(
            f"({xi:.2f}, {yi:.2f})",
            (xi, yi)
        )

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.set_xlim(xlo, xhi)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("System of Equations")

    ax.grid(True)
    ax.legend()

    plt.show()


# ==========================================
# 4. SOLVE QUADRATIC EQUATIONS AND GRAPH ROOTS
# ==========================================

def quadratic_eq_roots_and_vertex():

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a == 0:
        print("This is not a quadratic equation.")
        return

    discriminant = b**2 - 4*a*c

    vertex_x = -b / (2*a)
    vertex_y = a*vertex_x**2 + b*vertex_x + c

    print("\nQUADRATIC EQUATION RESULTS")

    print(f"Equation: {a}x² + {b}x + {c} = 0")
    print(f"Vertex: ({vertex_x:.4f}, {vertex_y:.4f})")

    if discriminant >= 0:

        root_1 = (-b + math.sqrt(discriminant)) / (2*a)
        root_2 = (-b - math.sqrt(discriminant)) / (2*a)

        print(f"Root 1: {root_1:.4f}")
        print(f"Root 2: {root_2:.4f}")

    else:

        root_1 = None
        root_2 = None

        print("No real roots. The roots are complex.")

    # Graph range
    xlo = vertex_x - 10
    xhi = vertex_x + 10

    x_values = np.linspace(xlo, xhi, 500)

    y_values = a*x_values**2 + b*x_values + c

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x_values, y_values, label="Quadratic equation")

    # Plot vertex
    ax.scatter(vertex_x, vertex_y, color="red", s=100,
               label="Vertex", zorder=5)

    # Plot roots
    if discriminant >= 0:

        ax.scatter(
            [root_1, root_2],
            [0, 0],
            color="green",
            s=100,
            label="Roots",
            zorder=5
        )

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Quadratic Equation Graph")

    ax.grid(True)
    ax.legend()

    plt.show()


# ==========================================
# 5. SHADE ABOVE OR BELOW A FUNCTION
# ==========================================

def shade_function():

    x = symbols("x")

    eq = input("Enter function (example: 2*x + 3): ")
    shade = input("Shade above or below? ").lower().strip()

    if shade not in ["above", "below"]:
        print("Choose either above or below.")
        return

    expr = parse_expr(eq)

    x_values = np.linspace(GRAPH_MIN, GRAPH_MAX, 500)

    function = lambdify(x, expr, modules=["numpy"])
    y_values = np.array(function(x_values), dtype=float)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x_values, y_values, label=f"y = {eq}")

    if shade == "above":
        ax.fill_between(
            x_values, y_values, GRAPH_MAX,
            alpha=0.3, label="Above the function"
        )
    else:
        ax.fill_between(
            x_values, GRAPH_MIN, y_values,
            alpha=0.3, label="Below the function"
        )

    ax.set_xlim(GRAPH_MIN, GRAPH_MAX)
    ax.set_ylim(GRAPH_MIN, GRAPH_MAX)

    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.grid(True)
    ax.legend()

    plt.title("Shaded Graph")
    plt.show()


# ==========================================
# 6. INTERACTIVE ZOOM
# ==========================================

def zoom_graph():

    import ipywidgets as widgets
    from IPython.display import display

    x = symbols("x")

    eq = input("Enter function to graph (example: x**2): ")
    expr = parse_expr(eq)

    function = lambdify(x, expr, modules=["numpy"])

    def draw_graph(zoom=10):

        x_values = np.linspace(-zoom, zoom, 500)
        y_values = np.array(function(x_values), dtype=float)

        fig, ax = plt.subplots(figsize=(9, 5))

        ax.plot(x_values, y_values, label=f"y = {eq}")

        ax.set_xlim(-zoom, zoom)
        ax.set_ylim(-zoom, zoom)

        ax.axhline(0, color="black")
        ax.axvline(0, color="black")

        ax.grid(True)
        ax.legend()

        plt.show()

    slider = widgets.IntSlider(
        value=10,
        min=2,
        max=50,
        step=1,
        description="Zoom:"
    )

    display(widgets.interactive(draw_graph, zoom=slider))


# ==========================================
# MAIN MENU
# ==========================================

options = [
    (table_and_graph,
     'Display the graph and a table of values for any "y=" equation input'),

    (solve_system_of_equations,
     "Solve a system of two equations without graphing"),

    (equations_intercept,
     "Graph two equations and plot the point of intersection"),

    (quadratic_eq_roots_and_vertex,
     "Given a, b and c in a quadratic equation, plot the roots and vertex"),

    (shade_function,
     "Shade above or below a function"),

    (zoom_graph,
     "Zoom in or out on a graph")
]


print("\n======================================")
print("          GRAPHING CALCULATOR")
print("======================================")

print("\nWhat would you like to do?")

for i in range(len(options)):
    print(f"{i+1}: {options[i][1]}")

try:

    selection = int(input("\nEnter your selection: "))

    if 1 <= selection <= len(options):
        options[selection-1][0]()

    else:
        print("Invalid selection. Choose between 1 and 6.")

except ValueError:
    print("Please enter a valid number.")
