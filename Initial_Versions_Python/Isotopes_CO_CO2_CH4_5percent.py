from ast import Load
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


def Load_Spec(file):
    Isotope = file[0:3]
    if Isotope == 'CO_':
        Data_File = CO_Directory + file + '.txt'
    elif Isotope == 'CO2':
        Data_File = CO2_Directory + file + '.txt'    
    elif Isotope == 'CH4':
        Data_File = CH4_Directory + file + '.txt'

    Data_array = np.genfromtxt(Data_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
    # Data_array = np.asarray(Data_array)
    return Data_array


PSG_Directory = "/Users/elitzer/Desktop/PSG/Atmospheric_Simulations/Isotopes/"
CO_Directory = PSG_Directory + 'CO/5%/'
CO2_Directory = PSG_Directory + 'CO2/5%/'
CH4_Directory = PSG_Directory + 'CH4/5%/'

Full_File_45_5 = PSG_Directory + 'Full_File_4.5_5mum.txt'
Full_File_375_45 = PSG_Directory + 'Full_File_3.75_4.5mum.txt'
CO2_Full_File = PSG_Directory + 'CO2_Full.txt'
CH4_Full_File = PSG_Directory + 'CH4_Full.txt'

Full_45_5 = np.genfromtxt(Full_File_45_5, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
Full_375_45 = np.genfromtxt(Full_File_375_45, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
CO2_Full = np.genfromtxt(CO2_Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
CH4_Full = np.genfromtxt(CH4_Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

#%% Load in CO isotope data

# CO_1 = 0.987 +- .05 Scalar in .01 Scalar increments (other isotopes are standart Titan isotopes)
CO_1_937 = Load_Spec('CO_1_937')
CO_1_947 = Load_Spec('CO_1_947')
CO_1_957 = Load_Spec('CO_1_957')
CO_1_967 = Load_Spec('CO_1_967')
CO_1_977 = Load_Spec('CO_1_977')
#Full_45_5
CO_1_997 = Load_Spec('CO_1_997')
CO_1_1007 = Load_Spec('CO_1_1007')
CO_1_1017 = Load_Spec('CO_1_1017')
CO_1_1027 = Load_Spec('CO_1_1027')
CO_1_1037 = Load_Spec('CO_1_1037')

CO_1_array = [CO_1_937, CO_1_947, CO_1_957, CO_1_967, CO_1_977, Full_45_5, CO_1_997, CO_1_1007, CO_1_1017, CO_1_1027, CO_1_1037]

# CO_2 = 0.011 +- .05 Scalar in .01 Scalar increments (other isotopes are standart Titan isotopes)
CO_2_006 = Load_Spec('CO_2_006')
CO_2_007 = Load_Spec('CO_2_007')
CO_2_008 = Load_Spec('CO_2_008')
CO_2_009 = Load_Spec('CO_2_009')
CO_2_010 = Load_Spec('CO_2_010')
#Full_45_5
CO_2_012 = Load_Spec('CO_2_012')
CO_2_013 = Load_Spec('CO_2_013')
CO_2_014 = Load_Spec('CO_2_014')
CO_2_015 = Load_Spec('CO_2_015')
CO_2_016 = Load_Spec('CO_2_016')
CO_2_array = [CO_2_006, CO_2_007, CO_2_008, CO_2_009, CO_2_010, Full_45_5, CO_2_012, CO_2_013, CO_2_014, CO_2_015, CO_2_016]

# CO_3 = 0.002 +- .05, .02 Scalar in .01 Scalar increments (other isotopes are standart Titan isotopes)
CO_3_000 = Load_Spec('CO_3_000')
CO_3_001 = Load_Spec('CO_3_001')
#Full_45_5
CO_3_003 = Load_Spec('CO_3_003')
CO_3_004 = Load_Spec('CO_3_004')
CO_3_005 = Load_Spec('CO_3_005')
CO_3_006 = Load_Spec('CO_3_006')
CO_3_007 = Load_Spec('CO_3_007')
CO_3_008 = Load_Spec('CO_3_008')
CO_3_array = [CO_3_000, CO_3_001, Full_45_5, CO_3_003, CO_3_004, CO_3_005, CO_3_006, CO_3_007, CO_3_008]

CO_isotope_numbers = ['12C16O','13C16O','12C18O']
#%% Load in CO2 data

# CO2 = 1.00 +- .05 Scalar in .01 Scalar increments (other isotopes are standart Titan isotopes)
CO2_095 = Load_Spec('CO2_095')
CO2_096 = Load_Spec('CO2_096')
CO2_097 = Load_Spec('CO2_097')
CO2_098 = Load_Spec('CO2_098')
CO2_099 = Load_Spec('CO2_099')
#Full_375_45
CO2_101 = Load_Spec('CO2_101')
CO2_102 = Load_Spec('CO2_102')
CO2_103 = Load_Spec('CO2_103')
CO2_104 = Load_Spec('CO2_104')
CO2_105 = Load_Spec('CO2_105')
CO2_array = [CO2_095, CO2_096, CO2_097, CO2_098, CO2_099, CO2_Full, CO2_101, CO2_102, CO2_103, CO2_104, CO2_105]
#%% Load in CH4 data
# CH4_1 = 1.00 +- .05 Scalar in .01 Scalar increments (other isotopes are standart Titan isotopes)
# ** Need to check scalar interval!!
CH4_1_095 = Load_Spec('CH4_1_095')
CH4_1_096 = Load_Spec('CH4_1_096')
CH4_1_097 = Load_Spec('CH4_1_097')
CH4_1_098 = Load_Spec('CH4_1_098')
CH4_1_099 = Load_Spec('CH4_1_099')
CH4_1_100 = Load_Spec('CH4_1_100')
CH4_1_101 = Load_Spec('CH4_1_101')
CH4_1_102 = Load_Spec('CH4_1_102')
CH4_1_103 = Load_Spec('CH4_1_103')
CH4_1_104 = Load_Spec('CH4_1_104')
CH4_1_105 = Load_Spec('CH4_1_105')
CH4_1_array = [CH4_1_095, CH4_1_096, CH4_1_097, CH4_1_098, CH4_1_099, CH4_1_100, CH4_1_101, CH4_1_102, CH4_1_103, CH4_1_104, CH4_1_105]

# CH4_2 = 1.00 +- .05 Scalar in .01 Scalar increments (other isotopes are standart Titan isotopes)
CH4_2_095 = Load_Spec('CH4_2_095')
CH4_2_096 = Load_Spec('CH4_2_096')
CH4_2_097 = Load_Spec('CH4_2_097')
CH4_2_098 = Load_Spec('CH4_2_098')
CH4_2_099 = Load_Spec('CH4_2_099')
CH4_2_100 = Load_Spec('CH4_2_100')
CH4_2_101 = Load_Spec('CH4_2_101')
CH4_2_102 = Load_Spec('CH4_2_102')
CH4_2_103 = Load_Spec('CH4_2_103')
CH4_2_104 = Load_Spec('CH4_2_104')
CH4_2_105 = Load_Spec('CH4_2_105')
CH4_2_array = [CH4_2_095, CH4_2_096, CH4_2_097, CH4_2_098, CH4_2_099, CH4_2_100, CH4_2_101, CH4_2_102, CH4_2_103, CH4_2_104, CH4_2_105]
CH4_isotope_numbers = ['12CH_4','13CH_4']

#%%

def plot_isotopes(data_array, molecule_isotope_num, min_max, Full_file):
    molecule, isotope_num = molecule_isotope_num

    fig = plt.figure(dpi=300)
    N = len(data_array) + 1
    colors = plt.cm.viridis(np.linspace(0,1,N))

    for i, Isotope in enumerate(data_array):
        plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'], label='{Isotope}', color=colors[i+1])
    
    if molecule == 'CO':
        plt.xlim(4.8,4.9)
        plt.title('Titan atmosphere spectral radiance dependance\n on scalar values of ' + CO_isotope_numbers[isotope_num-1])
        chem_form = CO_isotope_numbers[isotope_num-1]
        savetitle = "CO_" + CO_isotope_numbers[isotope_num-1] + '5%'
    if molecule == 'CO2':
        # plt.xlim(4.2,4.35)
        plt.title('Titan atmosphere spectral radiance dependance\n on scalar values of ' + r'$CO_2$')
        chem_form = 'CO_2'
        savetitle = "CO2_" + '5%'

    if molecule == 'CH4':
        plt.xlim(2.75,3.5)
        plt.title('Titan atmosphere spectral radiance dependance\n on scalar values of ' + CH4_isotope_numbers[isotope_num-1])
        chem_form = CH4_isotope_numbers[isotope_num-1]
        savetitle = "CH4_" + CH4_isotope_numbers[isotope_num-1] + '5%'

    
    plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
    plt.xlabel("Wavelength" + ' (µm)')

    ax = plt.gca() 

    norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.15)
    cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label=chem_form)

    plt.tight_layout()
    fig.savefig("Figures/" + savetitle + ".png", dpi=300)


def plot_isotope_diff(data_array, molecule_isotope_num, min_max, Full_file):
    molecule, isotope_num = molecule_isotope_num

    fig = plt.figure(dpi=300)
    N = len(data_array) + 1
    colors = plt.cm.viridis(np.linspace(0,1,N))

    for i, Isotope in enumerate(data_array):
        plt.plot(Full_file['Wavelength'], Isotope['Spectral_Radiance'] - Full_file['Spectral_Radiance'], label='{Isotope}', color=colors[i+1])
    
    if molecule == 'CO':
        plt.xlim(4.8,4.9)
        plt.title('Titan atmosphere spectral radiance dependance difference\n on scalar values of ' + CO_isotope_numbers[isotope_num-1])
        chem_form = CO_isotope_numbers[isotope_num-1]
        savetitle = "CO_" + CO_isotope_numbers[isotope_num-1] + '5%_diff'
    
    if molecule == 'CO2':
        # plt.xlim(4.2,4.35)
        plt.title('Titan atmosphere spectral radiance dependance difference\n on scalar values of ' + r'$CO_2$')
        chem_form = 'CO_2'
        savetitle = "CO2_" + '5%_diff'

    if molecule == 'CH4':
        plt.xlim(2.75,3.5)
        plt.title('Titan atmosphere spectral radiance dependance difference\n on scalar values of ' + CH4_isotope_numbers[isotope_num-1])
        chem_form = CH4_isotope_numbers[isotope_num-1]
        savetitle = "CH4_" + CH4_isotope_numbers[isotope_num-1] + '5%_diff'

    
    plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
    plt.xlabel("Wavelength" + ' (µm)')

    ax = plt.gca() 

    norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.15)
    cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label=chem_form)

    plt.tight_layout()
    fig.savefig("Figures/" + savetitle + ".png", dpi=300)




#%% Plot CO Isotopes and difference from titan's atmosphere
plot_isotopes(CO_1_array, ('CO', 1), [.937, 1.037, .01], Full_45_5)
plot_isotope_diff(CO_1_array, ('CO', 1), [.937, 1.037, .01], Full_45_5)

plot_isotopes(CO_2_array, ('CO', 2), [.006, .016, .001], Full_45_5)
plot_isotope_diff(CO_2_array, ('CO', 2), [.006, .016, .001], Full_45_5)

plot_isotopes(CO_3_array, ('CO', 3), [0, 0.008, .001], Full_45_5)
plot_isotope_diff(CO_3_array, ('CO', 3), [0, 0.008, .001], Full_45_5)

#%% Plot CO2 and difference from titan's atmosphere
plot_isotopes(CO2_array, ('CO2', 0), [.95, 1.05, .01], CO2_Full)
plot_isotope_diff(CO2_array, ('CO2', 0), [.95, 1.05, .01], CO2_Full)

#%% Plot CH4 isotopes and difference from titan's atmosphere
plot_isotopes(CH4_1_array, ('CH4', 1), [.95, 1.05, .01], CH4_1_100) #CH4_Full)
plot_isotope_diff(CH4_1_array, ('CH4', 1), [.95, 1.05, .01], CH4_1_100)#CH4_Full)

plot_isotopes(CH4_1_array, ('CH4', 2), [.95, 1.05, .01], CH4_2_100)#CH4_Full)
plot_isotope_diff(CH4_1_array, ('CH4', 2), [.95, 1.05, .01], CH4_2_100)#CH4_Full)




# plt.show()


# %%

# def make_panda(data, isotope):
#     Wavelength = []
#     Data = []
#     for i in range(0, len(data)):
#         Wavelength.append(data[i][0][0])
#         Data.append(data[i][0][1])
#     Wavelength = np.array(Wavelength)
#     Data = np.array(Data)
#     return Wavelength, Data

# CO_W, CO_D = make_panda(CO_1_array, 'CO')
# print(CO_W)2
CO_1_array = np.array(CO_1_array)
CO_2_array = np.array(CO_2_array)
CO_3_array = np.array(CO_3_array)

CO2_array = np.array(CO2_array)

CH4_1_array = np.array(CH4_1_array)
CH4_2_array = np.array(CH4_2_array)


CO_1_pddf = pd.DataFrame(data= CO_1_array[:]['Spectral_Radiance'].T,
                        columns = [i for i in ['CO_1_937', 'CO_1_947', 'CO_1_957', 'CO_1_967', 'CO_1_977', 'CO_1_1', 'CO_1_997', 'CO_1_1007', 'CO_1_1017', 'CO_1_1027', 'CO_1_1037']],
                        index = CO_1_array[0]["Wavelength"])
CO_2_pddf = pd.DataFrame(data= CO_2_array[:]['Spectral_Radiance'].T,
                        columns = [i for i in ['CO_2_006', 'CO_2_007', 'CO_2_008', 'CO_2_009', 'CO_2_010', 'CO_2_011', 'CO_2_012', 'CO_2_013', 'CO_2_014', 'CO_2_015', 'CO_2_016']],
                        index = CO_2_array[0]["Wavelength"])
CO_3_pddf = pd.DataFrame(data= CO_3_array[:]['Spectral_Radiance'].T,
                        columns = [i for i in ['CO_3_000', 'CO_3_001', 'CO_3_002', 'CO_3_003', 'CO_3_004', 'CO_3_005', 'CO_3_006', 'CO_3_007', 'CO_3_008']],
                        index = CO_3_array[0]["Wavelength"])

CO2_pddf = pd.DataFrame(data= CO2_array[:]['Spectral_Radiance'].T,
                        columns = [i for i in ['CO2_095', 'CO2_096', 'CO2_097', 'CO2_098', 'CO2_099', 'CO2_1', 'CO2_101', 'CO2_102', 'CO2_103', 'CO2_104', 'CO2_105']],
                        index = CO2_array[0]["Wavelength"])

CH4_1_pddf = pd.DataFrame(data= CH4_1_array[:]['Spectral_Radiance'].T,
                        columns = [i for i in ['CH4_1_095', 'CH4_1_096', 'CH4_1_097', 'CH4_1_098', 'CH4_1_099', 'CH4_1_100', 'CH4_1_101', 'CH4_1_102', 'CH4_1_103', 'CH4_1_104', 'CH4_1_105']],
                        index = CH4_1_array[0]["Wavelength"])

CH4_2_pddf = pd.DataFrame(data= CH4_2_array[:]['Spectral_Radiance'].T,
                        columns = [i for i in ['CH4_2_095', 'CH4_2_096', 'CH4_2_097', 'CH4_2_098', 'CH4_2_099', 'CH4_2_100', 'CH4_2_101', 'CH4_2_102', 'CH4_2_103', 'CH4_2_104', 'CH4_2_105']],
                        index = CH4_2_array[0]["Wavelength"])

with pd.ExcelWriter('CO.xlsx') as writer:
    CO_1_pddf.to_excel(writer, sheet_name='CO1')
    CO_2_pddf.to_excel(writer, sheet_name='CO2')
    CO_3_pddf.to_excel(writer, sheet_name='CO3')

with pd.ExcelWriter('CO2.xlsx') as writer:
    CO2_pddf.to_excel(writer, sheet_name='CO2')

with pd.ExcelWriter('CH4.xlsx') as writer:
    CH4_1_pddf.to_excel(writer, sheet_name='CH4_1')
    CH4_2_pddf.to_excel(writer, sheet_name='CH4_2')

# %%
