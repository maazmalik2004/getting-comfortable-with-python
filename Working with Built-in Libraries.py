import math

print(math.sqrt(16))
print(math.factorial(5))

with open('example.txt','w') as file:
    file.write('Hello, world!')

with open('example.txt','r') as file:
    content = file.read()
    print(content)

import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%d %H:%M:%S"))