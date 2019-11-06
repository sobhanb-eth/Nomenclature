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
AlkalineEarth_list = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra','None']
Icosagens_list = ['B', 'Al', 'Ga', 'In', 'Tl','None','None']
Crystal_list = ['C', 'Si', 'Ge', 'Sn', 'Pb','None','None']
Pnicto_list = ['N', 'P', 'As', 'Sb', 'Bi','Null','Null']
Chalco_list = ['O', 'S', 'Se', 'Te', 'Po','Null','Null']
Halo_list = ['F', 'Cl', 'Br', 'I', 'At','Null','Null']
Noble_list = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn','null']

### TODO
i = 0
x = 0
# while i < 8:
#     print("len of input is: ", len(listOfInputs))
#     for x in range(len(Alkali_list)):
#         if listOfInputs[i] == Alkali_list[x]:
#             check = 1
#             print(Alkali_list[x])
#         elif listOfInputs[i] == AlkalineEarth_list[x]:
#             check = 1
#             print(AlkalineEarth_list[x])
#     i += 1

for element in Alkali_list:
    for elem in listOfInputs:
        if listOfInputs[i] == Alkali_list[x]:
            print(Alkali_list[x])
            break
        else:
            print("Element Not Found!")
        i += 1
    break
