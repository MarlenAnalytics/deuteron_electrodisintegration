import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# initializing and defining data
file_numbers = [1, 4, 10, 18]
file_names = [f"{num}_q2.txt" for num in file_numbers]

colors = ['red', 'blue', 'green']

plt.figure()

# iterating through data files to plot data
for file_name in file_names:
    data = pd.read_csv(file_name, delim_whitespace=True, header=None)
    
    theta_fq = data.iloc[:, 4]      # polar angle of struck nucleon with respect to q
    crs_n_st = data.iloc[:,-1]      # cross-section of stationary neutron
    fsi = data.iloc[:,-3]           # final state interaction cross-section
    chex = data.iloc[:,-2]          # charge exchange cross-section

    
    plt.plot(theta_fq, crs_n_st, linestyle='--', color=colors[0])
    plt.plot(theta_fq, fsi, linestyle='-', color=colors[1])
    plt.plot(theta_fq, chex, color=colors[2])
    

# creating legend
legend = [Line2D([0], [0], linestyle='--', color=colors[0], label='Stationary Nucleon'),
          Line2D([0], [0], linestyle='-', color=colors[1], label='FSI'),
          Line2D([0], [0], linestyle='-', color=colors[2], label='FSI+CHEX')]



plt.legend(handles=legend, loc='upper right', fontsize=8, bbox_to_anchor=(1.1, 1.1), fancybox=True, shadow=True)

# creating dictionary for labeling each respective group of curves
d_0 = {"backgroundcolor": "white", "color": "black", "family": "Times New Roman", "size": 8,
     "style": "italic", "weight": "bold"}

plt.text(7.6, 2.1e-08, r"$Q^2 = 18.0$ $(GeV/c)^2$", fontdict=d_0)
plt.text(7.6, 0.000150, r"$Q^2 = 10.0$ $(GeV/c)^2$", fontdict=d_0)
plt.text(7.6, 8.5, r"$Q^2 = 4.0$ $(GeV/c)^2$", fontdict=d_0)
plt.text(7.6, 15319, r"$Q^2 = 1.0$ $(GeV/c)^2$", fontdict=d_0)

plt.grid()
plt.xlabel(r'$\theta_{pq}$ (degrees)')
plt.ylabel(r'Cross-Section (nb/sr)')
plt.title(r'$x_B = 1.0$')
plt.yscale('log')

plt.savefig('Q2_x1.png', dpi=300)

plt.show()