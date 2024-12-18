import numpy as np
import matplotlib.pyplot as plt

# Read the .dat file and replace commas with dots
with open('data/frequenzErhoehen.dat', 'r') as file:
    data = file.read().replace(',', '.')

# Convert data to a numpy array
data = np.genfromtxt(data.splitlines())

# Extract the 2nd and 3rd columns (H and B respectively)
H = data[:, 1] * 0.107815
B = data[:, 2] * 0.2938
B = B - ((np.max(B) + np.min(B)) * 0.5)

plt.style.use('seaborn-v0_8-paper')
plt.figure(figsize=(8, 6))

plt.plot(H, B, color='blue', linewidth=2)

plt.xlabel(r'$H \, [\mathrm{A/m}], 10^3 $', fontsize=14)
plt.ylabel(r'$\mu_{\mathrm{diff}} \, [\mathrm{Vs/Am}]$', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)
plt.title('B-H-Kenninie', fontsize=16)
plt.tight_layout()

plt.ticklabel_format(axis='both', style='sci', scilimits=(-2, 2))
plt.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)

ax = plt.gca()
ax.axhline(0, color='black', linewidth=0.9)
ax.axvline(0, color='black', linewidth=0.9)

plt.savefig('Entmagnetisierung.png', dpi=600)

plt.show()
