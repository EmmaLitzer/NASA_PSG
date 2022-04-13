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

PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CH4/"

# Full_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_1_CH42_0_R15000_4.5_5um_PSG.txt'
# Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
# Wavelength = Full['Wavelength']

# CH41_95_CH42_05_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_95_CH42_05_R15000_4.5_5um_PSG.txt'
# CH41_95_CH42_05 = np.genfromtxt(CH41_95_CH42_05_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_90_CH42_10_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_90_CH42_10_R15000_4.5_5um_PSG.txt'
# CH41_90_CH42_10 = np.genfromtxt(CH41_90_CH42_10_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_85_CH42_15_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_85_CH42_15_R15000_4.5_5um_PSG.txt'
# CH41_85_CH42_15 = np.genfromtxt(CH41_85_CH42_15_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_80_CH42_20_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_80_CH42_20_R15000_4.5_5um_PSG.txt'
# CH41_80_CH42_20 = np.genfromtxt(CH41_80_CH42_20_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_75_CH42_25_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_75_CH42_25_R15000_4.5_5um_PSG.txt'
# CH41_75_CH42_25 = np.genfromtxt(CH41_75_CH42_25_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_70_CH42_30_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_70_CH42_30_R15000_4.5_5um_PSG.txt'
# CH41_70_CH42_30 = np.genfromtxt(CH41_70_CH42_30_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_65_CH42_35_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_65_CH42_35_R15000_4.5_5um_PSG.txt'
# CH41_65_CH42_35 = np.genfromtxt(CH41_65_CH42_35_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_60_CH42_40_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_60_CH42_40_R15000_4.5_5um_PSG.txt'
# CH41_60_CH42_40 = np.genfromtxt(CH41_60_CH42_40_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_55_CH42_45_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_55_CH42_45_R15000_4.5_5um_PSG.txt'
# CH41_55_CH42_45 = np.genfromtxt(CH41_55_CH42_45_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_50_CH42_50_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_50_CH42_50_R15000_4.5_5um_PSG.txt'
# CH41_50_CH42_50 = np.genfromtxt(CH41_50_CH42_50_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_45_CH42_55_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_45_CH42_55_R15000_4.5_5um_PSG.txt'
# CH41_45_CH42_55 = np.genfromtxt(CH41_45_CH42_55_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_40_CH42_60_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_40_CH42_60_R15000_4.5_5um_PSG.txt'
# CH41_40_CH42_60 = np.genfromtxt(CH41_40_CH42_60_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_35_CH42_65_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_35_CH42_65_R15000_4.5_5um_PSG.txt'
# CH41_35_CH42_65 = np.genfromtxt(CH41_35_CH42_65_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_30_CH42_70_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_30_CH42_70_R15000_4.5_5um_PSG.txt'
# CH41_30_CH42_70 = np.genfromtxt(CH41_30_CH42_70_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_25_CH42_75_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_25_CH42_75_R15000_4.5_5um_PSG.txt'
# CH41_25_CH42_75 = np.genfromtxt(CH41_25_CH42_75_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_20_CH42_80_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_20_CH42_80_R15000_4.5_5um_PSG.txt'
# CH41_20_CH42_80 = np.genfromtxt(CH41_20_CH42_80_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_15_CH42_85_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_15_CH42_85_R15000_4.5_5um_PSG.txt'
# CH41_15_CH42_85 = np.genfromtxt(CH41_15_CH42_85_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_10_CH42_90_File = PSG_Directory + '/Ratios/'  + 'Titan_atmosphere_ratios_CO123_CH41_10_CH42_90_R15000_4.5_5um_PSG.txt'
# CH41_10_CH42_90 = np.genfromtxt(CH41_10_CH42_90_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_05_CH42_95_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_05_CH42_95_R15000_4.5_5um_PSG.txt'
# CH41_05_CH42_95 = np.genfromtxt(CH41_05_CH42_95_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# CH41_0_CH42_1_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_0_CH42_1_R15000_4.5_5um_PSG.txt'
# CH41_0_CH42_1 = np.genfromtxt(CH41_0_CH42_1_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

# Transmitance_0_1_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_0_CH42_1_R15000_4_Trans.txt'
# Transmitance_0_1 = np.genfromtxt(Transmitance_0_1_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

# Transmitance_1_0_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_1_CH42_0_R15000_4_Trans.txt'
# Transmitance_1_0 = np.genfromtxt(Transmitance_1_0_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

#--------------------------------------------------------
Full_File_3 = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_1_CH42_0_R15000_2.75_3.5um_PSG.txt'
Full = np.genfromtxt(Full_File_3, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Wavelength = Full['Wavelength']


CH41_90_CH42_10_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_9_CH42_1_R15000_2.75_3.5um_PSG.txt'
CH41_90_CH42_10 = np.genfromtxt(CH41_90_CH42_10_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_80_CH42_20_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_8_CH42_2_R15000_2.75_3.5um_PSG.txt'
CH41_80_CH42_20 = np.genfromtxt(CH41_80_CH42_20_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_70_CH42_30_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_7_CH42_3_R15000_2.75_3.5um_PSG.txt'
CH41_70_CH42_30 = np.genfromtxt(CH41_70_CH42_30_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_60_CH42_40_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_6_CH42_4_R15000_2.75_3.5um_PSG.txt'
CH41_60_CH42_40 = np.genfromtxt(CH41_60_CH42_40_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_50_CH42_50_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_5_CH42_5_R15000_2.75_3.5um_PSG.txt'
CH41_50_CH42_50 = np.genfromtxt(CH41_50_CH42_50_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_40_CH42_60_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_4_CH42_6_R15000_2.75_3.5um_PSG.txt'
CH41_40_CH42_60 = np.genfromtxt(CH41_40_CH42_60_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_30_CH42_70_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_3_CH42_7_R15000_2.75_3.5um_PSG.txt'
CH41_30_CH42_70 = np.genfromtxt(CH41_30_CH42_70_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_20_CH42_80_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_2_CH42_8_R15000_2.75_3.5um_PSG.txt'
CH41_20_CH42_80 = np.genfromtxt(CH41_20_CH42_80_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_10_CH42_90_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_1_CH42_9_R15000_2.75_3.5um_PSG.txt'
CH41_10_CH42_90 = np.genfromtxt(CH41_10_CH42_90_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CH41_0_CH42_1_File = PSG_Directory + '/Ratios/' +  'Titan_atmosphere_ratios_CO123_CH41_0_CH42_1_R15000_2.75_3.5um_PSG.txt'
CH41_0_CH42_1 = np.genfromtxt(CH41_0_CH42_1_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])


Transmitance_1_0_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_1_CH42_0_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_1_0 = np.genfromtxt(Transmitance_1_0_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_90_10_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_9_CH42_1_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_90_10 = np.genfromtxt(Transmitance_90_10_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_80_20_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_8_CH42_2_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_80_20 = np.genfromtxt(Transmitance_80_20_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_70_30_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_7_CH42_3_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_70_30 = np.genfromtxt(Transmitance_70_30_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_60_40_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_6_CH42_4_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_60_40 = np.genfromtxt(Transmitance_60_40_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_50_50_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_5_CH42_5_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_50_50 = np.genfromtxt(Transmitance_50_50_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_40_60_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_4_CH42_6_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_40_60 = np.genfromtxt(Transmitance_40_60_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_30_70_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_3_CH42_7_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_30_70 = np.genfromtxt(Transmitance_30_70_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_20_80_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_2_CH42_8_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_20_80 = np.genfromtxt(Transmitance_20_80_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_10_90_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_1_CH42_9_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_10_90 = np.genfromtxt(Transmitance_10_90_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])

Transmitance_0_1_File = PSG_Directory + '/Ratios/' + 'Titan_atmosphere_ratios_CO123_CH41_0_CH42_1_R15000_2.75_3.5um_PSG_trans.txt'
Transmitance_0_1 = np.genfromtxt(Transmitance_0_1_File, comments="#", dtype=np.float64, names=['Wavelength', 'Transmittance'])




N = 23
colors = plt.cm.jet(np.linspace(0,1,N))
# colors = plt.get_cmap('jet', N)

fig =plt.figure(dpi=300) 
# fig.set_size_inches(10, 4)
ax = plt.gca() 
# ax.set_aspect(25) 

a=.5
plt.plot(Wavelength, Full['Spectral_Radiance'], label='CH41_1_CH42_0', color=colors[0], alpha=a)
# plt.plot(Wavelength, CH41_95_CH42_05['Spectral_Radiance'], label='CH41_95_CH42_05', color=colors[20], alpha=a)
plt.plot(Wavelength, CH41_90_CH42_10['Spectral_Radiance'], label='CH41_90_CH42_10', color=colors[2], alpha=a)
# plt.plot(Wavelength, CH41_85_CH42_15['Spectral_Radiance'], label='CH41_85_CH42_15', color=colors[18], alpha=a)
plt.plot(Wavelength, CH41_80_CH42_20['Spectral_Radiance'], label='CH41_80_CH42_20', color=colors[4], alpha=a)
# plt.plot(Wavelength, CH41_75_CH42_25['Spectral_Radiance'], label='CH41_75_CH42_25', color=colors[16], alpha=a)
plt.plot(Wavelength, CH41_70_CH42_30['Spectral_Radiance'], label='CH41_70_CH42_30', color=colors[6], alpha=a)
# plt.plot(Wavelength, CH41_65_CH42_35['Spectral_Radiance'], label='CH41_65_CH42_35', color=colors[14], alpha=a)
plt.plot(Wavelength, CH41_60_CH42_40['Spectral_Radiance'], label='CH41_60_CH42_40', color=colors[8], alpha=a)
# plt.plot(Wavelength, CH41_55_CH42_45['Spectral_Radiance'], label='CH41_55_CH42_45', color=colors[12], alpha=a)
plt.plot(Wavelength, CH41_50_CH42_50['Spectral_Radiance'], label='CH41_50_CH42_50', color=colors[10], alpha=a)
# plt.plot(Wavelength, CH41_45_CH42_55['Spectral_Radiance'], label='CH41_45_CH42_55', color=colors[10], alpha=a)
plt.plot(Wavelength, CH41_40_CH42_60['Spectral_Radiance'], label='CH41_40_CH42_60', color=colors[12], alpha=a)
# plt.plot(Wavelength, CH41_35_CH42_65['Spectral_Radiance'], label='CH41_35_CH42_65', color=colors[8], alpha=a)
plt.plot(Wavelength, CH41_30_CH42_70['Spectral_Radiance'], label='CH41_30_CH42_70', color=colors[14], alpha=a)
# plt.plot(Wavelength, CH41_25_CH42_75['Spectral_Radiance'], label='CH41_25_CH42_75', color=colors[6], alpha=a)
plt.plot(Wavelength, CH41_20_CH42_80['Spectral_Radiance'], label='CH41_20_CH42_80', color=colors[16], alpha=a)
# plt.plot(Wavelength, CH41_15_CH42_85['Spectral_Radiance'], label='CH41_15_CH42_85', color=colors[4], alpha=a)
plt.plot(Wavelength, CH41_10_CH42_90['Spectral_Radiance'], label='CH41_10_CH42_90', color=colors[18], alpha=a)
# plt.plot(Wavelength, CH41_05_CH42_95['Spectral_Radiance'], label='CH41_05_CH42_95', color=colors[2], alpha=a)
plt.plot(Wavelength, CH41_0_CH42_1['Spectral_Radiance'], label='CH41_0_CH42_1', color=colors[20], alpha=a)






# plt.plot(Wavelength, Transmitance_1_0['Transmittance'], label='Transmittance [6:1]', color=colors[1], alpha=a)
# plt.plot(Wavelength, Transmitance_90_10['Transmittance'], label='', color=colors[3], alpha=a)
# plt.plot(Wavelength, Transmitance_80_20['Transmittance'], label='', color=colors[5], alpha=a)
# plt.plot(Wavelength, Transmitance_70_30['Transmittance'], label='', color=colors[7], alpha=a)
# plt.plot(Wavelength, Transmitance_60_40['Transmittance'], label='', color=colors[9], alpha=a)
# plt.plot(Wavelength, Transmitance_50_50['Transmittance'], label='', color=colors[11], alpha=a)
# plt.plot(Wavelength, Transmitance_40_60['Transmittance'], label='', color=colors[13], alpha=a)
# plt.plot(Wavelength, Transmitance_30_70['Transmittance'], label='', color=colors[15], alpha=a)
# plt.plot(Wavelength, Transmitance_20_80['Transmittance'], label='', color=colors[17], alpha=a)
# plt.plot(Wavelength, Transmitance_10_90['Transmittance'], label='', color=colors[19], alpha=a)
# plt.plot(Wavelength, Transmitance_0_1['Transmittance'], label='Transmittance [6:2]', color=colors[21], alpha=a)


# plt.xlim(2.75,3.5)
plt.xlim(2.95,3.35)
plt.ylim(0,.0045)
# plt.legend(loc=1)
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Titan atmosphere spectral radiance dependance\n on ratios of ' + r'$^{12}CH_4$ and $^{13}CH_4$' +' isotopes')
# plt.title('Titan atmosphere transmission dependance\n on ratios of ' + r'$^{12}CH_4$ and $^{13}CH_4$' +' isotopes')


# plt.ylabel("Transmittance")
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')

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
             boundaries=np.arange(-0.05,1), label=r'$^{13}CH_4/^{12}CH_4$')

# fig.tight_layout(rect=[.1,0,.9,1]) 
plt.tight_layout()


# fig.savefig("Figures/Titan_CH4_12_Ratios_Trans.png", dpi=300)
fig.savefig("Figures/Titan_CH4_12_Ratios.png", dpi=300)

plt.show()