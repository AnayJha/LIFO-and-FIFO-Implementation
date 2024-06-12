lst = []
queue = ''
while queue != 'x':
    queue = input("Enter a number: ")
    if queue != "x":
        lst.append(queue)
        
        
print(lst)
   
print('0->Exit')
print('1->LIFO')
print('2->FIFO')
order = -1
while order != 0:
    order = int(input("Enter input: "))
    if order == 1:
        len_list = len(lst)
        acounter = len_list - 1 
        while acounter >=0 :
            print(lst[acounter])
            acounter = acounter - 1 
    elif order == 2:
        len_list = len(lst)
        acounter =  0 
        while acounter >=0 and acounter < len_list :
            print(lst[acounter])
            acounter = acounter + 1 
    elif order == 0:
        print("------- Exited Programme -------")
        break
    else:
        print(" ")
        print("Invalid entry!")
        print("Enter a valid input")
        print(" ")