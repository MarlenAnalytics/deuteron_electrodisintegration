import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

file_numbers = [1, 50, 100, 200, 400]
file_names = [f"{num}mev.txt" for num in file_numbers]

colors = ['red', 'blue', 'green', 'orange']

d_0 = {"backgroundcolor": "white", "color": "black", "family": "Times New Roman", "size": 8,
     "style": "italic", "weight": "bold"}

plt.figure()

for file_name in file_names:
    data = pd.read_csv(file_name, delim_whitespace=True, header=None)
    
    thr0 = data.iloc[:,4]
    x = data.iloc[:,5]
    crs_n_fd_0 = data.iloc[:,-4]
    crs_n_fd_1 = data.iloc[:,-3]
    crs_n_st = data.iloc[:,-2]
    crs_n_mv = data.iloc[:,-1]
    
    
    plt.plot(thr0, crs_n_st, linestyle='--', color = colors[0])
    plt.plot(thr0, crs_n_mv, linestyle=':', color = colors[1])
    plt.plot(thr0, crs_n_fd_0, linestyle='-', color = colors[2])
    plt.plot(thr0, crs_n_fd_1, linestyle='-', color = colors[3])
    
legend = [Line2D([0], [0], linestyle='--', color=colors[0], label='Free Stationary Nucleon'),
          Line2D([0], [0], linestyle=':', color=colors[1], label='Free Moving Nucleon'),
          Line2D([0], [0], linestyle='-', color=colors[2], label='Moving Nucleon Bound by Deuteron'),
          Line2D([0], [0], linestyle='-', color=colors[3], label='Moving Nucleon Bound and Confound by Deuteron')]

plt.legend(handles=legend, loc='upper right', fontsize=8, fancybox=True, shadow=True)

plt.grid()
plt.xlabel(r"$\theta_{r}$ (degrees)")
plt.ylabel(r"Cross-Section (nb/sr)")
plt.title(r"$Q^2 = 4.0$ $(Gev/c)^2$")

plt.text(184.8, 0.347, "1 Mev/c", fontdict=d_0)
plt.text(184.8, 0.3179, "50 Mev/c", fontdict=d_0)
plt.text(184.8, 0.2581, "100 Mev/c", fontdict=d_0)
plt.text(184.8, 0.1917, "200 Mev/c", fontdict=d_0)
plt.text(184.8, 0.0848, "400 Mev/c", fontdict=d_0)


plt.xticks(np.arange(min(thr0), max(thr0) + 1, 20))

plt.savefig('crs_vs_thr0.png', dpi=300)


plt.show()


plt.figure()

for file_name in file_names:
    data = pd.read_csv(file_name, delim_whitespace=True, header=None)
    
    thr0 = data.iloc[:,4]
    x = data.iloc[:,5]
    crs_n_fd_0 = data.iloc[:,-4]
    crs_n_fd_1 = data.iloc[:,-3]
    crs_n_st = data.iloc[:,-2]
    crs_n_mv = data.iloc[:,-1]
    
    
    plt.plot(x, crs_n_st, linestyle=':', color = colors[0])
    plt.plot(x, crs_n_mv, linestyle='--', color = colors[1])
    plt.plot(x, crs_n_fd_0, linestyle='-', color = colors[2])
    plt.plot(x, crs_n_fd_1, linestyle='-', color = colors[3])
    

new_legend = [Line2D([0], [0], linestyle=':', color=colors[0], label='Free Stationary Nucleon'),
          Line2D([0], [0], linestyle='--', color=colors[1], label='Free Moving Nucleon'),
          Line2D([0], [0], linestyle='-', color=colors[2], label='Moving Nucleon Bound by Deuteron'),
          Line2D([0], [0], linestyle='-', color=colors[3], label='Moving Nucleon Bound and Confound by Deuteron')]
    
    
plt.legend(handles=new_legend, loc='upper left', fontsize=8, fancybox=True, shadow=True)

plt.grid()
plt.xlabel(r"$x_B$")
plt.ylabel(r"Cross-Section (nb/sr)")
plt.title(r"$Q^2 = 4.0$ $(Gev/c)^2$")


plt.text(0.715, 0.314, "50 Mev/c", fontdict=d_0)
plt.text(0.640, 0.273, "100 Mev/c", fontdict=d_0)
plt.text(0.526, 0.1968, "200 Mev/c", fontdict=d_0)
plt.text(0.300, 0.0541, "400 Mev/c", fontdict=d_0)

plt.savefig('crs_vs_xb.png', dpi=300)

plt.show()

    

