
!pip install numpy matplotlib ipywidgets -q

import random
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

from IPython.display import display, clear_output

print("Math Games Environment Ready!")

# ============================================================
# THREE MATH GAMES
# Scatter Plot | Algebra Practice | Projectile Game
# ============================================================

import random
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

from IPython.display import display, clear_output


# ============================================================
# GAME 1: SCATTER PLOT GAME
# ============================================================

def scatter_plot_game():

    print("\n===== SCATTER PLOT GAME =====")

    print("Find the coordinates of the highlighted point.")

    difficulty = input(
        "Choose difficulty (easy / medium / hard): "
    ).lower().strip()

    graph_sizes = {
        "easy": 5,
        "medium": 10,
        "hard": 20
    }

    limit = graph_sizes.get(difficulty, 5)

    x_target = random.randint(-limit, limit)
    y_target = random.randint(-limit, limit)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Generate random background points
    random_x = [
        random.randint(-limit, limit)
        for _ in range(20)
    ]

    random_y = [
        random.randint(-limit, limit)
        for _ in range(20)
    ]

    ax.scatter(
        random_x,
        random_y,
        color="blue",
        alpha=0.5,
        label="Other points"
    )

    # Highlight target point without displaying its coordinates
    ax.scatter(
        x_target,
        y_target,
        color="red",
        s=180,
        marker="*",
        label="Find this point"
    )

    ax.set_xlim(-limit-1, limit+1)
    ax.set_ylim(-limit-1, limit+1)

    ax.set_xticks(range(-limit, limit+1))
    ax.set_yticks(range(-limit, limit+1))

    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    ax.grid(True)
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_title("Identify the Red Point")

    ax.legend()
    plt.show()

    try:

        guess_x = int(input("\nEnter X coordinate: "))
        guess_y = int(input("Enter Y coordinate: "))

        if guess_x == x_target and guess_y == y_target:

            print("\nCorrect! Excellent work!")
            print("You earned 10 points.")

        else:

            print("\nIncorrect answer!")
            print(f"Correct coordinates: ({x_target}, {y_target})")

    except ValueError:

        print("Please enter valid integer coordinates.")


# ============================================================
# GAME 2: ALGEBRA PRACTICE GAME
# ============================================================

def algebra_game():

    print("\n===== ALGEBRA PRACTICE GAME =====")

    difficulty = input(
        "Choose difficulty (easy / medium / hard): "
    ).lower().strip()

    difficulty_levels = {
        "easy": 10,
        "medium": 50,
        "hard": 100
    }

    limit = difficulty_levels.get(difficulty, 10)

    score = 0
    total_questions = 5

    print("\nSolve for x.")
    print("You will receive 5 random questions.")

    for question in range(1, total_questions + 1):

        print(f"\nQuestion {question}")

        question_type = random.choice([
            "one_step_add",
            "one_step_subtract",
            "one_step_multiply",
            "two_step"
        ])

        answer = random.randint(-limit, limit)

        if question_type == "one_step_add":

            number = random.randint(-limit, limit)

            result = answer + number

            print(f"x + ({number}) = {result}")

        elif question_type == "one_step_subtract":

            number = random.randint(-limit, limit)

            result = answer - number

            print(f"x - ({number}) = {result}")

        elif question_type == "one_step_multiply":

            number = random.choice(
                [i for i in range(-limit, limit+1) if i != 0]
            )

            result = answer * number

            print(f"{number}x = {result}")

        else:

            coefficient = random.choice(
                [i for i in range(-10, 11) if i != 0]
            )

            constant = random.randint(-limit, limit)

            result = coefficient * answer + constant

            print(
                f"{coefficient}x + ({constant}) = {result}"
            )

        try:

            user_answer = int(input("Your answer: "))

            if user_answer == answer:

                print("Correct!")
                score += 10

            else:

                print(f"Incorrect. The correct answer is {answer}.")

        except ValueError:

            print(f"Invalid input. Correct answer: {answer}")

    print("\n===== GAME RESULTS =====")

    print(f"Your score: {score}/{total_questions * 10}")

    if score == 50:
        print("Perfect score! Outstanding!")

    elif score >= 30:
        print("Great job! Keep practicing!")

    else:
        print("Keep learning. You can improve!")


# ============================================================
# GAME 3: PROJECTILE GAME
# ============================================================

def projectile_game():

    print("\n===== PROJECTILE GAME =====")

    print("Your mission: Clear the wall using a parabolic path!")

    print("Level 1: Adjust the sliders.")
    print("Level 2: Enter the coefficients manually.")

    # Random wall
    wall_x = random.randint(3, 8)
    wall_height = random.randint(4, 12)

    print(f"\nWall location: x = {wall_x}")
    print(f"Wall height: {wall_height}")

    # --------------------------------------------------------
    # LEVEL 1: SLIDER CONTROL
    # --------------------------------------------------------

    def level_one():

        print("\n===== LEVEL 1: SLIDER CONTROL =====")

        print("Adjust a, b and c to clear the wall.")

        a_slider = widgets.FloatSlider(
            value=-0.2,
            min=-1.0,
            max=-0.05,
            step=0.05,
            description="a:",
            continuous_update=False
        )

        b_slider = widgets.FloatSlider(
            value=3.0,
            min=0,
            max=10,
            step=0.5,
            description="b:",
            continuous_update=False
        )

        c_slider = widgets.FloatSlider(
            value=0.0,
            min=0,
            max=10,
            step=0.5,
            description="c:",
            continuous_update=False
        )

        output = widgets.Output()

        def update_graph(change=None):

            with output:

                clear_output(wait=True)

                a = a_slider.value
                b = b_slider.value
                c = c_slider.value

                x_values = np.linspace(0, 12, 400)

                y_values = (
                    a*x_values**2 +
                    b*x_values +
                    c
                )

                # Height at wall position
                projectile_height = (
                    a*wall_x**2 +
                    b*wall_x +
                    c
                )

                fig, ax = plt.subplots(figsize=(9, 5))

                ax.plot(
                    x_values,
                    y_values,
                    color="blue",
                    linewidth=2,
                    label="Projectile path"
                )

                # Draw wall
                ax.bar(
                    wall_x,
                    wall_height,
                    width=0.3,
                    color="red",
                    label="Wall"
                )

                ax.axhline(0, color="black")

                ax.set_xlim(0, 12)
                ax.set_ylim(0, max(15, wall_height + 5))

                ax.set_xlabel("Horizontal Distance")
                ax.set_ylabel("Height")
                ax.set_title("Projectile Game - Level 1")

                ax.grid(True)
                ax.legend()

                plt.show()

                print(
                    f"Projectile height at wall: "
                    f"{projectile_height:.2f}"
                )

                if projectile_height > wall_height:

                    print("SUCCESS! You cleared the wall!")

                else:

                    print("TRY AGAIN! Your projectile hit the wall.")

        for slider in [a_slider, b_slider, c_slider]:
            slider.observe(update_graph, names="value")

        display(a_slider, b_slider, c_slider, output)

        update_graph()

        print(
            "\nAdjust the sliders to change the trajectory. "
            "The graph updates automatically."
        )

    # --------------------------------------------------------
    # LEVEL 2: MANUAL COEFFICIENT INPUT
    # --------------------------------------------------------

    def level_two():

        print("\n===== LEVEL 2: MANUAL CHALLENGE =====")

        print("Enter coefficients for y = ax² + bx + c")

        try:

            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))

            if a >= 0:
                print("Use a negative value for a downward trajectory.")
                return

            x_values = np.linspace(0, 12, 400)

            y_values = (
                a*x_values**2 +
                b*x_values +
                c
            )

            projectile_height = (
                a*wall_x**2 +
                b*wall_x +
                c
            )

            fig, ax = plt.subplots(figsize=(9, 5))

            ax.plot(
                x_values,
                y_values,
                color="blue",
                linewidth=2,
                label="Projectile path"
            )

            ax.bar(
                wall_x,
                wall_height,
                width=0.3,
                color="red",
                label="Wall"
            )

            ax.axhline(0, color="black")

            ax.set_xlim(0, 12)
            ax.set_ylim(0, max(15, wall_height + 5))

            ax.set_xlabel("Horizontal Distance")
            ax.set_ylabel("Height")
            ax.set_title("Projectile Game - Level 2")

            ax.grid(True)
            ax.legend()

            plt.show()

            print(
                f"\nHeight at wall: {projectile_height:.2f}"
            )

            if projectile_height > wall_height:

                print("SUCCESS! You cleared the wall!")
                print("You completed Level 2!")

            else:

                print("FAILED! The projectile did not clear the wall.")

        except ValueError:

            print("Please enter valid numerical coefficients.")

    # --------------------------------------------------------
    # PROJECTILE GAME MENU
    # --------------------------------------------------------

    level = input("\nChoose level (1 or 2): ")

    if level == "1":

        level_one()

    elif level == "2":

        level_two()

    else:

        print("Invalid level selection.")


# ============================================================
# MAIN GAME MENU
# ============================================================

def main_menu():

    while True:

        print("\n===================================")
        print("         THREE MATH GAMES")
        print("===================================")

        print("1. Scatter Plot Game")
        print("2. Algebra Practice Game")
        print("3. Projectile Game")
        print("4. Exit")

        choice = input("\nSelect a game (1-4): ")

        if choice == "1":

            scatter_plot_game()

        elif choice == "2":

            algebra_game()

        elif choice == "3":

            projectile_game()

        elif choice == "4":

            print("\nThank you for playing!")
            break

        else:

            print("Invalid selection. Please try again.")


# START THE APPLICATION

main_menu()
