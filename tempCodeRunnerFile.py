import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as curve_fit

# Read the CSV file and replace commas with dots
data = np.genfromtxt('data/magnetMessung.csv', delimiter=',', skip_header=1)

# Convert the processed string data to a numpy array

# Extract the 1st and 4th columns (x and y respectively)
x = data[:, 0]  # First column for x-axis
y = data[:, 3]  # Fourth column for y-axis

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, '-bs', linewidth=2)


def ln_func(x, a, b):
    return a * np.log(x) + b

# Perform curve fitting (logarithmic regression)
popt, pcov = curve_fit(ln_func, x, y)
a, b = popt

x_fit = np.linspace(min(x_data), max(x_data), 500)
y_fit = ln_func(x_fit, a, b)

plt.plot(x_fit,
         y_fit,
         label=f'Fitted ln(x) Function: {a:.2f}ln(x) + {b:.2f}',
         color='red')


# Add labels to the axes
plt.xlabel(r'$I \, \left[A\right]$', fontsize=30, loc='center')
plt.ylabel(r'$B \, \left[T\right]$',
           fontsize=30,
           rotation=0,
           labelpad=40,
           loc='center')

plt.ylim((0, 2))
plt.xlim((0, 30))

# Display grid and the plot
plt.grid(True)
plt.tight_layout()

plt.savefig('eMagnet.png', dpi=600)
plt.show()
