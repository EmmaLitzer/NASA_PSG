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

# Titan_atmosphere_ratios_CO1_0.987_2_0.011_3_0.002_R15000_4.5_5um_PSG.txt

def Load_Spec(file):
    Data_File = PSG_Directory + '/Ratios_small/' + file + '.txt'
    Data_array = np.genfromtxt(Data_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

    return Data_array


PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CO/"
Full_File = PSG_Directory + '/Ratios_small/' + 'CO1_987_CO2_011_CO3_002.txt'

Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Wavelength = Full['Wavelength']



CO1_101 = Load_Spec('CO1_101')
CO1_102 = Load_Spec('CO1_102')
CO1_103 = Load_Spec('CO1_103')
CO1_104 = Load_Spec('CO1_104')
CO1_105 = Load_Spec('CO1_105')
CO1_106 = Load_Spec('CO1_106')
CO1_107 = Load_Spec('CO1_107')
CO1_108 = Load_Spec('CO1_108')
CO1_109 = Load_Spec('CO1_109')
CO1_110 = Load_Spec('CO1_110')

CO1_100_CO2_000 = Load_Spec('CO1_100_CO2_000')
CO1_099_CO2_001 = Load_Spec('CO1_099_CO2_001')
CO1_098_CO2_002 = Load_Spec('CO1_098_CO2_002')
CO1_097_CO2_003 = Load_Spec('CO1_097_CO2_003')
CO1_096_CO2_004 = Load_Spec('CO1_096_CO2_004')
CO1_095_CO2_005 = Load_Spec('CO1_095_CO2_005')
CO1_094_CO2_006 = Load_Spec('CO1_094_CO2_006')
CO1_093_CO2_007 = Load_Spec('CO1_093_CO2_007')
CO1_092_CO2_008 = Load_Spec('CO1_092_CO2_008')
CO1_091_CO2_009 = Load_Spec('CO1_091_CO2_009')
CO1_090_CO2_010 = Load_Spec('CO1_090_CO2_010')

CO1_100_CO3_000 = Load_Spec('CO1_100_CO3_000')
CO1_099_CO3_001 = Load_Spec('CO1_099_CO3_001')
CO1_098_CO3_002 = Load_Spec('CO1_098_CO3_002')
CO1_097_CO3_003 = Load_Spec('CO1_097_CO3_003')
CO1_096_CO3_004 = Load_Spec('CO1_096_CO3_004')
CO1_095_CO3_005 = Load_Spec('CO1_095_CO3_005')
CO1_094_CO3_006 = Load_Spec('CO1_094_CO3_006')
CO1_093_CO3_007 = Load_Spec('CO1_093_CO3_007')
CO1_092_CO3_008 = Load_Spec('CO1_092_CO3_008')
CO1_091_CO3_009 = Load_Spec('CO1_091_CO3_009')
CO1_090_CO3_010 = Load_Spec('CO1_090_CO3_010')


CO1_array = [CO1_100_CO2_000,
            CO1_101,
            CO1_102,
            CO1_103,
            CO1_104,
            CO1_105,
            CO1_106,
            CO1_107,
            CO1_108,
            CO1_109,
            CO1_110]

CO1_CO2_array = [CO1_100_CO2_000,
                CO1_099_CO2_001,
                CO1_098_CO2_002,
                CO1_097_CO2_003,
                CO1_096_CO2_004,
                CO1_095_CO2_005,
                CO1_094_CO2_006,
                CO1_093_CO2_007,
                CO1_092_CO2_008,
                CO1_091_CO2_009,
                CO1_090_CO2_010]

CO1_CO3_array = [CO1_100_CO3_000,
                CO1_099_CO3_001,
                CO1_098_CO3_002,
                CO1_097_CO3_003,
                CO1_096_CO3_004,
                CO1_095_CO3_005,
                CO1_094_CO3_006,
                CO1_093_CO3_007,
                CO1_092_CO3_008,
                CO1_091_CO3_009,
                CO1_090_CO3_010]


N = 12
colors = plt.cm.viridis(np.linspace(0,1,N))
# colors = plt.get_cmap('jet', N)

fig =plt.figure(dpi=300) 
plt.plot(Wavelength, Full['Spectral_Radiance'], label='1_987_2_001_3_002', color=colors[0])

for i, Isotope in enumerate(CO1_CO2_array):
    plt.plot(Wavelength, Isotope['Spectral_Radiance'], label='{Isotope}', color=colors[i+1])


plt.xlim(4.8,4.9)
ax = plt.gca() 

# plt.legend()
plt.title('Titan atmosphere spectral radiance dependance\n on ratios of ' + r'$^{12}C^{16}O$ and $^{13}C^{16}O$' +' isotopes')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
plt.colorbar(sm, ticks=np.linspace(0,1,10), cax=cax,
             boundaries=np.arange(-0.05,1), label=r'$^{13}C^{16}O/^{12}C^{16}O$')

plt.tight_layout()
fig.savefig("Figures/Titan_CO123_small_Ratios.png", dpi=300)

# -----------------------------------------------------------------------------------------------------------

fig =plt.figure(dpi=300) 
plt.plot(Wavelength, Full['Spectral_Radiance'], label='1_987_2_001_3_002', color=colors[0])

for i, Ratio in enumerate(CO1_array):
    plt.plot(Wavelength, Ratio['Spectral_Radiance'], label='{Ratio}', color=colors[i+1])


plt.xlim(4.8,4.9)
ax = plt.gca() 

# plt.legend()
plt.title('Titan atmosphere spectral radiance dependance\n on scalar value of ' + r'$^{12}C^{16}O$ ' +' isotope')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
plt.colorbar(sm, ticks=np.linspace(0,1,10), cax=cax,
             boundaries=np.arange(-0.05,1), label=r'$^{12}C^{16}O$')

plt.tight_layout()
fig.savefig("Figures/Titan_CO1_small_Ratios.png", dpi=300)

# -----------------------------------------------------------------------------------------------------------

fig =plt.figure(dpi=300) 
plt.plot(Wavelength, Full['Spectral_Radiance'], label='1_987_2_001_3_002', color=colors[0])

for i, Isotope in enumerate(CO1_CO3_array):
    plt.plot(Wavelength, Isotope['Spectral_Radiance'], label='{Isotope}', color=colors[i+1])


plt.xlim(4.8,4.9)
ax = plt.gca() 

# plt.legend()
plt.title('Titan atmosphere spectral radiance dependance\n on ratios of ' + r'$^{12}C^{16}O$ and $^{16}C^{18}O$' +' isotopes')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
plt.colorbar(sm, ticks=np.linspace(0,1,10), cax=cax,
             boundaries=np.arange(-0.05,1), label=r'$^{12}C^{16}O/^{12}C^{18}O$')

plt.tight_layout()
fig.savefig("Figures/Titan_CO1_CO3_small_Ratios.png", dpi=300)
plt.show()




