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




### Identify Files ###
PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CO/"
CO123_file_name = PSG_Directory + "Titan_atmosphere_CO123_R15000_4.5_5um_PSG.txt"
CO12_file_name = PSG_Directory + "Titan_atmosphere_CO12_R15000_4.5_5um_PSG_2.txt"
CO13_file_name = PSG_Directory + "Titan_atmosphere_CO13_R15000_4.5_5um_PSG_2.txt"
CO23_file_name = PSG_Directory + "Titan_atmosphere_CO23_R15000_4.5_5um_PSG_2.txt"
        ### Titan CO Spectra: Note that _2 appended to end signifies that the ratios stay constant 
        #Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 4.5-5um:      "Titan_atmosphere_CO123_R15000_4.5_5um_PSG.txt"
        #Titan R15000 CO [5,1]0.987 [5,2]0.013 [5,3]0.00 4.5-5um:       "Titan_atmosphere_CO12_R15000_4.5_5um_PSG.txt"
        #Titan R15000 CO [5,1]0.987 [5,2]0.00 [5,3]0.013 4.5-5um:       "Titan_atmosphere_CO13_R15000_4.5_5um_PSG.txt"
        #Titan R15000 CO [5,1]0.987 [5,2]0.82 [5,3]0.18 4.5-5um:        "Titan_atmosphere_CO23_R15000_4.5_5um_PSG.txt"

### Read files into Dataframes ###
df_CO123 = pd.read_csv(CO123_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])
df_CO12 = pd.read_csv(CO12_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])
df_CO13 = pd.read_csv(CO13_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])
df_CO23 = pd.read_csv(CO23_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])


### Plot all spectra curves ###
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(df_CO123["Wavelength"], df_CO123["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:1,2,3]")
ax1.plot(df_CO12["Wavelength"], df_CO12["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:1,2]")
ax1.plot(df_CO13["Wavelength"], df_CO13["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:1,3]")
ax1.plot(df_CO23["Wavelength"], df_CO23["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:2,3]")

ax1.set_title("Titan NIR Radiance Modified Ratios")
ax1.set_xlabel("Wavelength (µm)")
ax1.set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
ax1.legend()
# ax1.set_yscale('log')
ax1.set_aspect(100)
ax1.set_xlim(4.5,5)
# ax1.set_aspect(.125)
fig1.tight_layout()
fig1.savefig("Figures/Titan_NIR_SR__CO123_CO12_CO13_CO23_Lin_2.png", dpi=300)


### Find Isotope contribution through subtracting partial spectra from full spectra ###
df_CO3 = pd.DataFrame(df_CO123["Wavelength"], columns=["Wavelength"])
df_CO3["Spectral Radiance"] = df_CO123["Spectral Radiance"] - df_CO12["Spectral Radiance"]

df_CO2 = pd.DataFrame(df_CO123["Wavelength"], columns=["Wavelength"])
df_CO2["Spectral Radiance"] = df_CO123["Spectral Radiance"] - df_CO13["Spectral Radiance"]

df_CO1 = pd.DataFrame(df_CO123["Wavelength"], columns=["Wavelength"])
df_CO1["Spectral Radiance"] = df_CO123["Spectral Radiance"] - df_CO23["Spectral Radiance"]

### Difference in Isotope spectra ###

df_dCO12 = pd.DataFrame(df_CO1["Wavelength"], columns=["Wavelength"])
df_dCO12["Spectral Radiance"] = abs(df_CO1["Spectral Radiance"]) - abs(df_CO2["Spectral Radiance"])

df_dCO13 = pd.DataFrame(df_CO1["Wavelength"], columns=["Wavelength"])
df_dCO13["Spectral Radiance"] = abs(df_CO1["Spectral Radiance"]) - abs(df_CO3["Spectral Radiance"])

df_dCO23 = pd.DataFrame(df_CO1["Wavelength"], columns=["Wavelength"])
df_dCO23["Spectral Radiance"] = abs(df_CO2["Spectral Radiance"]) - abs(df_CO3["Spectral Radiance"])


### Plot each isotope ###
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.plot(df_CO1["Wavelength"], df_CO1["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:1]")
ax2.plot(df_CO2["Wavelength"], df_CO2["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:2]")
ax2.plot(df_CO3["Wavelength"], df_CO3["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:3]")

ax2.set_title("Titan CO Difference Modified Ratios")
ax2.set_xlabel("Wavelength (µm)")
ax2.set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
ax2.legend()
# ax2.set_yscale('log')
ax2.set_xlim(4.5,5)
ax2.set_aspect("auto")
ax2.set_aspect(75)
fig2.tight_layout()
fig2.savefig("Figures/Titan_NIR_SR_CO_isotopes__CO1_CO2_CO3_Lin_2.png", dpi=300)


### Plot the difference contribution of each isotope ###
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)

ax3.plot(df_dCO12["Wavelength"], df_dCO12["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:1]- [5:2]")
ax3.plot(df_dCO13["Wavelength"], df_dCO13["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:1] -[5:3]")
ax3.plot(df_dCO23["Wavelength"], df_dCO23["Spectral Radiance"], alpha=1, linewidth=1, label="CO [5:2] - [5:3]")

ax3.set_title("Titan CO Difference Modified Ratios")
ax3.set_xlabel("Wavelength (µm)")
ax3.set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
ax3.legend()
ax3.set_xlim(4.5,5)
ax3.set_aspect("auto")
ax3.set_aspect(75)
# adjustFigAspect(fig3,aspect=.75)
fig3.tight_layout()
fig3.savefig("Figures/Titan_NIR_SR_CO_isotope_diff__CO1_CO2_CO3_Difference_Lin_2.png", dpi=300)


plt.show()