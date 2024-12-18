import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker

# Read the .dat file and replace commas with dots
with open('data/entmagnetisierung.dat', 'r') as file:
    data = file.read().replace(',', '.')

# Convert data to a numpy array
data = np.genfromtxt(data.splitlines())

# Extract the 2nd and 3rd columns (H and B respectively)
H = data[:, 1] * 1087.14
B = data[:, 2] * 0.2938
B = B - ((np.max(B) + np.min(B)) * 0.5) - 0.04

plt.style.use('seaborn-v0_8-paper')
plt.figure(figsize=(8, 6))

plt.plot(H, B, color='blue', linewidth=0.6)

plt.xlabel(r'$H \, [\mathrm{\frac{A}{m}}]} $', fontsize=20)
plt.ylabel(r'$B \, \left[T\right]$',
           fontsize=20,
           rotation=0,
           labelpad=25,
           loc='center')

plt.xlim(-1500, 1500)

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.ticklabel_format(axis='both', style='sci', scilimits=(-2, 2))
plt.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)

ax = plt.gca()
ax.axhline(0, color='black', linewidth=0.9)
ax.axvline(0, color='black', linewidth=0.9)
ax.xaxis.set_major_formatter(ScalarFormatter())

plt.savefig('Entmagnetisierung.png', dpi=600)

plt.show()
