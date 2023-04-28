list1=list()#THis lists all the values satisfying the conditions
for n in range(1, 200): #We take the range of said integer 'n' in between 1 to 200 as mentioned in the question
    if n % 5 == 2 and n % 6 == 3 and n % 7 == 2:  #These are the constraints on the value of 'n' provided by the question
        print("The candy bowl contains", n, "pieces of candy.")
        list1.append(n)
print(list1)
