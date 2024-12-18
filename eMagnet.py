import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file and replace commas with dots
data = np.genfromtxt('data/magnetMessung.csv',
                     delimiter=',',
                     skip_header=1)

print(data)
# Convert the processed string data to a numpy array

# Extract the 1st and 4th columns (x and y respectively)
x = data[:, 0]  # First column for x-axis
y = data[:, 3]  # Fourth column for y-axis

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, '-bs', linewidth=2)

# Add labels to the axes
plt.xlabel('I [A]', fontsize=14)
plt.ylabel('B [T]', fontsize=14)

plt.xlabel(r'$I \, \left[A\right]$', fontsize=20, loc='center')
plt.ylabel(r'$B \, \left[T\right]$',
           fontsize=20,
           rotation=0,
           labelpad=25,
           loc='center')

plt.ylim((0,2))
plt.xlim((0,30))

# Display grid and the plot
plt.grid(True)
plt.tight_layout()

plt.savefig('eMagnet.png', dpi=600)
plt.show()
