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



PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/"
Surface_Directory = PSG_Directory + 'Surface_Composition/Surface_with_standard_atmosphere_CH4_N2/CH4_C2H6/'
Full_File = Surface_Directory + 'CH4_Liquid_GSFC' + '.txt'

Titles = ['CH4_C2H6_Surface_10%Components_R500_standard_atmosphere2', 'CH4_C2H6_Surface_10%Components_R500_difference_standard_atmosphere2']

files = sorted(glob.glob(Surface_Directory + '*.txt'))

Ratio = []
Data_array = []

min_max= [.85, 1.15, .05]

def Load_Spec(file):
    # Data_File = file + '.txt'
    # print(file[-18:-4])
    Data_array = np.genfromtxt(file, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
    # Data_array = np.asarray(Data_array)
    return Data_array


for i, filename in enumerate(files):
    Ratio.append(filename[len(Surface_Directory):-4])
    data = Load_Spec(filename)
    # print(data["Spectral_Radiance"])
    Data_array.append(data)

Data_array = np.array(Data_array)
print(Ratio)



Titan_Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

fig = plt.figure(dpi=300)
N = len(Data_array) + 1
colors = plt.cm.tab10(np.linspace(0,1,N))

for i, Isotope in enumerate(Data_array):
    r = Ratio[i]
    plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'], label=('10% '+ r), color=colors[i+1], linewidth=1, alpha=.75)

# plt.xlim(2.5,2.9)
plt.title('Titan PSG Simulation for \nTitan_USGS + 10% CH4_C2H6 Surface Components at R500')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
plt.legend()


ax = plt.gca() 

# norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
# sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
# sm.set_array([])
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.15)
# cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

plt.tight_layout()
fig.savefig("Figures/" + Titles[1] + ".png", dpi=300)






fig = plt.figure(dpi=300)
# N = len(Data_array) + 1
# colors = plt.cm.jet(np.linspace(0,1,N))

for i, Isotope in enumerate(Data_array):
    r = Ratio[i]
    plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'] - Titan_Full['Spectral_Radiance'], label=('10% '+ r), color=colors[i+1], linewidth=1, alpha=.75)


# plt.xlim(2.5,2.9)
plt.title('Titan PSG Simulation Differences for \nTitan_USGS + 10% CH4_C2H6 Surface Components at R500')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
plt.legend()


# ax = plt.gca() 

# norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
# sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
# sm.set_array([])
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.15)
# cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

plt.tight_layout()
fig.savefig("Figures/" + Titles[2] + ".png", dpi=300)


plt.show()


# Data_array = np.array(Data_array)


# H2O_pddf = pd.DataFrame(data= Data_array['Spectral_Radiance'].T,
#                         columns = [i for i in Ratio],
#                         index = H2O_Full["Wavelength"])

# with pd.ExcelWriter('H2O.xlsx') as writer:
#     H2O_pddf.to_excel(writer, sheet_name='H2O')

