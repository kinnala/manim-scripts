from manim import *
import numpy as np

class FunctionPlot(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 2,
        "y_min": -1,
        "y_max": 1,
        "x_labeled_nums": range(-1, 3, 1),
        "y_labeled_nums": range(-1, 2, 1),
        "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate=False)
        func_graph=self.get_graph(lambda x: x**3 - x**2, stroke_color=WHITE)
        func_graph_lab=self.get_graph_label(func_graph, label = "x^{3}-x^{2}")
        root1 = Dot().move_to(self.coords_to_point(0, 0))
        root2 = Dot().move_to(self.coords_to_point(1, 0))
        linev1 = Line([1, -2, 0], [6, -2, 0])
        linev2 = Line([1, -3, 0], [6, -3, 0])
        lineh1 = Line([4, -3, 0], [4, -2, 0])
        lineh2 = Line([5, -3, 0], [5, -2, 0])
        self.wait(1)
        self.play(ShowCreation(func_graph), Write(func_graph_lab))
        self.wait(1)
        self.play(ShowCreation(root1), ShowCreation(root2), ShowCreation(linev1), ShowCreation(linev2), ShowCreation(lineh1), ShowCreation(lineh2))
        self.wait(1)
        left = self.get_area(func_graph, -1, 0, area_color=BLUE, dx_scaling=0.2)
        self.play(ShowCreation(left))
        self.wait(1)
        middle = self.get_area(func_graph, 0, 1, area_color=BLUE, dx_scaling=0.2)
        self.play(ShowCreation(middle))
        self.wait(1)
        right = self.get_area(func_graph, 1, 2, area_color=RED, dx_scaling=0.2)
        self.play(ShowCreation(right))
        self.wait(1)
