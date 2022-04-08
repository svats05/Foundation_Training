def bubble(list1):  
    for j in range(len(list1)-1):  
        if(list1[j]>list1[j+1]):  
            temp = list1[j]  
            list1[j] = list1[j+1]  
            list1[j+1] = temp  
    return list1  
  
list1 = list(map(int,input("Enter the list: ").split(",")))  
print("Sorted list is: ", bubble(list1))  
