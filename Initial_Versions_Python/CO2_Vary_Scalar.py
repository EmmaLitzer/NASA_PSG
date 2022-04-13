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

plt.close()

PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CO2/"


# Titan_atmosphere_ratios_CO123_CO2_1_R15000_3.75_4.5um_PSG.txt


Full_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_10_R15000_3.75_4.5um_PSG.txt'
Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Wavelength = Full['Wavelength']

CO2_9_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_9_R15000_3.75_4.5um_PSG.txt'
CO2_9 = np.genfromtxt(CO2_9_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_8_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_8_R15000_3.75_4.5um_PSG.txt'
CO2_8 = np.genfromtxt(CO2_8_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_7_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_7_R15000_3.75_4.5um_PSG.txt'
CO2_7 = np.genfromtxt(CO2_7_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_6_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_6_R15000_3.75_4.5um_PSG.txt'
CO2_6 = np.genfromtxt(CO2_6_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_5_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_5_R15000_3.75_4.5um_PSG.txt'
CO2_5 = np.genfromtxt(CO2_5_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_4_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_4_R15000_3.75_4.5um_PSG.txt'
CO2_4 = np.genfromtxt(CO2_4_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_3_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_3_R15000_3.75_4.5um_PSG.txt'
CO2_3 = np.genfromtxt(CO2_3_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_2_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_2_R15000_3.75_4.5um_PSG.txt'
CO2_2 = np.genfromtxt(CO2_2_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_1_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_1_R15000_3.75_4.5um_PSG.txt'
CO2_1 = np.genfromtxt(CO2_1_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO2_0_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_0_R15000_3.75_4.5um_PSG.txt'
CO2_0 = np.genfromtxt(CO2_0_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])


Transmitance_1_File = PSG_Directory +  'Titan_atmosphere_ratios_CO123_CO2_10_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_1 = np.genfromtxt(Transmitance_1_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_90_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_9_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_90 = np.genfromtxt(Transmitance_90_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_80_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_8_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_80 = np.genfromtxt(Transmitance_80_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_70_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_7_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_70 = np.genfromtxt(Transmitance_70_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_60_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_6_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_60 = np.genfromtxt(Transmitance_60_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_50_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_5_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_50 = np.genfromtxt(Transmitance_50_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_40_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_4_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_40 = np.genfromtxt(Transmitance_40_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_30_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_3_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_30 = np.genfromtxt(Transmitance_30_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_20_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_2_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_20 = np.genfromtxt(Transmitance_20_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_10_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_1_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_10 = np.genfromtxt(Transmitance_10_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_0_File = PSG_Directory + 'Titan_atmosphere_ratios_CO123_CO2_0_R15000_3.75_4.5um_PSG_trans.txt'
Transmitance_0 = np.genfromtxt(Transmitance_0_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])




N = 23
colors = plt.cm.jet(np.linspace(0,1,N))
# colors = plt.get_cmap('jet', N)

fig =plt.figure(dpi=300) 
# fig.set_size_inches(10, 4)
ax = plt.gca() 
# ax.set_aspect(25) 

a=.5
# plt.plot(Wavelength, Full['Spectral_Radiance'], label='CO2_100', color=colors[0], alpha=a)
# plt.plot(Wavelength, CO2_9['Spectral_Radiance'], label='CO2_90', color=colors[2], alpha=a)
# plt.plot(Wavelength, CO2_8['Spectral_Radiance'], label='CO2_90', color=colors[4], alpha=a)
# plt.plot(Wavelength, CO2_7['Spectral_Radiance'], label='CO2_70', color=colors[6], alpha=a)
# plt.plot(Wavelength, CO2_6['Spectral_Radiance'], label='CO2_60', color=colors[8], alpha=a)
# plt.plot(Wavelength, CO2_5['Spectral_Radiance'], label='CO2_50', color=colors[10], alpha=a)
# plt.plot(Wavelength, CO2_4['Spectral_Radiance'], label='CO2_40', color=colors[12], alpha=a)
# plt.plot(Wavelength, CO2_3['Spectral_Radiance'], label='CO2_30', color=colors[14], alpha=a)
# plt.plot(Wavelength, CO2_2['Spectral_Radiance'], label='CO2_20', color=colors[16], alpha=a)
# plt.plot(Wavelength, CO2_1['Spectral_Radiance'], label='CO2_10', color=colors[18], alpha=a)
# plt.plot(Wavelength, CO2_0['Spectral_Radiance'], label='CO2_0', color=colors[20], alpha=a)






plt.plot(Wavelength, Transmitance_1['Transmittance'], label='Transmittance [6:1]', color=colors[1], alpha=a)
plt.plot(Wavelength, Transmitance_90['Transmittance'], label='', color=colors[3], alpha=a)
plt.plot(Wavelength, Transmitance_80['Transmittance'], label='', color=colors[5], alpha=a)
plt.plot(Wavelength, Transmitance_70['Transmittance'], label='', color=colors[7], alpha=a)
plt.plot(Wavelength, Transmitance_60['Transmittance'], label='', color=colors[9], alpha=a)
plt.plot(Wavelength, Transmitance_50['Transmittance'], label='', color=colors[11], alpha=a)
plt.plot(Wavelength, Transmitance_40['Transmittance'], label='', color=colors[13], alpha=a)
plt.plot(Wavelength, Transmitance_30['Transmittance'], label='', color=colors[15], alpha=a)
plt.plot(Wavelength, Transmitance_20['Transmittance'], label='', color=colors[17], alpha=a)
plt.plot(Wavelength, Transmitance_10['Transmittance'], label='', color=colors[19], alpha=a)
plt.plot(Wavelength, Transmitance_0['Transmittance'], label='Transmittance [6:2]', color=colors[21], alpha=a)


plt.xlim(4.2,4.35)
# plt.ylim(.00008, .00014)
plt.ylim(0, .000000000001)

# plt.title('Titan atmosphere spectral radiance dependance\n on amount of ' + r'$CO_2$' )
plt.title('Titan atmosphere transmission dependance\n on amount of ' + r'$CO_2$')


plt.ylabel("Transmittance")
# plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')


# plt.legend()

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='jet', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
plt.colorbar(sm, ticks=np.linspace(0,1,10), cax=cax,
             boundaries=np.arange(-0.05,1), label=r'% $CO_2$')

# fig.tight_layout(rect=[.1,0,.9,1]) 
plt.tight_layout()


fig.savefig("Figures/Titan_CO2_Trans.png", dpi=300)
# fig.savefig("Figures/Titan_CO2.png", dpi=300)

plt.show()