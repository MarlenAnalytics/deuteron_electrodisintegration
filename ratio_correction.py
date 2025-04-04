import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

# defining data and iterating through each data file
file_numbers = [1, 4, 8, 12, 16, 18]  # each number correspoonds to momentum-transfer value
file_names = [f"{num}_q2.txt" for num in file_numbers]


line_styles = ['--', ':', '-']
colors = ['red', 'blue', 'black']  # PWIA = Blue (Dashed), FSI = Red (Dotted), Chex = Black (Solid)

plt.figure()

# loop over multiple data files to create plot
for file_name in file_names:
    data = pd.read_csv(file_name, delim_whitespace=True, header=None)

    theta_fq = data.iloc[:, 5].values   # polar angle of struck nucleon with respect to virtual photon, q.
    pwia = data.iloc[:, -3].values      # plane wave impulse approximation
    fsi = data.iloc[:, -2].values       # final state interaction
    chex = data.iloc[:, -1].values      # charge exchange

    # interpolating all y values to simulate cross-section
    # at all theta values ranging between 0 and 8 degrees
    theta_smooth = np.linspace(theta_fq.min(), theta_fq.max(), 300)

    
    pwia_smooth = make_interp_spline(theta_fq, pwia, k=3)(theta_smooth)
    fsi_smooth = make_interp_spline(theta_fq, fsi, k=3)(theta_smooth)
    chex_smooth = make_interp_spline(theta_fq, chex, k=3)(theta_smooth)


    plt.plot(theta_smooth, pwia_smooth, line_styles[0], color=colors[0])
    plt.plot(theta_smooth, fsi_smooth, line_styles[1], color=colors[1])
    plt.plot(theta_smooth, chex_smooth, line_styles[2], color=colors[2])
    

# dictionary for curve labels
d_0 = {"backgroundcolor": "white", "color": "black", "family": "Times New Roman", "size": 8,
     "style": "italic", "weight": "bold"}

# custom legend to show final states
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], linestyle='--', color=colors[0], label='PWIA'),
    Line2D([0], [0], linestyle=':', color=colors[1], label='FSI'),
    Line2D([0], [0], linestyle='-', color=colors[2], label='CHEX')
]
plt.legend(handles=legend_elements, loc='lower left', fontsize=8)


plt.text(8.2, 0.90, r"$1.0$", fontdict=d_0)
plt.text(8.2, 0.84, r"$4.0$", fontdict=d_0)
plt.text(8.2, 0.81, r"$8.0$", fontdict=d_0)
plt.text(7.6, 0.58, r"$12.0$", fontdict=d_0)
plt.text(5.6, 0.61, r"$16.0$", fontdict=d_0)
plt.text(4.5, 0.75, r"$18.0$", fontdict=d_0)

plt.grid()
plt.xlabel(r'$\theta_{pq}$ (degrees)')
plt.title('Ratio Correction Factor')

plt.savefig('rcf_smooth_updt.png', dpi=300)

plt.show()


