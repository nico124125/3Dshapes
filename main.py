import pyvista as pv
from shapes3D import ThreeDShape, cylinder, Octahedron, Dodecahedron
import shapes3D

print("Welcome to the 3D Shape Drawing Program!")
print(" 1) Draw a shape")
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

def drawshapes():
    print("What shape would you like to draw?")
    print(" 1) Cylinder")
    print(" 2) Octahedron")
    print(" 3) Dodecahedron")
    choice = chooseOption(3)
    if choice == 1:
        shapes3D.draw
    elif choice == 2:
        pass
    elif choice == 3:
        pass

choice = chooseOption(1)
print(choice)
if choice == 1:
    pass
else:
    print("That wasn't a option!")
