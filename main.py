# Counter wtf do I need to explain
counter = int(input("How many Compounds in Formula: "))
listOfInputs = []
while counter > 0:
    f_element = input("Enter Element: ")
    listOfInputs.append(f_element)
    f_element_num = int(input("Enter Element's Coefficient Num: "))
    listOfInputs.append(f_element_num)
    counter = counter - 1
print(listOfInputs)
