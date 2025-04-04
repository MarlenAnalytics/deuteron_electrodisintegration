import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


#importing data
file_numbers = [1, 50, 100]
file_names = [f"{num}mev.txt" for num in file_numbers]

plt.figure()

for file_name in file_names:
     data = pd.read_csv(file_name, delim_whitespace=True, header=None)
     
     theta = data.iloc[:, 4].values
     r_0 = data.iloc[:, 6].values
     r_12 = data.iloc[:, 7].values
     r_123 = data.iloc[:, 8].values
     r_s = data.iloc[:, 9].values
     
     plt.plot(theta, r_0, 'r-')
     plt.plot(theta, r_12, 'b-')
     plt.plot(theta, r_123, 'g-')
     plt.plot(theta, r_s, 'y-')
     


d_0 = {"backgroundcolor": "white", "color": "black", "family": "Times New Roman", "size": 10,
     "style": "italic", "weight": "bold"}


from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], linestyle='-', color='red', label='PWIA'),
    Line2D([0], [0], linestyle='-', color='blue', label='FSI'),
    Line2D([0], [0], linestyle='-', color='green', label='CHEX')
]
plt.legend(handles=legend_elements, loc='upper right')


plt.xlabel('Recoil Nucleon Polar Angle (degrees)')
plt.ylabel('Cross-Section')
plt.title('Ratio of Neutron-Proton Cross Section ($Q^2$ = 4.0 GeV)')

plt.text(180, 0.4323, "100 MeV/c", fontdict=d_0)
plt.text(180, 0.4316, "50 MeV/c", fontdict=d_0)
plt.text(180, 0.4315, "1 MeV/c", fontdict=d_0)

plt.grid(True)

plt.savefig('RNPCS.png', dpi = 300)

plt.show()