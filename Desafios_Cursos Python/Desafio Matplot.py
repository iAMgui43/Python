from math import sqrt
import matplotlib.pyplot as plt

#Dada a equação da cirunferência, faça o gráfico. (x − a)²+(y-b)² = r², r = 100, a = 100, b = 100

a, b, r = 100, 100, 100
x = []
y = []

x = [i for i in range(2*r +1)]
y_x = lambda x: sqrt((r**2)- (x-a)**2) + b
y_x_menos = lambda x: -sqrt((r**2)- (x-a)**2) + b

y.extend(list(map(y_x,x)))
y.extend(list(map(y_x_menos,x)))

x.extend(x)


         
print(y)

plt.plot(x, y, '-')
plt.show()