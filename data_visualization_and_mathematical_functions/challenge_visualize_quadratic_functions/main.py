import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(a, b, c):
    # Write your code here
    x = np.linspace(-10,10,400)
    y = a*(x**2) + b*x + c
    
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Graph of the quadratic function y ={a}x^2 + {b}x + {c}")
    plt.grid(True)
    plt.show()
# Test with a = 1, b = -2, c = 1
plot_quadratic(1, -2, 1)
