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

PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CH4/"

Full_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_1_CH42_0_R15000_4.5_5um_PSG.txt'
Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Wavelength = Full['Wavelength']

CH41_95_CH42_05_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_95_CH42_05_R15000_4.5_5um_PSG.txt'
CH41_95_CH42_05 = np.genfromtxt(CH41_95_CH42_05_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_90_CH42_10_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_90_CH42_10_R15000_4.5_5um_PSG.txt'
CH41_90_CH42_10 = np.genfromtxt(CH41_90_CH42_10_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_85_CH42_15_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_85_CH42_15_R15000_4.5_5um_PSG.txt'
CH41_85_CH42_15 = np.genfromtxt(CH41_85_CH42_15_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_80_CH42_20_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_80_CH42_20_R15000_4.5_5um_PSG.txt'
CH41_80_CH42_20 = np.genfromtxt(CH41_80_CH42_20_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_75_CH42_25_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_75_CH42_25_R15000_4.5_5um_PSG.txt'
CH41_75_CH42_25 = np.genfromtxt(CH41_75_CH42_25_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_70_CH42_30_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_70_CH42_30_R15000_4.5_5um_PSG.txt'
CH41_70_CH42_30 = np.genfromtxt(CH41_70_CH42_30_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_65_CH42_35_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_65_CH42_35_R15000_4.5_5um_PSG.txt'
CH41_65_CH42_35 = np.genfromtxt(CH41_65_CH42_35_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_60_CH42_40_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_60_CH42_40_R15000_4.5_5um_PSG.txt'
CH41_60_CH42_40 = np.genfromtxt(CH41_60_CH42_40_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_55_CH42_45_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_55_CH42_45_R15000_4.5_5um_PSG.txt'
CH41_55_CH42_45 = np.genfromtxt(CH41_55_CH42_45_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_50_CH42_50_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_50_CH42_50_R15000_4.5_5um_PSG.txt'
CH41_50_CH42_50 = np.genfromtxt(CH41_50_CH42_50_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_45_CH42_55_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_45_CH42_55_R15000_4.5_5um_PSG.txt'
CH41_45_CH42_55 = np.genfromtxt(CH41_45_CH42_55_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_40_CH42_60_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_40_CH42_60_R15000_4.5_5um_PSG.txt'
CH41_40_CH42_60 = np.genfromtxt(CH41_40_CH42_60_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_35_CH42_65_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_35_CH42_65_R15000_4.5_5um_PSG.txt'
CH41_35_CH42_65 = np.genfromtxt(CH41_35_CH42_65_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_30_CH42_70_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_30_CH42_70_R15000_4.5_5um_PSG.txt'
CH41_30_CH42_70 = np.genfromtxt(CH41_30_CH42_70_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_25_CH42_75_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_25_CH42_75_R15000_4.5_5um_PSG.txt'
CH41_25_CH42_75 = np.genfromtxt(CH41_25_CH42_75_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_20_CH42_80_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_20_CH42_80_R15000_4.5_5um_PSG.txt'
CH41_20_CH42_80 = np.genfromtxt(CH41_20_CH42_80_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_15_CH42_85_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_15_CH42_85_R15000_4.5_5um_PSG.txt'
CH41_15_CH42_85 = np.genfromtxt(CH41_15_CH42_85_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_10_CH42_90_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_10_CH42_90_R15000_4.5_5um_PSG.txt'
CH41_10_CH42_90 = np.genfromtxt(CH41_10_CH42_90_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_05_CH42_95_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_05_CH42_95_R15000_4.5_5um_PSG.txt'
CH41_05_CH42_95 = np.genfromtxt(CH41_05_CH42_95_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_0_CH42_1_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_0_CH42_1_R15000_4.5_5um_PSG.txt'
CH41_0_CH42_1 = np.genfromtxt(CH41_0_CH42_1_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])


N = 21
colors = plt.cm.jet(np.linspace(0,1,N))
# colors = plt.get_cmap('jet', N)

fig =plt.figure(dpi=300) 
# fig.set_size_inches(10, 4)
ax = plt.gca() 
# ax.set_aspect(25) 

a=.1

plt.plot(Wavelength, CH41_95_CH42_05['Spectral_Radiance'], label='CH41_95_CH42_05', color=colors[20], alpha=a)
plt.plot(Wavelength, CH41_90_CH42_10['Spectral_Radiance'], label='CH41_90_CH42_10', color=colors[19], alpha=a)
plt.plot(Wavelength, CH41_85_CH42_15['Spectral_Radiance'], label='CH41_85_CH42_15', color=colors[18], alpha=a)
plt.plot(Wavelength, CH41_80_CH42_20['Spectral_Radiance'], label='CH41_80_CH42_20', color=colors[17], alpha=a)
plt.plot(Wavelength, CH41_75_CH42_25['Spectral_Radiance'], label='CH41_75_CH42_25', color=colors[16], alpha=a)
plt.plot(Wavelength, CH41_70_CH42_30['Spectral_Radiance'], label='CH41_70_CH42_30', color=colors[15], alpha=a)
plt.plot(Wavelength, CH41_65_CH42_35['Spectral_Radiance'], label='CH41_65_CH42_35', color=colors[14], alpha=a)
plt.plot(Wavelength, CH41_60_CH42_40['Spectral_Radiance'], label='CH41_60_CH42_40', color=colors[13], alpha=a)
plt.plot(Wavelength, CH41_55_CH42_45['Spectral_Radiance'], label='CH41_55_CH42_45', color=colors[12], alpha=a)
plt.plot(Wavelength, CH41_50_CH42_50['Spectral_Radiance'], label='CH41_50_CH42_50', color=colors[11], alpha=a)
plt.plot(Wavelength, CH41_45_CH42_55['Spectral_Radiance'], label='CH41_45_CH42_55', color=colors[10], alpha=a)
plt.plot(Wavelength, CH41_40_CH42_60['Spectral_Radiance'], label='CH41_40_CH42_60', color=colors[9], alpha=a)
plt.plot(Wavelength, CH41_35_CH42_65['Spectral_Radiance'], label='CH41_35_CH42_65', color=colors[8], alpha=a)
plt.plot(Wavelength, CH41_30_CH42_70['Spectral_Radiance'], label='CH41_30_CH42_70', color=colors[7], alpha=a)
plt.plot(Wavelength, CH41_25_CH42_75['Spectral_Radiance'], label='CH41_25_CH42_75', color=colors[6], alpha=a)
plt.plot(Wavelength, CH41_20_CH42_80['Spectral_Radiance'], label='CH41_20_CH42_80', color=colors[5], alpha=a)
plt.plot(Wavelength, CH41_15_CH42_85['Spectral_Radiance'], label='CH41_15_CH42_85', color=colors[4], alpha=a)
plt.plot(Wavelength, CH41_10_CH42_90['Spectral_Radiance'], label='CH41_10_CH42_90', color=colors[3], alpha=a)
plt.plot(Wavelength, CH41_05_CH42_95['Spectral_Radiance'], label='CH41_05_CH42_95', color=colors[2], alpha=a)
plt.plot(Wavelength, CH41_0_CH42_1['Spectral_Radiance'], label='CH41_0_CH42_1', color=colors[1], alpha=a)

plt.plot(Wavelength, Full['Spectral_Radiance'], label='CH41_1_CH42_0', color=colors[0], alpha=a)

plt.xlim(4.8,4.9)
# plt.legend()
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title("Ratios of CH4 [6:1] and [6:2] isotopes in Titan's atmosphere")
plt.ylabel("Spectral Radiance")
plt.xlabel("Wavelength")

# divider = make_axes_locatable(ax)
# colorbar_axes = divider.append_axes("right",
#                                     size="10%",
#                                     pad=0.1)
# plt.colorbar(ax, cmap=colors, ticks=np.linspace(0,2,N), 
#              boundaries=np.arange(-0.05,2.1,.1))

# plt.legend()

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='jet', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
plt.colorbar(sm, ticks=np.linspace(0,1,10), cax=cax,
             boundaries=np.arange(-0.05,1), label='%CH4 [6:2]')

# fig.tight_layout(rect=[.1,0,.9,1]) 
plt.tight_layout()


fig.savefig("Figures/Titan_CH4_12_Ratios.png", dpi=300)

plt.show()