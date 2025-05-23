from manim import *

class ConicSections(Scene):
    def construct(self):
        # Ellipse parameters
        a = 3  # Semi-major axis
        b = 2  # Semi-minor axis
        c = np.sqrt(a**2 - b**2)  # Distance from center to focus

        # Ellipse
        ellipse = Ellipse(width=2*a, height=2*b, color=BLUE)
        self.play(Create(ellipse))

        # Foci of the ellipse
        focus1 = Dot(point=LEFT * c, color=RED)
        focus2 = Dot(point=RIGHT * c, color=RED)
        self.play(FadeIn(focus1), FadeIn(focus2))

        # Directrices of the ellipse
        directrix1 = Line(start=LEFT * (a**2 / c + 1), end=LEFT * (a**2 / c - 1), color=GREEN)
        directrix2 = Line(start=RIGHT * (a**2 / c - 1), end=RIGHT * (a**2 / c + 1), color=GREEN)
        self.play(Create(directrix1), Create(directrix2))

        # Reflective property: a point on the ellipse
        point = Dot(point=ellipse.point_from_proportion(0.25), color=YELLOW)
        self.play(FadeIn(point))

        # Lines from the point to each focus
        line1 = Line(point.get_center(), focus1.get_center(), color=ORANGE)
        line2 = Line(point.get_center(), focus2.get_center(), color=ORANGE)
        self.play(Create(line1), Create(line2))

        self.wait(2)

        # Hyperbola parameters
        a_h = 3  # Semi-transverse axis
        b_h = 2  # Semi-conjugate axis
        c_h = np.sqrt(a_h**2 + b_h**2)  # Distance from center to focus

        # Hyperbola
        hyperbola = ParametricFunction(
            lambda t: np.array([a_h * np.cosh(t), b_h * np.sinh(t), 0]),
            t_range = [-2, 2],
            color = PURPLE
        )
        hyperbola_mirror = ParametricFunction(
            lambda t: np.array([-a_h * np.cosh(t), b_h * np.sinh(t), 0]),
            t_range = [-2, 2],
            color = PURPLE
        )
        self.play(Create(hyperbola), Create(hyperbola_mirror))

        # Foci of the hyperbola
        focus1_h = Dot(point=RIGHT * c_h, color=RED)
        focus2_h = Dot(point=LEFT * c_h, color=RED)
        self.play(FadeIn(focus1_h), FadeIn(focus2_h))

        # Directrices of the hyperbola
        directrix1_h = Line(start=RIGHT * (a_h / c_h + 1), end=RIGHT * (a_h / c_h - 1), color=GREEN)
        directrix2_h = Line(start=LEFT * (a_h / c_h - 1), end=LEFT * (a_h / c_h + 1), color=GREEN)
        self.play(Create(directrix1_h), Create(directrix2_h))

        self.wait(2)
