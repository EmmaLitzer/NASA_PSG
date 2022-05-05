import requests
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
import glob

import plotly.express as px
from dash import Dash, dcc, html, Input, Output

R = str(15000)
xls_name = 'Atmosphere_components_1ppb'


PSG_Directory = "https://github.com/EmmaLitzer/NASA_PSG/tree/main/Docker" # "/Users/elitzer/Desktop/PSG/NASA_PSG-main/Docker/"
atm_1ppb_failed = PSG_Directory + '1ppb_atmosphere/try/'
atm_1ppb = PSG_Directory + '1ppb_atmosphere/'
Lakes = PSG_Directory + 'Lakes/'
Ices = PSG_Directory + 'Ices/'

Full_File = PSG_Directory + 'Base_Titan_Atmosphere_SR' + '.txt'

Fig_Titles = ['Atmosphere_components_1ppb_noNitriles22', 'Atmosphere_components_1ppb_Difference_noNitriles22']
Pic_Titles = ['Titan PSG Simulation for Different Atmospheric \n components at R' + R,
              'Titan PSG Simulation Difference between Atmospheric \n Components and Standard Titan Atmosphere at R' + R]

def Load_Spec(file):
    # print(file[-:-4])
    (Data_array) = np.genfromtxt(file, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
    return Data_array

Titan_Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

def files_from_dir(dir_PATH, molecule_type, data_dict, Ratio, types):
    # Pull files from directory specified from dir_PATH and add molecule name to Ratio, 
    # Spectral radience data to data_dict and molecule type (atmosphere, surface, lakes, ices) to types
    files = sorted(glob.glob(dir_PATH  + '*.txt'))

    for i, filename in enumerate(files):
        species = filename[len(dir_PATH):-4]
        Ratio.append(species)
        data = Load_Spec(filename)
        data_dict[species] = np.array(data['Spectral_Radiance']) - Titan_Full['Spectral_Radiance']
        types[species] = molecule_type
    
    return data_dict, Ratio, types #, data

# Initiallize empty dicts and lists to be filled when loading in data
Ratio = []
data_dict = {}
types = {}

# Load in files from directories. Identify where the molecule is on Titan
data_dict, Ratio, types = files_from_dir(atm_1ppb, 'Atmosphere', data_dict, Ratio, types)
data_dict, Ratio, types = files_from_dir(atm_1ppb_failed, 'Surface', data_dict, Ratio, types)
data_dict, Ratio, types = files_from_dir(Lakes, 'Lakes', data_dict, Ratio, types)
data_dict, Ratio, types = files_from_dir(Ices, 'Ice', data_dict, Ratio, types)

# Initialize Wavelength refrence array
data_dict['Wavelength'] = [Titan_Full['Wavelength']]
types['Wavelength'] = 'None'
Ratio.append('None')


#"""
# Create dash app with interactive plot of data
app = Dash(__name__)

app.layout = html.Div([
    html.H4('Molecules on Titan: A Comparison with a Standard Titan Atmosphere'),
    dcc.Graph(id='Graph'),
    dcc.Checklist(
        id='checklist',
        options=['Atmosphere','Surface', 'Lakes', 'Ice'],
        value=['Atmosphere'],
        inline=True
    )
])

@app.callback(
    Output("Graph", "figure"),
    Input('checklist', 'value')
)
#"""
def update_line_chart(pick_type):
    np_mask = np.isin(list(types.values()), pick_type)
    data_array = np.array(list(data_dict.values()))
    data_array = data_array[np_mask]

    fig = px.line(data_array, 
        x = data_dict['Wavelength'][0], y=data_array, title='Molecule Spectral Radience Differance from Standard Titan Atmosphere', log_y=True)
    for i, newname in enumerate(np.array(Ratio)[np_mask]):
        fig.data[i].name = newname
    return fig.write_html("docs/SR.html")


if __name__ == "__main__":
	app.run_server(debug=False)

# """
