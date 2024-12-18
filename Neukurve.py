import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker

with open('data/NeukurveInvertiert.dat', 'r') as file:
    data = file.read().replace(',', '.')

data = np.genfromtxt(data.splitlines())
# Ersten 100 in gruen

data[:,2] = data[:,2] - ((np.max(data[:, 2]) + np.min(data[:,2])) * 0.5)

Hn = -1 * data[:100, 1] * 1078.14
Bn = -1 * data[:100, 2] * 0.29389
H = -1 * data[100:, 1] * 1078.14
B = -1 * data[100:, 2] * 0.29389

plt.style.use('seaborn-v0_8-paper')
plt.figure(figsize=(8, 6))
plt.plot(H, B, color='blue', linewidth=2)
plt.plot(Hn, Bn, color='green', linewidth=2)

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.xlabel(r'$H \, [\mathrm{\frac{A}{m}}]} $', fontsize=30)
plt.ylabel(r'$B \, \left[T\right]$',
           fontsize=30,
           rotation=0,
           labelpad=25,
           loc='center')

plt.xlim(np.min(H)+1500, np.max(H)-1500)

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

plt.savefig('Neukurve.png', dpi=600, bbox_inches = "tight")

plt.show()
