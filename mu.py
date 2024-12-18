import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.ticker as ticker

# Read the .dat file and replace commas with dots
with open('data/MuDiffR.dat', 'r') as file:
    data = file.read().replace(',', '.')

# Convert data to a numpy array
data = np.genfromtxt(data.splitlines())

# Extract the 2nd and 3rd columns (H and B respectively)
H = data[:, 1] * 1078.14
B = abs(data[:, 2] * 9780)
#B = B - ((np.max(B) + np.min(B)) * 0.5)

plt.style.use('seaborn-v0_8-paper')
plt.figure(figsize=(8, 6))

plt.plot(H, B, color='blue', linewidth=2)

plt.xlabel(r'$H \, \left[\frac{\mathrm{A}}{\mathrm{m}}\right]$',
           fontsize=20,
           loc='center')
plt.ylabel(
    r'$\mu_{\mathrm{r}} \, \left[\frac{\mathrm{Vs}}{\mathrm{Am}}\right]$',
    fontsize=20,
    rotation=0,
    labelpad=30,
    loc='center')
plt.ylim(bottom=0)
plt.xlim(np.min(H), np.max(H))
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
'''plt.ticklabel_format(axis='both', style='sci', scilimits=(-2, 2))
plt.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)'''
#plt.yticks(np.arange(min(B), max(B), 0.05))

ax = plt.gca()
ax.axhline(0, color='black', linewidth=0.9)
ax.axvline(0, color='black', linewidth=0.9)
ax.xaxis.set_major_formatter(ScalarFormatter())

#start, end = ax.get_ylim()
#x.yaxis.set_ticks(np.arange(start, end, 0.1))
#ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.01f'))
plt.savefig('mu.png', dpi=300)
plt.show()
