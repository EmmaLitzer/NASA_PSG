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
# import plotly.graph_objects as go

# pd.options.plotting.backend = "plotly"

R = str(15000)
xls_name = 'Atmosphere_components_1ppb'


PSG_Directory = "/Users/elitzer/Desktop/PSG/NASA_PSG-main/Docker/"
Surface_Directory = PSG_Directory + '1ppb_atmosphere/try/'
Full_File = PSG_Directory + 'Base_Titan_Atmosphere_SR' + '.txt'

Fig_Titles = ['Atmosphere_components_1ppb_noNitriles22', 'Atmosphere_components_1ppb_Difference_noNitriles22']
Pic_Titles = ['Titan PSG Simulation for Different Atmospheric \n components at R' + R,
              'Titan PSG Simulation Difference between Atmospheric \n Components and Standard Titan Atmosphere at R' + R]

files = sorted(glob.glob(Surface_Directory  + '*.txt'))

Ratio = []
Data_array_atmosphere = []

data_dict = {}
types = {}

min_max= [.85, 1.15, .05]

def Load_Spec(file):
    # Data_File = file + '.txt'
    # print(file[-:-4])
    (Data_array) = np.genfromtxt(file, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
    # Data_array = np.asarray(Data_array)
    return Data_array


for i, filename in enumerate(files):
    species = filename[len(Surface_Directory):-4]
    Ratio.append(species)
    data = Load_Spec(filename)
    data_dict[species] = [np.array(data['Spectral_Radiance'])] #'Atmosphere'
    # print(data["Spectral_Radiance"])
    Data_array_atmosphere.append(np.array(data))

    types[species] = 'Atmosphere'

data_dict['Wavelength'] = [data['Wavelength']]
# print(data_dict)

data_dict2 = {}
print(data['Wavelength'])
data_dict2['Wavelength'] = data['Wavelength']
Data_array_atmosphere = np.array(Data_array_atmosphere)
# print(Ratio)
# print(Data_array.shape)
# print(Data_array)


df = pd.DataFrame(data_dict) #, index=data['Wavelength'])
# df = df #.T
df.loc[len(df.index)] = types #np.chararray(len(Data_array_atmosphere) + 1, itemsize=len('Atmosphere'))
# print(df.loc[0][i])
# print(len(Ratio))
# print(df.loc[0])

Species = 'xyz'

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Titan molecule atmosphere'),
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

def update_line_chart(types):
    fig = px.line(df, #[mask],
        x = df['Wavelength'][0], y=df.loc[0][:-1], title='Molecule Spectral Radience', log_y=True)#Ratio)#, color='Specie')
    for i, newname in enumerate(Ratio):
        fig.data[i].name = newname
    # fig.show()
    return fig

app.run_server(debug=False)


# fig = go.Figure()
# for i in range(0, len(Ratio)):
#     fig.add_trace(go.Scatter(
#         x=df['Wavelength'],
#         y=df.loc[0][i],
#         name=Ratio[i]
#     ))
# print('done', i)
# fig.show()






# Titan_Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])



# fig = plt.figure(dpi=300) #, figsize=(10, 2))
# N = len(Data_array) + 1
# colors = plt.cm.jet(np.linspace(0,1,N))

# for i, Isotope in enumerate(Data_array):
#     r = Ratio[i]
#     plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'], label=( r), color=colors[i+1], linewidth=.75, alpha=1)

# # plt.xlim(2.5,2.9)
# plt.title(Pic_Titles[0])
# plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
# plt.xlabel("Wavelength" + ' (µm)')
# plt.yscale('log')
# # plt.xlim(4.5,4.75)
# # plt.ylim(0,5e-4)

# plt.legend()


# ax = plt.gca() 

# # norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
# # sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
# # sm.set_array([])
# # divider = make_axes_locatable(ax)
# # cax = divider.append_axes("right", size="5%", pad=0.15)
# # cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

# plt.tight_layout()
# # fig.savefig("Figures/" + Fig_Titles[0] + ".png", dpi=300)






# fig = plt.figure(dpi=300) #, figsize=(10, 2))
# # N = len(Data_array) + 1
# # colors = plt.cm.jet(np.linspace(0,1,N))

# for i, Isotope in enumerate(Data_array):
#     r = Ratio[i]
#     plt.plot(Isotope['Wavelength'], Isotope['Spectral_Radiance'] - Titan_Full['Spectral_Radiance'], label=( r), color=colors[i+1], linewidth=.75, alpha=1)


# # plt.xlim(2.5,2.9)
# plt.title(Pic_Titles[1])
# plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
# plt.xlabel("Wavelength" + ' (µm)')
# # plt.yscale('log')
# # plt.xlim(4.5,4.75)
# # plt.ylim(0,5e-4)
# plt.legend()


# # ax = plt.gca() 

# # norm = mpl.colors.Normalize(vmin=min_max[0],vmax=min_max[1])
# # sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
# # sm.set_array([])
# # divider = make_axes_locatable(ax)
# # cax = divider.append_axes("right", size="5%", pad=0.15)
# # cbar = plt.colorbar(sm, ticks=np.arange(min_max[0],min_max[1],min_max[2]), cax=cax, label="H2O")

# plt.tight_layout()
# # fig.savefig("Figures/" + Fig_Titles[1] + ".png", dpi=300)


# plt.show()


# # Data_array = np.array(Data_array)


# # pddf = pd.DataFrame(data= Data_array['Spectral_Radiance'].T,
# #                         columns = [i for i in Ratio],
# #                         index = Titan_Full["Wavelength"])

# # with pd.ExcelWriter('Excel/' + xls_name + '.xlsx') as writer:
# #     pddf.to_excel(writer, sheet_name=xls_name+'_R'+R)

