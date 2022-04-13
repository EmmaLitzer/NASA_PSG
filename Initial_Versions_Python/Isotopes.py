from tkinter import ON
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

"""
def Isotopes(files=[], isotopes=[], abundance=[], file_order=[], R=15000, molecule='CO', Wrange=[4.5, 5]):
    xmin, xmax = Wrange[0], Wrange[1]
    df_isotopes = {}
    fig = []
    ax = []
    for i, file_name in enumerate(files):
        df_isotopes[str(file_order[i])] = np.genfromtxt(file_name, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan'])
        df_isotopes[str(file_order[i])] = 

    fig[0] = plt.figure()
    fig[0] = ax[0].subplot(1)
    for i in enumerate(abundance):
        ax[0].plot(df_isotopes[0][0]["Wavelength"], df_isotopes[i][0]["Spectral Radiance"], alpha=1, linewidth=1, 
                    label="{0} {1} at {2}scalar".format(molecule, df_isotopes[i][1], df_isotopes[i][2], df_isotopes[i][3]))
    ax[0].set_title("{0} R={1}, isotopes:{2}, abundance:{3}".format(molecule, R, isotopes, abundance))
    ax[0].set_xlabel("Wavelength (µm)")
    ax[0].set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
    ax[0].legend()
    ax[0].set_aspect(100)
    ax[0].set_xlim(xmin, xmax)
    fig[0].tight_layout()
    # fig[0].savefig("Figures/Titan_NIR_SR__CO123_CO12_CO13_CO23_Lin_2.png", dpi=300)

        
def Subtract_Isotope_From_Full(Isotope_data=[], isotopes=[]):
    Full = Isotope_data[0][0]
    df_dif_isotopes = np.empty(len(isotopes))
    # df_dif_isotopes[0] = Full
    df_iso_isotopes = np.empty(len(Isotopes)*2-2)
    # df_iso_isotopes[0] = Full
    for i in range(0, len(isotopes)-1):
        df_dif_isotopes[i] = np.array(Full["Wavelength"], columns=["Wavelength"])
        df_dif_isotopes[i]["Spectral Radiance"] = Full["Spectral Radiance"] - Isotope_data[i][0]["Spectral Radiance"]
    
    if len(isotopes == 4):
        for i in range(0, len(isotopes)-1):
            df_iso_isotopes[i] = pd.DataFrame(Full["Wavelength"], columns=["Wavelength"])
            df_iso_isotopes[i]["Spectral Radiance"] = Full["Spectral Radiance"] - Isotope_data[i-1][0]["Spectral Radiance"]
            df_iso_isotopes[i+3] = pd.DataFrame(Full["Wavelength"], columns=["Wavelength"])
            df_iso_isotopes[i+3]["Spectral Radiance"] = Full["Spectral Radiance"] - Isotope_data[i-2][0]["Spectral Radiance"]
    
    return df_dif_isotopes, df_iso_isotopes
"""
###############################

def Isolate_Isotopes(data, isotopes=[], abundance=[], file_order=[], R=15000, molecule='CO', Wrange=[4.5,5]):
    df_iso_isotopes1 = []
    df_iso_isotopes2 = []

    fig2 = plt.figure()
    ax2 = fig2.subplots(1)

    for i in range(1, len(data)):

        # COd12 = 



        if i ==1:
            df_iso_isotopes1.append(abs(data[i][:,1] - data[i-2][:,1]))
            df_iso_isotopes2.append(abs(data[i][:,1] - data[i-3][:,1]))

            ax2.plot(data[0][:,0], df_iso_isotopes1[i-1], alpha=1, linewidth=1, 
                    label="{0} {1}-{2} at {3}scalar".format(molecule, file_order[i], file_order[i-2], abundance))
            ax2.plot(data[0][:,0], df_iso_isotopes2[i-1], alpha=1, linewidth=1, 
                    label="{0} {1}-{2} at {3}scalar".format(molecule, file_order[i], file_order[i-3], abundance))
        else:
            df_iso_isotopes1.append(abs(data[i][:,1] - data[i-1][:,1]))
            df_iso_isotopes2.append(abs(data[i][:,1] - data[i-2][:,1]))

            ax2.plot(data[0][:,0], df_iso_isotopes1[i-1], alpha=1, linewidth=1, 
                    label="{0} {1}-{2} at {3}scalar".format(molecule, file_order[i], file_order[i-1], abundance))
            ax2.plot(data[0][:,0], df_iso_isotopes2[i-1], alpha=1, linewidth=1, 
                    label="{0} {1}-{2} at {3}scalar".format(molecule, file_order[i], file_order[i-2], abundance))


        
    ax2.set_title("Titan CO Difference Modified Ratios")
    ax2.set_xlabel("Wavelength (µm)")
    ax2.set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
    ax2.legend()
    ax2.set_xlim(4.5,5)
    ax2.set_aspect("auto")
    # ax2.set_aspect(75)
    fig2.tight_layout()
    # fig3.savefig("Figures/Titan_NIR_SR_CO_isotope_diff__CO1_CO2_CO3_Difference_Lin_2.png", dpi=300)
    
    df_iso_isotopes = df_iso_isotopes1 + df_iso_isotopes2

    return df_iso_isotopes



def Subtract_Isotopes(files=[], isotopes=[], abundance=[], file_order=[], R=15000, molecule='CO', Wrange=[4.5, 5]):
    xmin, xmax = Wrange[0], Wrange[1]
    df_isotopes = []

    fig1 = plt.figure()
    ax1 = fig1.subplots(1)

    for i, file_name in enumerate(files):
        df_isotopes.append(np.genfromtxt(file_name, comments="#", dtype=np.float64)) #, names=['Wavelength', 'Spectral Radiance','Noise', 'Titan']))

        ax1.plot(df_isotopes[0][:,0], df_isotopes[i][:,1], alpha=1, linewidth=1, 
                    label="{0} {1} at {2}scalar".format(molecule, file_order[i], abundance))


    ax1.set_title("{0} R={1}, isotopes:{2}, abundance:{3}".format(molecule, R, file_order, abundance))
    ax1.set_xlabel("Wavelength (µm)")
    ax1.set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
    ax1.legend()
    # ax1.set_aspect(100)
    ax1.set_xlim(xmin, xmax)
    fig1.tight_layout()
    # fig[0].savefig("Figures/Titan_NIR_SR__CO123_CO12_CO13_CO23_Lin_2.png", dpi=300)

    df_sub_isotopes = []
    fig3 = plt.figure()
    ax3 = fig3.subplots(1)
    for i in range(0, len(files)):
        df_sub_isotopes.append(df_isotopes[0][:,1] - df_isotopes[i][:,1])
        ax3.plot(df_isotopes[0][:,0], df_sub_isotopes[i])

    ax3.set_title("{0} R={1}, isotopes:{2}, abundance:{3}".format(molecule, R, file_order, abundance))
    ax3.set_xlabel("Wavelength (µm)")
    ax3.set_ylabel("Spectral Radiance  " + r'($\frac{W}{sr *m^2 *µm}$)')
    ax3.legend()
    # ax1.set_aspect(100)
    ax3.set_xlim(xmin, xmax)
    fig3.tight_layout()

    Iso_isotopes = Isolate_Isotopes(df_sub_isotopes, isotopes=isotopes, abundance=abundance, file_order=file_order)

    return df_isotopes, Iso_isotopes

        



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


Subtract_Isotopes(files=[CO123_file_name, CO12_file_name, CO13_file_name, CO23_file_name],
                isotopes=[123, 1, 2,3],
                abundance=[0.987, 0.011, 0.002],
                file_order=[123,12,13,23])


plt.show()