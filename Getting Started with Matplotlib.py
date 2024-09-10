import matplotlib.pyplot as plt
import numpy as np
'''
x = np.linspace(0,10,100)#100 points between 0 and 10
y = np.sin(x)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('simple line plot')

plt.plot(x,y)
plt.show()
plt.scatter(x,y)
plt.show()
plt.bar(x,y)
plt.show()

data = np.random.randn(1000)

plt.hist(data, bins=30)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

plt.show()


fig, ax = plt.subplots(2,1)#multiple plots in a single figure
x = np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)

ax[0].plot(x,y1,'r')#r stands for red color
ax[0].set_title('sine')
ax[1].plot(x,y2)
ax[1].set_title('cosine')

plt.show()

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)', color='red')

plt.legend()

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sine and Cosine Waves')

plt.show()

plt.plot(x, y1, color='green', linestyle='--', marker='o', label='sin(x)')
plt.plot(x, y2, color='blue', linestyle='-', marker='x', label='cos(x)')

plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Customized Sine and Cosine Waves')

plt.show()
'''

image = np.random.rand(10,10,3)#dimentions of random image 100x100x3 where 3 stands for rgb channels
plt.imshow(image)
plt.show()