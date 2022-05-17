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

R = str(15000)
xls_name = 'Atmosphere_components_1ppb'


PSG_Directory = "/Users/elitzer/Desktop/PSG/NASA_PSG-main/Docker/"
Surface_Directory = PSG_Directory + 'Lakes/'
Full_File = PSG_Directory + 'Base_Titan_Atmosphere_SR' + '.txt'

Fig_Titles = ['Atmosphere_components_1ppb_noNitriles22', 'Atmosphere_components_1ppb_Difference_noNitriles22']
Pic_Titles = ['Titan PSG Simulation for Different Atmospheric \n components at R' + R,
              'Titan PSG Simulation Difference between Atmospheric \n Components and Standard Titan Atmosphere at R' + R]

# Fig_Titles = ['COiso_1ppb', 'COiso_1ppb_Difference']
# Pic_Titles = ['Titan PSG Simulation for Different Atmospheric \n components at R' + R,
#               'Titan PSG Simulation Difference between Atmospheric \n Components and Standard Titan Atmosphere at R' + R]

# Fig_Titles = ['Nobel_Gas_atm_1ppb_noXe', 'Nobel_Gas_atm_difference_1ppb_noXe']
# Pic_Titles = ['Titan PSG Simulation for Nobel Gasses \n in Atmosphere at R' + R,
#               'Titan PSG Simulation Difference between Nobel \n Gas and Standard Titan Atmosphere at R' + R]

files = sorted(glob.glob(Surface_Directory  + '*.txt'))

Ratio = []
Data_array = []

min_max= [.85, 1.15, .05]

def Load_Spec(file):
    # Data_File = file + '.txt'
    # print(file[-:-4])
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



fig = plt.figure(dpi=300) #, figsize=(10, 2))
N = len(Data_array) + 1
colors = plt.cm.jet(np.linspace(0,1,N))

for i, Isotope in enumerate(Data_array):
    r = Ratio[i]
    plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'], label=( r), color=colors[i+1], linewidth=.75, alpha=1)

# plt.xlim(2.5,2.9)
plt.title(Pic_Titles[0])
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
plt.yscale('log')
# plt.xlim(4.5,4.75)
# plt.ylim(0,5e-4)

plt.legend()


ax = plt.gca() 

# norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
# sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
# sm.set_array([])
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.15)
# cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

plt.tight_layout()
# fig.savefig("Figures/" + Fig_Titles[0] + ".png", dpi=300)






fig = plt.figure(dpi=300) #, figsize=(10, 2))
# N = len(Data_array) + 1
# colors = plt.cm.jet(np.linspace(0,1,N))

for i, Isotope in enumerate(Data_array):
    r = Ratio[i]
    plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'] - Titan_Full['Spectral_Radiance'], label=( r), color=colors[i+1], linewidth=.75, alpha=1)


# plt.xlim(2.5,2.9)
plt.title(Pic_Titles[1])
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
# plt.yscale('log')
# plt.xlim(4.5,4.75)
# plt.ylim(0,5e-4)
plt.legend()


# ax = plt.gca() 

# norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
# sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
# sm.set_array([])
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.15)
# cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

plt.tight_layout()
# fig.savefig("Figures/" + Fig_Titles[1] + ".png", dpi=300)


plt.show()


# Data_array = np.array(Data_array)


# pddf = pd.DataFrame(data= Data_array['Spectral_Radiance'].T,
#                         columns = [i for i in Ratio],
#                         index = Titan_Full["Wavelength"])

# with pd.ExcelWriter('Excel/' + xls_name + '.xlsx') as writer:
#     pddf.to_excel(writer, sheet_name=xls_name+'_R'+R)

