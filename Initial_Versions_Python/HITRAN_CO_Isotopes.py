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

HITRAN_Directory = "/Users/elitzer/Desktop/NASA_Titan/CO_Data/"
CO_file_name = HITRAN_Directory + "CO_Isotope_Transitions2.txt"


df_CO = pd.read_csv(CO_file_name, dtype=np.float64, sep=',', header=0)
# print(df_CO.columns, '\n', df_CO, '\nMax:', np.max(df_CO["sw"]))

plt.plot(1e4/df_CO["nu"][df_CO['local_iso_id'] == 1], df_CO["sw"][df_CO['local_iso_id'] == 1], alpha=1, linewidth=1, label="CO 5:1")
plt.plot(1e4/df_CO["nu"][df_CO['local_iso_id'] == 2], df_CO["sw"][df_CO['local_iso_id'] == 2], alpha=1, linewidth=1, label="CO 5:2")
plt.plot(1e4/df_CO["nu"][df_CO['local_iso_id'] == 3], df_CO["sw"][df_CO['local_iso_id'] == 3], alpha=1, linewidth=1, label="CO 5:3")
plt.plot(1e4/df_CO["nu"][df_CO['local_iso_id'] == 4], df_CO["sw"][df_CO['local_iso_id'] == 4], alpha=1, linewidth=1, label="CO 5:4")


plt.yscale('log')
plt.legend()
plt.title("CO Isotope Line Intensity [HITRAN]")
plt.xlabel(r'$Wavelength (µm)$')
plt.ylabel("Line intensity  "+r"( $\frac{cm^{-1}}{molec.cm^2}$ )")
plt.savefig("Figures/CO_Isotope_Line_Intensity_HITRAN.png", dpi=300)
plt.show()



"""
CO
--

The fields output for this profile are listed in order below with format strings, units and description the following information: :

global_iso_id
-------------
Data type: int
Units: [dimensionless]
Description: Unique integer ID of a particular isotopologue: every global isotopologue ID is unique to a particular species, even between different molecules. The number itself is, however arbitrary.

molec_id
--------
Data type: int
Units: [dimensionless]
Description: The HITRAN integer ID for this molecule in all its isotopologue forms

local_iso_id
------------
Data type: int
Units: [dimensionless]
Description: Integer ID of a particular Isotopologue, unique only to a given molecule, in order or abundance (1 = most abundant)

nu
--
Data type: float
Units: cm-1
Description: Transition wavenumber

sw
--
Data type: float
Units: cm-1/(molec.cm-2)
Description: Line intensity, multiplied by isotopologue abundance, at T = 296 K

a
-
Data type: float
Units: s-1
Description: Einstein A-coefficient in s-1

trans_id
--------
Data type: int
Units: [dimensionless]
Description: Unique integer ID of a particular transition entry in the database. (The same physical transition may have different IDs if its parameters have been revised or updated).

nu-err
------
Data type: int
Units: [dimensionless]
Description: HITRAN uncertainty code for nu

sw-err
------
Data type: int
Units: [dimensionless]
Description: HITRAN uncertainty code for sw

nu-ref
------
Data type: int
Units: [dimensionless]
Description: Source (reference) ID for nu

sw-ref
------
Data type: int
Units: [dimensionless]
Description: Source (reference) ID for sw

"""