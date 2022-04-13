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

PSG_CO_Directory = "/Users/elitzer/Desktop/PSG/Molecule_Spectra/"
CO1_file_name = PSG_CO_Directory + "12C16O_hitran05_1_26_26_Spectra.txt"
CO2_file_name = PSG_CO_Directory + "13C16O_hitran05_2_27_36_Spectra.txt"
CO3_file_name = PSG_CO_Directory + "12C18O_hitran05_3_28_28_Spectra.txt"
CO4_file_name = PSG_CO_Directory + "12C17O_hitran05_4_29_27_Spectra.txt"
CO5_file_name = PSG_CO_Directory + "13C18O_hitran05_5_30_38_Spectra.txt"
CO6_file_name = PSG_CO_Directory + "13C17O_hitran05_6_31_37_Spectra.txt"



df_CO1 = pd.read_csv(CO1_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Intensity', '?'])
df_CO2 = pd.read_csv(CO2_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Intensity', '?'])
df_CO3 = pd.read_csv(CO3_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Intensity', '?'])
df_CO4 = pd.read_csv(CO4_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Intensity', '?'])
df_CO5 = pd.read_csv(CO5_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Intensity', '?'])
df_CO6 = pd.read_csv(CO6_file_name, comment="#", dtype=np.float64, delim_whitespace=True, names=['Wavelength', 'Intensity', '?'])

plt.plot(1e4/df_CO1["Wavelength"], df_CO1["Intensity"], alpha=1, linewidth=1, label="CO 5:1")
plt.plot(1e4/df_CO2["Wavelength"], df_CO2["Intensity"], alpha=1, linewidth=1, label="CO 5:2")
plt.plot(1e4/df_CO3["Wavelength"], df_CO3["Intensity"], alpha=1, linewidth=1, label="CO 5:3")
plt.plot(1e4/df_CO4["Wavelength"], df_CO4["Intensity"], alpha=1, linewidth=1, label="CO 5:4")
plt.plot(1e4/df_CO5["Wavelength"], df_CO5["Intensity"], alpha=1, linewidth=1, label="CO 5:5")
plt.plot(1e4/df_CO6["Wavelength"], df_CO6["Intensity"], alpha=1, linewidth=1, label="CO 5:6")



# plt.yscale('log')
plt.legend()
plt.title("CO Isotope [PSG]")
plt.xlabel(r'$Wavelength (µm)$')
plt.xlim(4.7,5)
plt.ylim(10e-34,10e-19)
# plt.ylabel("Line intensity  "+r"( $\frac{cm^{-1}}{molec.cm^2}$ )")
plt.savefig("Figures/CO_Isotope_PSG_4.7_5um.png", dpi=300)
plt.show()