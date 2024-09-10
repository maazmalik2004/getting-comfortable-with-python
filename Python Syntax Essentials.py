#data type declaration is not required
x = 10
y = 2.5
name = "python"

sum = x+y
div = x/y

if x>5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

for i in range(5):
    print(i)

while x>0:
    print(x)
    x-=1

#list comprehension: will copy all the even elements. its like .filter in js
numbers = [x for x in range(10) if x%2==0]

myList = [1,2,3]
myList.append(4)
myTuple = (1,2,3)
mySet = {1,2,2,3}
myDict = {'key':'value','age':25}
print(myList)
print(myTuple)
print(mySet)
print(myDict)

#in python a simple list can be used as a stack
stack = [1,2,3]
stack.pop()
stack.append(4)
print(stack)