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
Full_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.987_2_0.011_3_0.002_R15000_4.5_5um_PSG.txt'

Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Wavelength = Full['Wavelength']

CO1_937_2_011_3_052_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.937_2_0.011_3_0.052_R15000_4.5_5um_PSG.txt'
CO1_937_2_011_3_052 = np.genfromtxt(CO1_937_2_011_3_052_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_887_2_011_3_10_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.887_2_0.011_3_0.102_R15000_4.5_5um_PSG.txt'
CO1_887_2_011_3_10 = np.genfromtxt(CO1_887_2_011_3_10_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_837_2_011_3_152_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.837_2_0.011_3_0.152_R15000_4.5_5um_PSG.txt'
CO1_837_2_011_3_152 = np.genfromtxt(CO1_837_2_011_3_152_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_787_2_011_3_202_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.787_2_0.011_3_0.202_R15000_4.5_5um_PSG.txt'
CO1_787_2_011_3_202 = np.genfromtxt(CO1_787_2_011_3_202_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_737_2_011_3_252_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.737_2_0.011_3_0.252_R15000_4.5_5um_PSG.txt'
CO1_737_2_011_3_252 = np.genfromtxt(CO1_737_2_011_3_252_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_687_2_011_3_302_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.687_2_0.011_3_0.302_R15000_4.5_5um_PSG.txt'
CO1_687_2_011_3_302 = np.genfromtxt(CO1_687_2_011_3_302_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_637_2_011_3_352_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.637_2_0.011_3_0.352_R15000_4.5_5um_PSG.txt'
CO1_637_2_011_3_352 = np.genfromtxt(CO1_637_2_011_3_352_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_587_2_011_3_402_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.587_2_0.011_3_0.402_R15000_4.5_5um_PSG.txt'
CO1_587_2_011_3_402 = np.genfromtxt(CO1_587_2_011_3_402_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_537_2_011_3_452_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.537_2_0.011_3_0.452_R15000_4.5_5um_PSG.txt'
CO1_537_2_011_3_452 = np.genfromtxt(CO1_537_2_011_3_452_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_487_2_011_3_502_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.487_2_0.011_3_0.502_R15000_4.5_5um_PSG.txt'
CO1_487_2_011_3_502 = np.genfromtxt(CO1_487_2_011_3_502_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_437_2_011_3_552_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.437_2_0.011_3_0.552_R15000_4.5_5um_PSG.txt'
CO1_437_2_011_3_552 = np.genfromtxt(CO1_437_2_011_3_552_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_387_2_011_3_602_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.387_2_0.011_3_0.602_R15000_4.5_5um_PSG.txt'
CO1_387_2_011_3_602 = np.genfromtxt(CO1_387_2_011_3_602_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_337_2_011_3_652_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.337_2_0.011_3_0.652_R15000_4.5_5um_PSG.txt'
CO1_337_2_011_3_652 = np.genfromtxt(CO1_337_2_011_3_652_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_287_2_011_3_702_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.287_2_0.011_3_0.702_R15000_4.5_5um_PSG.txt'
CO1_287_2_011_3_702 = np.genfromtxt(CO1_287_2_011_3_702_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_237_2_011_3_752_File = PSG_Directory + '/Ratios/' +'CO13/' + 'Titan_atmosphere_ratios_CO1_0.237_2_0.011_3_0.752_R15000_4.5_5um_PSG.txt'
CO1_237_2_011_3_752 = np.genfromtxt(CO1_237_2_011_3_752_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_187_2_011_3_802_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.187_2_0.011_3_0.802_R15000_4.5_5um_PSG.txt'
CO1_187_2_011_3_802 = np.genfromtxt(CO1_187_2_011_3_802_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_137_2_011_3_852_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.137_2_0.011_3_0.852_R15000_4.5_5um_PSG.txt'
CO1_137_2_011_3_852 = np.genfromtxt(CO1_137_2_011_3_852_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_087_2_011_3_902_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.087_2_0.011_3_0.902_R15000_4.5_5um_PSG.txt'
CO1_087_2_011_3_902 = np.genfromtxt(CO1_087_2_011_3_902_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

CO1_037_2_011_3_952_File = PSG_Directory + '/Ratios/' + 'CO13/' + 'Titan_atmosphere_ratios_CO1_0.037_2_0.011_3_0.952_R15000_4.5_5um_PSG.txt'
CO1_037_2_011_3_952 = np.genfromtxt(CO1_037_2_011_3_952_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

N = 20
colors = plt.cm.viridis(np.linspace(0,1,N))

fig =plt.figure(dpi=300) 
# fig.set_size_inches(11, 5.25)
ax = plt.gca() 
# ax.set_aspect(25) 

plt.plot(Wavelength, Full['Spectral_Radiance'], label='1_987_2_001_3_002', color=colors[0])

plt.plot(Wavelength, CO1_937_2_011_3_052['Spectral_Radiance'], label='CO1_937_2_011_3_052', color=colors[1])
plt.plot(Wavelength, CO1_887_2_011_3_10['Spectral_Radiance'], label='CO1_887_2_011_3_10', color=colors[2])
plt.plot(Wavelength, CO1_837_2_011_3_152['Spectral_Radiance'], label='CO1_837_2_011_3_152', color=colors[3])
plt.plot(Wavelength, CO1_787_2_011_3_202['Spectral_Radiance'], label='CO1_787_2_011_3_202', color=colors[4])
plt.plot(Wavelength, CO1_737_2_011_3_252['Spectral_Radiance'], label='CO1_737_2_011_3_252', color=colors[5])
plt.plot(Wavelength, CO1_687_2_011_3_302['Spectral_Radiance'], label='CO1_687_2_011_3_302', color=colors[6])
plt.plot(Wavelength, CO1_637_2_011_3_352['Spectral_Radiance'], label='CO1_637_2_011_3_352', color=colors[7])
plt.plot(Wavelength, CO1_587_2_011_3_402['Spectral_Radiance'], label='CO1_587_2_011_3_402', color=colors[8])
plt.plot(Wavelength, CO1_537_2_011_3_452['Spectral_Radiance'], label='CO1_537_2_011_3_452', color=colors[9])
plt.plot(Wavelength, CO1_487_2_011_3_502['Spectral_Radiance'], label='CO1_487_2_011_3_502', color=colors[10])
plt.plot(Wavelength, CO1_437_2_011_3_552['Spectral_Radiance'], label='CO1_437_2_011_3_552', color=colors[11])
plt.plot(Wavelength, CO1_387_2_011_3_602['Spectral_Radiance'], label='CO1_387_2_011_3_602', color=colors[12])
plt.plot(Wavelength, CO1_337_2_011_3_652['Spectral_Radiance'], label='CO1_337_2_011_3_652', color=colors[13])
plt.plot(Wavelength, CO1_287_2_011_3_702['Spectral_Radiance'], label='CO1_287_2_011_3_702', color=colors[14])
plt.plot(Wavelength, CO1_237_2_011_3_752['Spectral_Radiance'], label='CO1_237_2_011_3_752', color=colors[15])
plt.plot(Wavelength, CO1_187_2_011_3_802['Spectral_Radiance'], label='CO1_187_2_011_3_802', color=colors[16])
plt.plot(Wavelength, CO1_137_2_011_3_852['Spectral_Radiance'], label='CO1_137_2_011_3_852', color=colors[17])
plt.plot(Wavelength, CO1_087_2_011_3_902['Spectral_Radiance'], label='CO1_087_2_011_3_902', color=colors[18])
plt.plot(Wavelength, CO1_037_2_011_3_952['Spectral_Radiance'], label='CO1_037_2_011_3_952', color=colors[19])



plt.xlim(4.8,4.9)
# plt.legend()
# ax.legend(loc='center left', bbox_to_anchor=(1.1, .5))
plt.title('Titan atmosphere spectral radiance dependance\n on ratios of ' + r'$^{12}C^{16}O$ and $^{12}C^{18}O$' +' isotopes')
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
# ax.colorbar()
fig.tight_layout(rect=[.1,0,.9,1.4]) 
# ax.set_aspect("auto")

# plt.legend()

norm = mpl.colors.Normalize(vmin=0,vmax=1)
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)
plt.colorbar(sm, ticks=np.linspace(0,1,10), cax=cax,
             boundaries=np.arange(-0.05,1), label=r'$^{12}C^{18}O/^{12}C^{16}O$')

# fig.tight_layout(rect=[.1,0,.9,1]) 
plt.tight_layout()

fig.savefig("Figures/Titan_CO13_Ratios.png", dpi=300)

plt.show()