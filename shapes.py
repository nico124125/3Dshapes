import pyvista as pv
# Parent Class for main 3d shape #
class ThreeDShape:
    def __init__(self, type, colour):
        self.type = type
        self.colour = colour

# Getters and Setters for the parent class #
    def get_type(self):
        return None

    def set_type(self, type):
        self.type = None

    def get_colour(self):
        return None

    def set_colour(self, colour):
        self.colour = None

# Methods for the parent class #
    def volume(self):
        return None

    def surface_area(self):
        return None

    def draw(self):
        return None

# Child Class cylinder #
class cylinder(ThreeDShape):
    def __init__(self, radius, height, colour):
        super().__init__("cylinder", colour)
        self.radius = radius
        self.height = height

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def volume(self):
        return 3.14159 * (self.radius ** 2) * self.height
    
    def surface_area(self):
        return 2 * 3.14159 * self.radius * (self.radius + self.height)

    def draw(self):
        cyl = pv.Cylinder()
        plotter = pv.Plotter()
        plotter.add_mesh(cyl, color='turquoise')
        plotter.show() 
    
# Child Class Octahedron #
class Octahedron(ThreeDShape):
    def __init__(self, edge_length, colour):
        super().__init__("octahedron", colour)
        self.edge_length = edge_length

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def volume(self):
        return (1/3) * (2 ** 0.5) * (self.edge_length ** 3)

    def surface_area(self):
        return 2 * (2 ** 0.5) * (self.edge_length ** 2)

    def draw(self):
        Octahedron = pv.Octahedron()
        plotter = pv.Plotter()
        plotter.add_mesh(Octahedron, color='turquoise')
        plotter.show()

# Child Class Dodecahedron #
class Dodecahedron(ThreeDShape):
    def __init__(self, edge_length, colour):
        super().__init__("dodecahedron", colour)
        self.edge_length = edge_length

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def volume(self):
        return (15 + 7 * (5 ** 0.5)) / 4 * (self.edge_length ** 3)

    def surface_area(self):
        return 3 * (25 + 10 * (5 ** 0.5)) * (self.edge_length ** 2)

    def draw(self):
        Dodecahedron = pv.Dodecahedron(radius=self.edge_length)
        plotter = pv.Plotter()
        plotter.add_mesh(Dodecahedron, color='turquoise')
        plotter.show()
