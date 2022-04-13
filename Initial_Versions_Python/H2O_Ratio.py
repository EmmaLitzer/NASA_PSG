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
H2O_Directory = PSG_Directory + 'H2O/'
Full_File = H2O_Directory + 'H2O_1_00_scalar' + '.txt'

files = sorted(glob.glob(H2O_Directory + '*.txt'))

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
    Ratio.append(filename[-18:-4])
    data = Load_Spec(filename)
    # print(data["Spectral_Radiance"])
    Data_array.append(data)

Data_array = np.array(Data_array)
# print(Data_array["Spectral_Radiance"])



H2O_Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

fig = plt.figure(dpi=300)
N = len(Data_array) + 1
colors = plt.cm.viridis(np.linspace(0,1,N))

for i, Isotope in enumerate(Data_array):
    r = Ratio[i]
    plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'], label=r, color=colors[i+1], linewidth=1)

plt.xlim(2.5,2.9)
plt.title('Titan atmosphere spectral radiance dependance\n on scalar values of ' + 'H2O')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
# plt.legend()


ax = plt.gca() 

norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

plt.tight_layout()
fig.savefig("Figures/" + "H20_ratios" + ".png", dpi=300)






fig = plt.figure(dpi=300)
N = len(Data_array) + 1
colors = plt.cm.viridis(np.linspace(0,1,N))

for i, Isotope in enumerate(Data_array):
    plt.plot(H2O_Full['Wavelength'], Isotope['Spectral_Radiance'] - H2O_Full['Spectral_Radiance'], label='{Ratio[i]}', color=colors[i+1])

plt.plot(H2O_Full['Wavelength'], Isotope['Spectral_Radiance'] - H2O_Full['Spectral_Radiance'], label='{Ratio[i]}', color=colors[i+1])


plt.xlim(2.5,2.9)
plt.title('Titan atmosphere spectral radiance dependance\n on scalar values of ' + 'H2O')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')


ax = plt.gca() 

norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

plt.tight_layout()
fig.savefig("Figures/" + "H20_difference_ratios" + ".png", dpi=300)


plt.show()


Data_array = np.array(Data_array)


H2O_pddf = pd.DataFrame(data= Data_array['Spectral_Radiance'].T,
                        columns = [i for i in Ratio],
                        index = H2O_Full["Wavelength"])

with pd.ExcelWriter('H2O.xlsx') as writer:
    H2O_pddf.to_excel(writer, sheet_name='H2O')

