import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read the CSV file and replace commas with dots
data = np.genfromtxt('data/magnetMessung.csv', delimiter=',', skip_header=1)

# Extract the 1st and 4th columns (x and y respectively)
x = data[:, 0]  # First column for x-axis
y = data[:, 3]  # Fourth column for y-axis

# Ensure all x values are positive for logarithmic fitting
valid_indices = x > 0
xl = x[valid_indices]
yl = y[valid_indices]

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, '-bs', linewidth=2, label='Messpunkte')


# Define the shifted logarithmic function
def shifted_ln_func(x, a, b, c):
    return a * np.log(x + c) + b


# Perform curve fitting with a shift in the logarithmic function
popt, pcov = curve_fit(shifted_ln_func, x, y,
                       p0=[1, 1, 0.1])  # Initial guesses for a, b, c
a, b, c = popt

# Generate the regression curve
x_fit = np.linspace(min(x), max(xl), 500)
y_fit = shifted_ln_func(x_fit, a, b, c)

# Plot the regression curve
plt.plot(x_fit,
         y_fit,
         label=f'Approximierte ln-Funktion',
         color='red')

# Add labels to the axes
plt.xlabel(r'$I \, \left[A\right]$', fontsize=30, loc='center')
plt.ylabel(r'$B \, \left[T\right]$',
           fontsize=30,
           rotation=0,
           labelpad=40,
           loc='center')

# Set axis limits
plt.ylim((0, 2))
plt.xlim((0, 30))

# Display grid and customize the plot
plt.grid(True)
plt.legend(fontsize=14)
plt.tight_layout()

# Save the plot
plt.savefig('eMagnet.png', dpi=600)

# Show the plot
plt.show()
