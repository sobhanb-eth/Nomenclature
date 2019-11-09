from typing import List, Union

counter = int(input("Number of the elements of compound: "))
ctrl = 1
element_List = []
coefficient_List = []

while ctrl <= counter:

    if ctrl == 1 or counter == 21:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "st element: ")
        coefficient_no = input("Enter the COEFFICIENT Number of the " + str(ctrl) + "st element: ")
    elif ctrl == 2 or ctrl == 22 or ctrl == 32:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "nd element: ")
        coefficient_no = input("Enter the COEFFICIENT NUMBER of the " + str(ctrl) + "nd element: ")
    elif ctrl == 3 or ctrl == 23 or ctrl == 33:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "rd element: ")
        coefficient_no = input("Enter the COEFFICIENT NUMBER of the " + str(ctrl) + "rd element: ")
    else:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "th element: ")
        coefficient_no = input("Enter the COEFFICIENT NUMBER of the " + str(ctrl) + "th element: ")
    element_List.append(element_input)
    coefficient_List.append(coefficient_no)

    ctrl = ctrl + 1

# list for elements

Alkali_list = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
AlkalineEarth_list = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra', 'None']
Icosagens_list = ['B', 'Al', 'Ga', 'In', 'Tl', 'None', 'None']
Crystal_list = ['C', 'Si', 'Ge', 'Sn', 'Pb', 'None', 'None']
Pnicto_list = ['N', 'P', 'As', 'Sb', 'Bi', 'Null', 'Null']
Chalco_list = ['O', 'S', 'Se', 'Te', 'Po', 'Null', 'Null']
Halo_list = ['F', 'Cl', 'Br', 'I', 'At', 'Null', 'Null']
Noble_list = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'null']
Metals = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra', 'Al', 'Ga', 'In', 'Tl', 'Sn', 'Pb',
          'Bi', 'Po']
Non_Metals = ['H', 'C', 'N', 'P', 'O', 'S', 'Se', 'F', 'Cl', 'Br', 'I', 'At', 'He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
Metalloids = ['B', 'Si', 'Ge', 'As', 'Sb', 'Te', 'Po']
# TODO: Naming The Elements
n_Alkali_list = ['Hydrogen', 'Lithium', 'Sodium', 'Potassium', 'Rubidium', 'Cesium', 'Francium']
n_AlkalineEarth_list = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium', 'None']
n_Icosagens_list = ['Boron', 'Aluminum', 'Gallium', 'Indium', 'Thallium', 'null', 'null']
n_Crystal_list = ['Carbon', 'Silicon', 'Germanium', 'Tin', 'Lead', 'null', 'null']
n_Pnicto_list = ['Nitrogen', 'Phosphorus', 'Arsenic', 'Antimony', 'Bismuth', 'null', 'null']
n_Chalco_list = ['Oxygen', 'Sulfur', 'Selenium', 'Tellurium', 'Polonium', 'null', 'null']
n_Halo_list = ['Fluorine', 'Chlorine', 'Bromine', 'Iodine', 'Astatine', 'null', 'null']
n_Noble_list = ['Helium', 'Neon', 'Argon', 'Krypton', 'Xenon', 'Radon', 'null']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# TODO: Input Analysis: 1) First Phase of detecting Input's group type => DONE!
# TODO: Input Analysis: 2) Second Phase Element Type : Metal - NonMetal - Ion => DONE!
# TODO: Input Analysis: 3) 3rd Phase Bond Type Detection => DONE!

n_input_ctrlf = counter
i = 0
metal = 0
nonmetal = 0
metalloid = 0
result_list = []
while i < n_input_ctrlf:
    if element_List[i] in Alkali_list:
        print("Element '", element_List[i], "' is in Alkali Group.", end='')
        if element_List[i] in Metals:
            print(" And It is Metal")
            metal = 1
        elif element_List[i] in Non_Metals:
            print(" And It is Non-Metal")
            nonmetal = 1
        else:
            print("And It is Metalloid")
            metalloid = 1
    elif element_List[i] in AlkalineEarth_list:
        print("Element '", element_List[i], "' is in Alkaline Earth Group.", end='')
        if element_List[i] in Metals:
            metal = 1
            print(" And It is Metal")
        else:
            print(" And It is Non-Metal")
            nonmetal = 1
    elif element_List[i] in Icosagens_list:
        print("Element '", element_List[i], "' is in Icosagens Group.", end='')
        if element_List[i] in Metals:
            print(" And It is Metal")
            metal = 1
        elif element_List[i] in Non_Metals:
            print(" And It is Non-Metal")
            nonmetal = 1
        else:
            print("And It is Metalloid")
            metalloid = 1
    elif element_List[i] in Crystal_list:
        print("Element '", element_List[i], "' is in Crystals Group.", end='')
        if element_List[i] in Metals:
            print(" And It is Metal")
            metal = 1
        elif element_List[i] in Non_Metals:
            print(" And It is Non-Metal")
            nonmetal = 1
        else:
            print("And It is Metalloid")
            metalloid = 1
    elif element_List[i] in Pnicto_list:
        print("Element ''", element_List[i], "' is in Pnicto Group.", end='')
        if element_List[i] in Metals:
            print(" And It is Metal")
            metal = 1
        elif element_List[i] in Non_Metals:
            print(" And It is Non-Metal")
            nonmetal = 1
        else:
            print("And It is Metalloid")
            metalloid = 1
    elif element_List[i] in Chalco_list:
        print("Element ''", element_List[i], "' is in Chacos Group.", end='')
        if element_List[i] in Metals:
            print(" And It is Metal")
            metal = 1
        elif element_List[i] in Non_Metals:
            print(" And It is Non-Metal")
            nonmetal = 1
        else:
            print("And It is Metalloid")
            metalloid = 1
    elif element_List[i] in Halo_list:
        print("Element '", element_List[i], "'  is in Halogens Group.", end='')
        if element_List[i] in Metals:
            print(" And It is Metal")
            metal = 1
        elif element_List[i] in Non_Metals:
            print(" And It is Non-Metal")
            nonmetal = 1
        else:
            print("And It is Metalloid")
            metalloid = 1
    elif element_List[i] in Noble_list:
        print("Element ''", element_List[i], "' is in Nobel Gases Group.", end='')
        if element_List[i] in Metals:
            print(" And It is Metal")
            metal = 1
        elif element_List[i] in Non_Metals:
            print(" And It is Non-Metal")
            nonmetal = 1
    result_list.append(element_List[i])
    i += 1
print(result_list)
naming_list = []
### TODO: Turn Symbols to names
i = 0
x = 0
while i < len(result_list):
    while x < 7:
        if result_list[i] in Alkali_list[x]:
            naming_list.append(n_Alkali_list[x])
            break
        elif result_list[i] in AlkalineEarth_list[x]:
            naming_list.append(n_AlkalineEarth_list[x])
            break
        elif result_list[i] in Icosagens_list[x]:
            naming_list.append(n_Icosagens_list[x])
            break
        elif result_list[i] in Crystal_list[x]:
            naming_list.append(n_Crystal_list[x])
            break
        elif result_list[i] in Pnicto_list[x]:
            naming_list.append(n_Pnicto_list[x])
            break
        elif result_list[i] in Chalco_list[x]:
            naming_list.append(n_Chalco_list[x])
            break
        elif result_list[i] in Halo_list[x]:
            naming_list.append(n_Halo_list[x])
            break
        elif result_list[i] in Noble_list[x]:
            naming_list.append(n_Noble_list[x])
            break

        x += 1
    i += 1
print(naming_list)
# TODO: Bond Type Detection -> DONE!

covelant = 0
ionic = 0
metalic = 0
if metal == 1 and nonmetal == 1:
    print('Ionic Bond')
    ionic = 1
elif metal == 0 and nonmetal == 1 and metalloid == 0:
    print('Covalent bond')
    covelant = 1
elif metal == 1 and metalloid == 0 and nonmetal == 0:
    print('Metallic Bonding')
    metalic = 1
print(covelant, ionic, metalic)


def roman_number_switcher(argument):
    switcher = {
        1: "mono",
        2: "di",
        3: "tri",
        4: "tetra",
        5: "penta",
        6: "hex",
        7: "hept",
        8: "oct",
        9: "non",
        10: "dec",
    }
    return switcher.get(argument, "Invalid Number!")


# TODO: Check the Number of Coeficients of each Element => if it is GREATER than "1" and it is Covelant then proceed
#  to add Mono - di - tri etc.
c_input_ctrlf = counter
x = 0
if covelant == 1:
    while x < c_input_ctrlf:
        if coefficient_List[x] in numbers:
            if int(coefficient_List[0]) == 1 and x == 0:
                print(naming_list[x], end=" ")
            else:
                print(roman_number_switcher(int(coefficient_List[x])), naming_list[x], end=" ")
        x += 1

# TODO: Define fixed case: Carbide, Nitride, Oxide, Fluoride, Phosphide, Sulfide, Chloride, Selenide, Bromide,
#  Telluride, Iodide, etc

# TODO: Special Case of OH (Hydroxides)
# TODO: Special Case for NH4 NH3 etc
# TODO:
