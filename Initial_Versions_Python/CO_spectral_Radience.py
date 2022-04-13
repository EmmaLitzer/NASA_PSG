import numpy as np
import scipy as sp
import astropy as ap
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import time
import os
import sys

PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Resolutions/"
PICTURE_file_name = PSG_Directory + "Titan_atmosphere_CO123_R15000_4.5_5um_PSG.txt"
JWST_file_name = PSG_Directory + "Titan_atmosphere_CO123_R2700_4.5_5um_PSG.txt"
VIMS_file_name = PSG_Directory + "Titan_atmosphere_CO123_R270_4.5_5um_PSG.txt"
        #Titan R15000 CO [5,1] [5,2] [5,3] PICTURE 4.5-5um:     "Titan_atmosphere_CO123_R15000_4.5_5um_PSG.txt"
        #Titan R2700 CO [5,1] [5,2] [5,3] JWST 4.5-5um:         "Titan_atmosphere_CO123_R2700_4.5_5um_PSG.txt"
        #Titan R270 CO [5,1] [5,2] [5,3] VIMS 4.5-5um:          "Titan_atmosphere_CO123_R270_4.5_5um_PSG.txt"

df_PICTURE = pd.read_csv(PICTURE_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])
df_JWST = pd.read_csv(JWST_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])
df_VIMS = pd.read_csv(VIMS_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])

# print(df, '\n',df.shape, df.dtypes)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(df_PICTURE["Wavelength"], df_PICTURE["Spectral Radiance"], alpha=1, linewidth=1, label="PICTURE (R=15000)")
ax1.plot(df_JWST["Wavelength"], df_JWST["Spectral Radiance"], alpha=1, linewidth=1, label="JWST (R=2700)")
ax1.plot(df_VIMS["Wavelength"], df_VIMS["Spectral Radiance"], alpha=1, linewidth=1, label="VIMS (R=270)")
ax1.set_title("Titan NIR Radiance")
ax1.set_xlabel("Wavelength (µm)")
ax1.set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
ax1.legend()
ax1.set_yscale('log')
ax1.set_xlim(4.5,5)
ax1.set_aspect(.125)
# fig1.savefig("Figures/Titan_NIR_SR__PICTURE_JWST_VIMS.png", dpi=300)





plt.show()
