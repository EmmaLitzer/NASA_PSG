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
print("All packages loaded")


print("\tAstropy version:", ap.version.version,
        "\n\tNumpy Version:", np.version.version,
        "\n\tScipy Version:", sp.version.version,
        "\n\tPandas Version:", pd.__version__,
        "\n\tMatplotlib Version:", matplotlib.__version__,
        "\n\tSeaborn Version:", sns.__version__)

print(time.asctime())
print(time.strftime("%a_%d_%b_%Y_%Hh%Mm%Ss"))

"""
To fix python version issue (VSCode not initiallizing env):
Settings > inheritEnv > terminal.integrated.inheritEnv = False/no check mark
Reload terminal
"""

# CO_Spectral_Radience.py               Compare R spectra of Titan
# Titan_CO_Isotopes.py                  Compare Isotope spectra (Titan and Individual contribution of CO)
# HAPI_Data.py                          HAPI API 
# HITRAN_CO_Isotopes.py                 HITRAN Data analysis of CO
# PSG_CO_Isotopes.py                    PSG HITRAN CO Isotope individual data file analysis
# CO12_Vary_Ratio.py                    Vary PSG ratios of CO 1 and CO 2 by .05 scalar increment
# CO13_Vary_Ratio.py                    Vary PSG ratios of CO 1 and CO 3 by .05 scalar increment
# Ratios.py                             Base copy of CO12,CO13_Vary_Ratios.py
# Titan_CO_Isotopes.py                  View individual isotope contribution
# Isotopes.py                           Attempt to view individual isotope contributin (Fails)
# CH4_12_Ratios.py                      Plot ratios of CH4 1 and 2 as varying scalar increment by 0.05
# CO2_Vary_Scalar.py                    Plot large variations of CO2 in Titan's atmosphere from 0 to 1 in .05 scalar increments
# CO2_Vary_small_scalar.py              Plot small variations of CO2 in Titan's atmosphere from .9 to 1.1 in .01 scalar increments
# CO12_Vary_Small_Ratio.py              Plot small variations of CO 1,2,3 in Titan's atmosphere from .9 to 1.1 in .01 scalar increments

PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/"

### Look at different Isotopes (get rid of one isotope in each PSG to see that isotopes contribution) ### Titan_CO_Isotopes.py 
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 4.5-5um:      "Titan_atmosphere_CO123_R15000_4.5_5um_PSG.txt"
#Titan R15000 CO [5,1]0.987 [5,2]0.013 [5,3]0.00 4.5-5um:       "Titan_atmosphere_CO12_R15000_4.5_5um_PSG.txt"
#Titan R15000 CO [5,1]0.987 [5,2]0.00 [5,3]0.013 4.5-5um:       "Titan_atmosphere_CO13_R15000_4.5_5um_PSG.txt"
#Titan R15000 CO [5,1]0.987 [5,2]0.82 [5,3]0.18 4.5-5um:        "Titan_atmosphere_CO23_R15000_4.5_5um_PSG.txt"



### Vary ratio of CO1 and CO2 #### CO12_Vary_Ratios.py
# /Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CO/Ratios/CO12
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.987_2_0.011_3_0.002_R15000_4.5_5um_PSG.txt

#Titan R15000 CO [5,1]0.937 [5,2]0.061 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.937_2_0.061_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.887 [5,2]0.111 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.887_2_0.111_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.837 [5,2]0.161 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.837_2_0.161_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.787 [5,2]0.211 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.787_2_0.211_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.737 [5,2]0.261 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.737_2_0.261_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.687 [5,2]0.311 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.687_2_0.311_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.637 [5,2]0.361 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.637_2_0.361_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.587 [5,2]0.411 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.587_2_0.411_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.537 [5,2]0.461 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.537_2_0.461_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.487 [5,2]0.511 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.487_2_0.511_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.437 [5,2]0.561 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.437_2_0.561_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.387 [5,2]0.611 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.387_2_0.611_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.337 [5,2]0.661 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.337_2_0.661_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.287 [5,2]0.711 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.287_2_0.711_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.237 [5,2]0.761 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.237_2_0.761_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.187 [5,2]0.811 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.187_2_0.811_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.137 [5,2]0.861 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.137_2_0.861_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.087 [5,2]0.911 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.087_2_0.911_3_0.002_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.037 [5,2]0.961 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.037_2_0.961_3_0.002_R15000_4.5_5um_PSG.txt


### Vary ratio of CO1 and CO3 ### CO13_Vary_Ratios.py
# /Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/CO/Ratios/CO13
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 4.5-5um:      Titan_atmosphere_ratios_CO1_0.987_2_0.011_3_0.002_R15000_4.5_5um_PSG.txt

#Titan R15000 CO [5,1]0.937 [5,2]0.011 [5,3]0.052 4.5-5um:      Titan_atmosphere_ratios_CO1_0.937_2_0.011_3_0.052_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.887 [5,2]0.011 [5,3]0.102 4.5-5um:      Titan_atmosphere_ratios_CO1_0.887_2_0.011_3_0.102_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.837 [5,2]0.011 [5,3]0.152 4.5-5um:      Titan_atmosphere_ratios_CO1_0.837_2_0.011_3_0.152_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.787 [5,2]0.011 [5,3]0.202 4.5-5um:      Titan_atmosphere_ratios_CO1_0.787_2_0.011_3_0.202_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.737 [5,2]0.011 [5,3]0.252 4.5-5um:      Titan_atmosphere_ratios_CO1_0.737_2_0.011_3_0.252_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.687 [5,2]0.011 [5,3]0.302 4.5-5um:      Titan_atmosphere_ratios_CO1_0.687_2_0.011_3_0.302_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.637 [5,2]0.011 [5,3]0.352 4.5-5um:      Titan_atmosphere_ratios_CO1_0.637_2_0.011_3_0.352_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.587 [5,2]0.011 [5,3]0.402 4.5-5um:      Titan_atmosphere_ratios_CO1_0.587_2_0.011_3_0.402_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.537 [5,2]0.011 [5,3]0.452 4.5-5um:      Titan_atmosphere_ratios_CO1_0.537_2_0.011_3_0.452_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.487 [5,2]0.011 [5,3]0.502 4.5-5um:      Titan_atmosphere_ratios_CO1_0.487_2_0.011_3_0.502_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.437 [5,2]0.011 [5,3]0.552 4.5-5um:      Titan_atmosphere_ratios_CO1_0.437_2_0.011_3_0.552_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.387 [5,2]0.011 [5,3]0.602 4.5-5um:      Titan_atmosphere_ratios_CO1_0.387_2_0.011_3_0.602_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.337 [5,2]0.011 [5,3]0.652 4.5-5um:      Titan_atmosphere_ratios_CO1_0.337_2_0.011_3_0.652_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.287 [5,2]0.011 [5,3]0.702 4.5-5um:      Titan_atmosphere_ratios_CO1_0.287_2_0.011_3_0.702_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.237 [5,2]0.011 [5,3]0.752 4.5-5um:      Titan_atmosphere_ratios_CO1_0.237_2_0.011_3_0.752_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.187 [5,2]0.011 [5,3]0.802 4.5-5um:      Titan_atmosphere_ratios_CO1_0.187_2_0.011_3_0.802_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.137 [5,2]0.011 [5,3]0.852 4.5-5um:      Titan_atmosphere_ratios_CO1_0.137_2_0.011_3_0.852_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.087 [5,2]0.011 [5,3]0.902 4.5-5um:      Titan_atmosphere_ratios_CO1_0.087_2_0.011_3_0.902_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.037 [5,2]0.011 [5,3]0.952 4.5-5um:      Titan_atmosphere_ratios_CO1_0.037_2_0.011_3_0.952_R15000_4.5_5um_PSG.txt



### Vary ratio of CH4 1 and CH4 2 ### CH4_12_Ratios.py
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]1 [6,2]0_4.5-5um:            Titan_atmosphere_ratios_CO123_CH41_1_CH42_0_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.95 [6,2]0.05_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_95_CH42_05_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.90 [6,2]0.10_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_90_CH42_10_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.85 [6,2]0.15_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_85_CH42_15_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.80 [6,2]0.20_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_80_CH42_20_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.75 [6,2]0.25_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_75_CH42_25_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.70 [6,2]0.30_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_70_CH42_30_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.65 [6,2]0.35_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_65_CH42_35_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.60 [6,2]0.40_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_60_CH42_40_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.55 [6,2]0.45_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_55_CH42_45_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.50 [6,2]0.50_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_50_CH42_50_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.45 [6,2]0.55_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_45_CH42_55_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.40 [6,2]0.60_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_40_CH42_60_R15000_4.5_5um_PSG.txt *
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.35 [6,2]0.65_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_35_CH42_65_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.30 [6,2]0.70_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_30_CH42_70_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.25 [6,2]0.75_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_25_CH42_75_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.20 [6,2]0.80_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_20_CH42_80_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.15 [6,2]0.85_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_15_CH42_85_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.10 [6,2]0.90_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_10_CH42_90_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.05 [6,2]0.95_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_05_CH42_95_R15000_4.5_5um_PSG.txt
#Titan R15000 CO [5,1]0.987 [5,2]0.011 [5,3]0.002 CH4 [6,1]0.00 [6,2]1.00_4.5-5um:      Titan_atmosphere_ratios_CO123_CH41_0_CH42_1_R15000_4.5_5um_PSG.txt



