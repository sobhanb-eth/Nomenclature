# Counter wtf do I need to explain
counter = int(input("How many Compounds in Formula: "))
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
AlkalineEarth_list = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
Icosagens_list = ['B', 'Al', 'Ga', 'In', 'Tl']
Crystal_list = ['C', 'Si', 'Ge', 'Sn', 'Pb']
Pnicto_list = ['N', 'P', 'As', 'Sb', 'Bi']
Chalco_list = ['O', 'S', 'Se', 'Te', 'Po']
Halo_list = ['F', 'Cl', 'Br', 'I', 'At']
Noble_list = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
