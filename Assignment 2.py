lst = [1,2,3,4]

# deleting an element at the begning position
for i in range(len(lst)-1):
    lst[i] = lst[i+1]
    i -= 1 
print(lst)


# Deleting element atany position
p = 2
for i in range(len(lst)-1,p-1,-1):
    lst[i+1] = lst[i]
    i-=1
    
print(lst)


#Rotatin the list to left for k times
k = int(input())

length = len(lst)-1


for j in range(k):
    temp = lst[0]
    for i in range(length):
        lst[i] = lst[i+1]
    lst[length] = temp
print(lst)




