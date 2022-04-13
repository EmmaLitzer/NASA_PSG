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

PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CO/"
Full_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.987_2_0.011_3_0.002_R15000_4.5_5um_PSG.txt'

Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Wavelength = Full['Wavelength']

CO1_437_2_561_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.437_2_0.561_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_437_2_561_3_002 = np.genfromtxt(CO1_437_2_561_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_487_2_511_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.487_2_0.511_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_487_2_511_3_002 = np.genfromtxt(CO1_487_2_511_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_537_2_461_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.537_2_0.461_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_537_2_461_3_002 = np.genfromtxt(CO1_537_2_461_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_587_2_411_3_002_File = PSG_Directory + '/Ratios/' +  'CO12/' +'Titan_atmosphere_ratios_CO1_0.587_2_0.411_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_587_2_411_3_002 = np.genfromtxt(CO1_587_2_411_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_637_2_361_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.637_2_0.361_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_637_2_361_3_002 = np.genfromtxt(CO1_637_2_361_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_687_2_311_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.687_2_0.311_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_687_2_311_3_002 = np.genfromtxt(CO1_687_2_311_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_737_2_261_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.737_2_0.261_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_737_2_261_3_002 = np.genfromtxt(CO1_737_2_261_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_787_2_211_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.787_2_0.211_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_787_2_211_3_002 = np.genfromtxt(CO1_787_2_211_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_837_2_161_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.837_2_0.161_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_837_2_161_3_002 = np.genfromtxt(CO1_837_2_161_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_887_2_111_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.887_2_0.161_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_887_2_111_3_002 = np.genfromtxt(CO1_887_2_111_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_937_2_061_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.937_2_0.061_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_937_2_061_3_002 = np.genfromtxt(CO1_937_2_061_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_387_2_611_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.387_2_0.611_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_387_2_611_3_002 = np.genfromtxt(CO1_387_2_611_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_337_2_661_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.337_2_0.661_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_337_2_661_3_002 = np.genfromtxt(CO1_337_2_661_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_287_2_711_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.287_2_0.711_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_287_2_711_3_002 = np.genfromtxt(CO1_287_2_711_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_237_2_761_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.237_2_0.761_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_237_2_761_3_002 = np.genfromtxt(CO1_237_2_761_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_187_2_811_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.187_2_0.811_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_187_2_811_3_002 = np.genfromtxt(CO1_187_2_811_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_137_2_861_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.137_2_0.861_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_137_2_861_3_002 = np.genfromtxt(CO1_137_2_861_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_087_2_911_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.087_2_0.911_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_087_2_911_3_002 = np.genfromtxt(CO1_087_2_911_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_037_2_961_3_002_File = PSG_Directory + '/Ratios/' + 'CO12/' + 'Titan_atmosphere_ratios_CO1_0.037_2_0.961_3_0.002_R15000_4.5_5um_PSG.txt'
CO1_037_2_961_3_002 = np.genfromtxt(CO1_037_2_961_3_002_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])


N = 20
colors = plt.cm.viridis(np.linspace(0,1,20))
# colors = plt.get_cmap('jet', N)

fig =plt.figure(dpi=300) 
# fig.set_size_inches(10, 4)
ax = plt.gca() 
# ax.set_aspect(25) 



plt.plot(Wavelength, CO1_037_2_961_3_002['Spectral_Radiance'], label='CO1_037_2_961_3_002', color=colors[19])
plt.plot(Wavelength, CO1_087_2_911_3_002['Spectral_Radiance'], label='CO1_087_2_911_3_002', color=colors[18])
plt.plot(Wavelength, CO1_137_2_861_3_002['Spectral_Radiance'], label='CO1_137_2_861_3_002', color=colors[17])
plt.plot(Wavelength, CO1_187_2_811_3_002['Spectral_Radiance'], label='CO1_187_2_811_3_002', color=colors[16])
plt.plot(Wavelength, CO1_237_2_761_3_002['Spectral_Radiance'], label='CO1_237_2_761_3_002', color=colors[15])
plt.plot(Wavelength, CO1_287_2_711_3_002['Spectral_Radiance'], label='CO1_287_2_711_3_002', color=colors[14])
plt.plot(Wavelength, CO1_337_2_661_3_002['Spectral_Radiance'], label='CO1_337_2_661_3_002', color=colors[13])
plt.plot(Wavelength, CO1_387_2_611_3_002['Spectral_Radiance'], label='CO1_387_2_611_3_002', color=colors[12])
plt.plot(Wavelength, CO1_437_2_561_3_002['Spectral_Radiance'], label='CO1_437_2_561_3_002', color=colors[11])
plt.plot(Wavelength, CO1_487_2_511_3_002['Spectral_Radiance'], label='CO1_487_2_511_3_002', color=colors[10])
plt.plot(Wavelength, CO1_537_2_461_3_002['Spectral_Radiance'], label='CO1_537_2_461_3_002', color=colors[9])
plt.plot(Wavelength, CO1_587_2_411_3_002['Spectral_Radiance'], label='CO1_587_2_411_3_002', color=colors[8])
plt.plot(Wavelength, CO1_637_2_361_3_002['Spectral_Radiance'], label='CO1_637_2_361_3_002', color=colors[7])
plt.plot(Wavelength, CO1_687_2_311_3_002['Spectral_Radiance'], label='CO1_687_2_311_3_002', color=colors[6])
plt.plot(Wavelength, CO1_737_2_261_3_002['Spectral_Radiance'], label='CO1_737_2_261_3_002', color=colors[5])
plt.plot(Wavelength, CO1_787_2_211_3_002['Spectral_Radiance'], label='CO1_787_2_211_3_002', color=colors[4])
plt.plot(Wavelength, CO1_837_2_161_3_002['Spectral_Radiance'], label='CO1_837_2_161_3_002', color=colors[3])
plt.plot(Wavelength, CO1_887_2_111_3_002['Spectral_Radiance'], label='CO1_887_2_111_3_002', color=colors[2])
plt.plot(Wavelength, CO1_937_2_061_3_002['Spectral_Radiance'], label='CO1_937_2_061_3_002', color=colors[1])

plt.plot(Wavelength, Full['Spectral_Radiance'], label='1_987_2_001_3_002', color=colors[0])

plt.xlim(4.8,4.9)
# plt.legend()
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Titan atmosphere spectral radiance dependance\n on ratios of ' + r'$^{12}C^{16}O$ and $^{13}C^{16}O$' +' isotopes')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')

# divider = make_axes_locatable(ax)
# colorbar_axes = divider.append_axes("right",
#                                     size="10%",
#                                     pad=0.1)
# plt.colorbar(ax, cmap=colors, ticks=np.linspace(0,2,N), 
#              boundaries=np.arange(-0.05,2.1,.1))

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
plt.colorbar(sm, ticks=np.linspace(0,1,10), cax=cax,
             boundaries=np.arange(-0.05,1), label=r'$^{13}C^{16}O/^{12}C^{16}O$')

# fig.tight_layout(rect=[.1,0,.9,1]) 
plt.tight_layout()


fig.savefig("Figures/Titan_CO12_Ratios.png", dpi=300)

plt.show()




