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


def Load_Spec(file):
    Data_File = PSG_Directory + '/Ratios_small/' + file + '.txt'
    Data_array = np.genfromtxt(Data_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

    return Data_array


PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CO2/"
Full_File = PSG_Directory + '/Ratios_small/' + 'CO2_100.txt'

Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Wavelength = Full['Wavelength']


C02_110 = Load_Spec('CO2_110')
C02_109 = Load_Spec('CO2_109')
C02_108 = Load_Spec('CO2_108')
C02_107 = Load_Spec('CO2_107')
C02_106 = Load_Spec('CO2_106')
C02_105 = Load_Spec('CO2_105')
C02_104 = Load_Spec('CO2_104')
C02_103 = Load_Spec('CO2_103')
C02_102 = Load_Spec('CO2_102')
C02_101 = Load_Spec('CO2_101')

#Full

C02_099 = Load_Spec('CO2_099')
C02_098 = Load_Spec('CO2_098')
C02_097 = Load_Spec('CO2_097')
C02_096 = Load_Spec('CO2_096')
C02_095 = Load_Spec('CO2_095')
C02_094 = Load_Spec('CO2_094')
C02_093 = Load_Spec('CO2_093')
C02_092 = Load_Spec('CO2_092')
C02_091 = Load_Spec('CO2_091')
C02_090 = Load_Spec('CO2_090')




CO2_array = [C02_110,
            C02_109,
            C02_108,
            C02_107,
            C02_106,
            C02_105,
            C02_104,
            C02_103,
            C02_102,
            C02_101,
            Full,
            C02_099,
            C02_098,
            C02_097,
            C02_096,
            C02_095,
            C02_094,
            C02_093,
            C02_092,
            C02_091,
            C02_090]




N = 22
colors = plt.cm.viridis(np.linspace(0,1,N))
# colors = plt.get_cmap('jet', N)

fig =plt.figure(dpi=300) 
plt.plot(Wavelength, Full['Spectral_Radiance'], label='CO2_100', color=colors[0])

for i, Isotope in enumerate(CO2_array):
    plt.plot(Wavelength, Isotope['Spectral_Radiance'], label='{Isotope}', color=colors[i+1])


plt.xlim(4.2,4.35)
plt.ylim(.00009,.00014)
ax = plt.gca() 

# plt.legend()
plt.title('Titan atmosphere spectral radiance dependance\n on scalar values of ' + r'$CO_2$')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
cbar = plt.colorbar(sm, ticks=np.linspace(.9,1.1,20), cax=cax,
             boundaries=np.arange(-.85,1.15), label=r'$CO_2$')



plt.tight_layout()
fig.savefig("Figures/Titan_CO2_small_ratio.png", dpi=300)


plt.show()