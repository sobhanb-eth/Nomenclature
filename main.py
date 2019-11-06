# Counter wtf do I need to explain
counter = int(input("How many Compounds in Formula: "))
s_counter = counter
# list for storage of inputs
listOfInputs = []
# iterative loop for inputs
while counter > 0:
    f_element = input("Enter Element: ")
    listOfInputs.append(f_element)
    f_element_num = int(input("Enter Element's Coefficient Num: "))
    listOfInputs.append(f_element_num)
    counter = counter - 1
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
i = 0
x = 0
# while is_Found == 0:
for element_list in Alkali_list, AlkalineEarth_list, Icosagens_list, Crystal_list, Pnicto_list, Crystal_list, Halo_list, Noble_list:
    for elem_input in listOfInputs:
        if listOfInputs[i] == Alkali_list[x]:
            print("Element ", Alkali_list[x], " is in Alkali Group.")
        elif listOfInputs[i] == AlkalineEarth_list[x]:
            print("Element ", AlkalineEarth_list[x], " is in Alkaline Earth Group.")
        elif listOfInputs[i] == Icosagens_list[x]:
            print("Element ", Icosagens_list[x], " is in Icosagens Group.")
        elif listOfInputs[i] == Crystal_list[x]:
            print("Element ", Crystal_list[x], " is in Crystals Group.")
        elif listOfInputs[i] == Pnicto_list[x]:
            print("Element ", Pnicto_list[x], " is in Pnicto Group.")
        elif listOfInputs[i] == Chalco_list[x]:
            print("Element ", Chalco_list[x], " is in Chalco Group.")
        elif listOfInputs[i] == Halo_list[x]:
            print("Element ", Halo_list[x], " is in Halogens Group.")
        elif listOfInputs[i] == Noble_list[x]:
            print("Element ", Noble_list[x], " is in Noble Gases Group.")
        else:
            print("heyvaaan Yanlis Yaptin bole bisey Yok")
            break
        i += 1
        break
    break
