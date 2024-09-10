def bubbleSort(list):
    n = len(list)
    #outer loop keeps track of the number of comparisions to be made in each iteration
    for i in range(n-1,0,-1):#n-1 is included and 0 is excluded. from n-1 to >0... last number of comparisions will be 1
        #inner loop actually performs the comparisions
        for j in range(i-1,-1,-1):
            print(f"{j} and {j+1}")
            if list[j] < list[j+1]:
                #interview question : swap two numbers without using tmp
                swap(list, j, j+1)

def swap(list, i, j):
    list[i] = list[i]+list[j]
    list[j]=list[i]-list[j]
    list[i]=list[i]-list[j]

myList = [64, 25, 12, 22, 11]
bubbleSort(myList)
print(myList)