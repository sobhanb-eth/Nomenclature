counter = int(input("Number of the elements of compound: "))
ctrl = 1
element_List = []
coefficient_List = []

while ctrl <= counter:

    if ctrl == 1 or counter == 21:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "st element: ")
        coefficient_no = input("Enter the Number of the " + str(ctrl) + "st element: ")
    elif ctrl == 2 or ctrl == 22 or ctrl == 32:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "nd element: ")
        coefficient_no = input("Enter the NUMBER of the " + str(ctrl) + "nd element: ")
    elif ctrl == 3 or ctrl == 23 or ctrl == 33:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "rd element: ")
        coefficient_no = input("Enter the NUMBER of the " + str(ctrl) + "rd element: ")
    else:
        element_input = input("Enter the SYMBOL of the " + str(ctrl) + "th element: ")
        coefficient_no = input("Enter the NUMBER of the " + str(ctrl) + "th element: ")
    element_List.append(element_input)
    coefficient_List.append(coefficient_no)

    ctrl = ctrl + 1
# print(element_List)
# list for elements
Alkali_list = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
AlkalineEarth_list = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra', 'None']
Icosagens_list = ['B', 'Al', 'Ga', 'In', 'Tl', 'None', 'None']
Crystal_list = ['C', 'Si', 'Ge', 'Sn', 'Pb', 'None', 'None']
Pnicto_list = ['N', 'P', 'As', 'Sb', 'Bi', 'Null', 'Null']
Chalco_list = ['O', 'S', 'Se', 'Te', 'Po', 'Null', 'Null']
Halo_list = ['F', 'Cl', 'Br', 'I', 'At', 'Null', 'Null']
Noble_list = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'null']

### TODO: Input Analysis: 1) First Phase of detecting Input's group type => DONE!
### TODO: Input Analysis: 2) Second Phase Element Type : Metal - NonMetal - Ion
### TODO: Input Analysis: 3) 3rd Phase Bond Type Detection
input_ctrlf = counter
i = 0
while i < input_ctrlf:
    if element_List[i] in Alkali_list:
        print("Element '", element_List[i], "' is in Alkali Group.")
    elif element_List[i] in AlkalineEarth_list:
        print("Element '", element_List[i], "' is in Alkaline Earth Group.")
    elif element_List[i] in Icosagens_list:
        print("Element '", element_List[i], "' is in Icosagens Group.")
    elif element_List[i] in Crystal_list:
        print("Element '", element_List[i], "' is in Crystals Group.")
    elif element_List[i] in Pnicto_list:
        print("Element ''", element_List[i], "' is in Pnicto Group.")
    elif element_List[i] in Chalco_list:
        print("Element ''", element_List[i], "' is in Chacos Group.")
    elif element_List[i] in Halo_list:
        print("Element '", element_List[i], "'  is in Halogens Group.")
    elif element_List[i] in Noble_list:
        print("Element ''", element_List[i], "' is in Nobel Gases Group.")
    i += 1

### TODO: Bond Type Detection
### TODO: Check the Number of Coeficients of each Element => if it is GREATER than "1" and it is Covelant then proceed to add Mono - di - tri etc.
### TODO: Define fixed case: Carbide, Nitride, Oxide, Fluoride, Phosphide, Sulfide, Chloride, Selenide, Bromide, Telluride, Iodide,
### TODO: Special Case of OH (Hydroxides)
### TODO: Special Case for NH4 NH3 etc
### TODO: