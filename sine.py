from manim import *

class AdvancedMath2DAnimation(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Define the function
        def func(x):
            return np.sin(x) + 0.5 * np.cos(2 * x)

        # Plot the function
        graph = axes.plot(func, color=YELLOW)
        graph_label = axes.get_graph_label(graph, label=Tex("f(x)"))

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # ValueTracker for the moving point
        x_val = ValueTracker(-2.5)

        # Moving dot on the curve
        dot = always_redraw(lambda: Dot(
            axes.c2p(x_val.get_value(), func(x_val.get_value())),
            color=RED
        ))

        # Tangent line
        def get_tangent_line(x):
            dx = 0.01
            slope = (func(x + dx) - func(x - dx)) / (2 * dx)
            point = np.array([x, func(x), 0])
            direction = np.array([1, slope, 0])
            direction = direction / np.linalg.norm(direction)
            start = axes.c2p(*(point - direction))
            end = axes.c2p(*(point + direction))
            return Line(start, end, color=GREEN, stroke_width=6)

        tangent_line = always_redraw(lambda: get_tangent_line(x_val.get_value()))

        # Slope label
        slope_label = always_redraw(lambda: 
            MathTex(f"m = {((func(x_val.get_value()+0.01)-func(x_val.get_value()-0.01))/0.02):.2f}")
            .next_to(dot, UP)
        )

        self.play(FadeIn(dot), FadeIn(tangent_line), FadeIn(slope_label))
        self.wait(0.5)

        # Animate the dot and tangent line moving along the curve
        self.play(x_val.animate.set_value(2.5), run_time=5, rate_func=linear)
        self.wait(1)

        # Area under the curve between x = -2 and x = 2
        area = axes.get_area(graph, x_range=[-2, 2], color=PURPLE, opacity=0.5)
        area_label = MathTex(r"\int_{-2}^{2} f(x)\,dx").next_to(area, DOWN)

        self.play(FadeIn(area), Write(area_label))
        self.wait(2)

        # Animate the area growing from left to right
        for x_end in np.linspace(-2, 2, 30):
            new_area = axes.get_area(graph, x_range=[-2, x_end], color=PURPLE, opacity=0.5)
            self.play(Transform(area, new_area), run_time=0.05)
        self.wait(2)