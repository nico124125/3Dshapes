from prompt_toolkit import choice
import pyvista as pv
from shapes3D import ThreeDShape, cylinder, Octahedron, Dodecahedron
import shapes3D

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
    
def main():
    print("Welcome to the 3D Shape Drawing Program!")
    print(" 1) Draw a shape")
    print(" 2) Change the colour of the shapes")
    print(" 3) Exit")

    choice = chooseOption(3)
    print(choice)
    if choice == 1:
        drawshapes()
    elif choice == 2:
        shape_colour()
    elif choice == 3:
        exit()
    else:
        print("That wasn't a option!")


def drawshapes():
    print("What shape would you like to draw?")
    print(" 1) Cylinder")
    print(" 2) Octahedron")
    print(" 3) Dodecahedron")
    print(" 4) Back")
    choice = chooseOption(4)
    if choice == 1:
        cyl = cylinder(radius= 5, height= 10, colour= 'turquoise')
        cyl.draw()
        main()
    elif choice == 2:
        octa = Octahedron(edge_length= 5, colour= 'turquoise')
        octa.draw()
        main() 
    elif choice == 3:
        dodeca = Dodecahedron(edge_length= 5, colour= 'turquoise')
        dodeca.draw()
        main()
    elif choice == 4:
        main()
    else:
        print("That wasn't a option!")

def shape_colour():
    print("What shapes colour do you want to change?")
    print(" 1) Cylinder")
    print(" 2) Octahedron")
    print(" 3) Dodecahedron")
    choice = chooseOption(3)
    if choice == 1:
        colour_cyl()
    elif choice == 2:
        colour_octa()
    elif choice == 3:
        colour_dodeca()
    else:
        print("That wasn't a option!")

def colour_cyl():
    print("What colour would you like to change the cylinder to?")
    cyl.colour = input()

def colour_octa():
    pass

def colour_dodeca():
    pass

main()
