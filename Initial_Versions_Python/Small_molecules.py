from ast import Load
import numpy as np
import scipy as sp
import astropy as ap
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import time
import os
import sys
import glob

## FILES:
'''
C2H2_0_ppbv_230_330.txt
C2H2_0_ppbv_350_470.txt
C2H2_1_ppbv_230_330.txt
C2H2_1_ppbv_350_470.txt

CH3OH_0_ppbv_265_365.txt
CH3OH_0_ppbv_450_500.txt
CH3OH_1_ppbv_265_365.txt
CH3OH_1_ppbv_450_500.txt

H2CO_0_ppbv.txt
H2CO_1_ppbv.txt
'''



PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/"
Small_Directory = PSG_Directory + 'Small_Molecules/'
Full_File1 = Small_Directory + 'H2CO_0_ppbv' + '.txt'
Isotope_file1 = Small_Directory + 'H2CO_1_ppbv' + '.txt'
# Full_File2 = Small_Directory + 'C2H2_0_ppbv_350_470' + '.txt'
# Isotope_file2 = Small_Directory + 'C2H2_1_ppbv_350_470' + '.txt'

Molecule_name = 'H2CO'
Wavelength_Range1 = ''
# Wavelength_Range2 = '350_470'

min_max= [0, 1.05, .1]


Full1 = np.genfromtxt(Full_File1, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Isotope1 = np.genfromtxt(Isotope_file1, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# Full2 = np.genfromtxt(Full_File2, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
# Isotope2 = np.genfromtxt(Isotope_file2, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])






fig = plt.figure(dpi=300)
N = 2 #len(Data_array) + 1
colors = plt.cm.viridis(np.linspace(0,1,N))

plt.plot(Isotope1['Wavelength'], Isotope1['Spectral_Radiance'], label='1ppbv ' + Molecule_name, color=colors[0], linewidth=1)
plt.plot(Full1['Wavelength'], Full1['Spectral_Radiance'], label='0ppbv ' +Molecule_name, color=colors[1], linewidth=1)


plt.title('Titan atmosphere spectral radiance dependance\n on values of ' + Molecule_name)
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
plt.legend()

plt.tight_layout()
fig.savefig("Figures/" + Molecule_name +'_' + Wavelength_Range1 + ".png", dpi=300)



fig = plt.figure(dpi=300)
plt.plot(Full1['Wavelength'], Isotope1['Spectral_Radiance'] - Full1['Spectral_Radiance'], label='Difference of 1ppbv '+Molecule_name, color=colors[0])
plt.title('Titan atmosphere spectral radiance dependance\n on values of ' + Molecule_name)
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
plt.legend()


plt.tight_layout()
fig.savefig("Figures/" + Molecule_name +'_Difference'+'_' + Wavelength_Range1 + ".png", dpi=300)





# fig = plt.figure(dpi=300)
# N = 2 #len(Data_array) + 1
# colors = plt.cm.viridis(np.linspace(0,1,N))

# plt.plot(Isotope2['Wavelength'], Isotope2['Spectral_Radiance'], label='1ppbv ' + Molecule_name, color=colors[0], linewidth=1)
# plt.plot(Full2['Wavelength'], Full2['Spectral_Radiance'], label='0ppbv ' +Molecule_name, color=colors[1], linewidth=1)


# plt.title('Titan atmosphere spectral radiance dependance\n on values of ' + Molecule_name)
# plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
# plt.xlabel("Wavelength" + ' (µm)')
# plt.legend()

# plt.tight_layout()
# fig.savefig("Figures/" + Molecule_name +'_' + Wavelength_Range2 + ".png", dpi=300)



# fig = plt.figure(dpi=300)
# plt.plot(Full2['Wavelength'], Isotope2['Spectral_Radiance'] - Full2['Spectral_Radiance'], label='Difference of 1ppbv '+Molecule_name, color=colors[0])
# plt.title('Titan atmosphere spectral radiance dependance\n on values of ' + Molecule_name)
# plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
# plt.xlabel("Wavelength" + ' (µm)')

# plt.legend()

# plt.tight_layout()

# fig.savefig("Figures/" + Molecule_name +'_Difference'+'_' + Wavelength_Range2 + ".png", dpi=300)


plt.show()