from prompt_toolkit import choice
import pyvista as pv
from shapes3D import ThreeDShape, cylinder, Octahedron, Dodecahedron
import shapes3D
import os
import json

CONFIG_FILE = "shape_settings.json"
DEFAULT_COLOR = "crimson"

def chooseOption(numberOfOptions):
    choice = 0
    while choice < 1 or choice > numberOfOptions:
        print('1 to ' + str(numberOfOptions) + '> ', end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            choice = int(choice)
        print('\n\n')
        return choice


def load_saved_color():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("color", DEFAULT_COLOR)
        except (json.JSONDecodeError, KeyError):
            return DEFAULT_COLOR
    return DEFAULT_COLOR

def save_new_color(color_name):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"color": color_name}, f)

    
def main():
    print("Welcome to the 3D Shape Drawing Program!")
    print(" 1) Draw a shape")
    print(" 2) Exit")

    choice = chooseOption(2)
    print(choice)
    if choice == 1:
        drawshapes()
    elif choice == 2:
        exit()
    else:
        print("That wasn't a option!")


def drawshapes():
    current_color = load_saved_color()


    print("What shape would you like to draw?")
    print(" 1) Cylinder")
    print(" 2) Octahedron")
    print(" 3) Dodecahedron")
    print(" 4) Back")

    choice = chooseOption(4)

    if choice == 1:
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for radius and height.")
            radius, height = 0.5, 1.0
        
        mesh = pv.Cylinder(radius=radius, height=height)
        print(f"Mesh Bounds (Xmin, Xmax, Ymin, Ymax, Zmin, Zmax): {mesh.bounds}")



        pl = pv.Plotter()
        pl.show_bounds(grid='front', location='outer', all_edges=True)
        pl.add_axes()
        actor = pl.add_mesh(mesh, color=current_color)
        pl.add_text(f"Current Color: {current_color}\nPress the key for the desired color (some may not work)", position="upper_left")
        
        def change_color_to(color_name):
            actor.prop.color = color_name
            save_new_color(color_name)
            pl.render()

        pl.add_key_event("g", lambda: change_color_to("green"))
        pl.add_key_event("b", lambda: change_color_to("blue"))
        pl.add_key_event("r", lambda: change_color_to("red"))
        pl.add_key_event("p", lambda: change_color_to("purple"))
        pl.add_key_event("y", lambda: change_color_to("yellow"))
        pl.add_key_event("o", lambda: change_color_to("orange"))
        pl.add_key_event("c", lambda: change_color_to("cyan"))
        pl.add_key_event("m", lambda: change_color_to("magenta"))
        pl.add_key_event("t", lambda: change_color_to("turquoise"))
        pl.add_key_event("l", lambda: change_color_to("lime"))

        pl.show()
        drawshapes()


    elif choice == 2:
        try:
            edge_length = float(input("Enter the edge length of the octahedron: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for edge length.")
            edge_length = 1.0



        pv_radius = edge_length / (2 ** 0.5)
        mesh = pv.Octahedron(radius=pv_radius)
        print(f"Mesh Bounds (Xmin, Xmax, Ymin, Ymax, Zmin, Zmax): {mesh.bounds}")




        pl = pv.Plotter()
        pl.show_bounds(grid='front', location='outer', all_edges=True)
        pl.add_axes()
        actor = pl.add_mesh(mesh, color=current_color)
        pl.add_text(f"Current Color: {current_color}\nPress the key for the desired color (some may not work)", position="upper_left")
                
        def change_color_to(color_name):
            actor.prop.color = color_name
            save_new_color(color_name)
            pl.render()
        
        pl.add_key_event("g", lambda: change_color_to("green"))
        pl.add_key_event("b", lambda: change_color_to("blue"))
        pl.add_key_event("r", lambda: change_color_to("red"))
        pl.add_key_event("p", lambda: change_color_to("purple"))
        pl.add_key_event("y", lambda: change_color_to("yellow"))
        pl.add_key_event("o", lambda: change_color_to("orange"))
        pl.add_key_event("c", lambda: change_color_to("cyan"))
        pl.add_key_event("m", lambda: change_color_to("magenta"))
        pl.add_key_event("t", lambda: change_color_to("turquoise"))
        pl.add_key_event("l", lambda: change_color_to("lime"))
        
        pl.show()
        drawshapes()

    elif choice == 3:
        try:
            edge_length = float(input("Enter the edge length of the dodecahedron: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for edge length.")
            edge_length = 1.0

        pv_radius = edge_length / (2 * (3 ** 0.5))
        mesh = pv.Dodecahedron(radius=pv_radius)
        print(f"Mesh Bounds (Xmin, Xmax, Ymin, Ymax, Zmin, Zmax): {mesh.bounds}")

        pl = pv.Plotter()
        pl.show_bounds(grid='front', location='outer', all_edges=True)
        pl.add_axes()
        actor = pl.add_mesh(mesh, color=current_color)
        pl.add_text(f"Current Color: {current_color}\nPress the key for the desired color (some may not work)", position="upper_left")
        
        def change_color_to(color_name):
            actor.prop.color = color_name
            save_new_color(color_name)
            pl.render()

        pl.add_key_event("g", lambda: change_color_to("green"))
        pl.add_key_event("b", lambda: change_color_to("blue"))
        pl.add_key_event("r", lambda: change_color_to("red"))
        pl.add_key_event("p", lambda: change_color_to("purple"))
        pl.add_key_event("y", lambda: change_color_to("yellow"))
        pl.add_key_event("o", lambda: change_color_to("orange"))
        pl.add_key_event("c", lambda: change_color_to("cyan"))
        pl.add_key_event("m", lambda: change_color_to("magenta"))
        pl.add_key_event("t", lambda: change_color_to("turquoise"))
        pl.add_key_event("l", lambda: change_color_to("lime"))

        pl.show()
        drawshapes()
        
    elif choice == 4:
        main()
    
    else:
        print("That wasn't an option!")
        drawshapes()

main()
