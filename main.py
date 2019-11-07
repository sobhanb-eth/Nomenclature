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
print(element_List)
# list for elements
Alkali_list = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
AlkalineEarth_list = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra', 'None']
Icosagens_list = ['B', 'Al', 'Ga', 'In', 'Tl', 'None', 'None']
Crystal_list = ['C', 'Si', 'Ge', 'Sn', 'Pb', 'None', 'None']
Pnicto_list = ['N', 'P', 'As', 'Sb', 'Bi', 'Null', 'Null']
Chalco_list = ['O', 'S', 'Se', 'Te', 'Po', 'Null', 'Null']
Halo_list = ['F', 'Cl', 'Br', 'I', 'At', 'Null', 'Null']
Noble_list = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'null']

### TODO: Input Analysis
input_ctrlf = counter
i = 0
x = 0
while i < input_ctrlf:
    for element_list in Alkali_list, AlkalineEarth_list, Icosagens_list, Crystal_list, Pnicto_list, Crystal_list, Halo_list, Noble_list:
        for elem_input in element_List:
            print("------% Inner Loop %------", i)
            if element_List[i] == Alkali_list[x]:
                print("Element ", Alkali_list[x], " and" " is in Alkali Group.")
            elif element_List[i] == AlkalineEarth_list[x]:
                print("Element ", AlkalineEarth_list[x], " is in Alkaline Earth Group.")
            elif element_List[i] == Icosagens_list[x]:
                print("Element ", Icosagens_list[x], " is in Icosagens Group.")
            elif element_List[i] == Crystal_list[x]:
                print("Element ", Crystal_list[x], " is in Crystals Group.")
            elif element_List[i] == Pnicto_list[x]:
                print("Element ", Pnicto_list[x], " is in Pnicto Group.")
            elif element_List[i] == Chalco_list[x]:
                print("Element ", Chalco_list[x], " is in Chalco Group.")
            elif element_List[i] == Halo_list[x]:
                print("Element ", Halo_list[x], " is in Halogens Group.")
            elif element_List[i] == Noble_list[x]:
                print("Element ", Noble_list[x], " is in Noble Gases Group.")
            else:
                print("PATLADIK ANNAAAAM!")
                print(i)
                print(element_List[i])
                print(x)
                print(Alkali_list[x], AlkalineEarth_list[x], Icosagens_list[x], Crystal_list[x], Pnicto_list[x], Chalco_list[x], Halo_list[x], Noble_list[x])
                break
        break
    i += 1
    x += 1
