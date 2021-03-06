import numpy as np
import glob

import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output

R = str(15000)
xls_name = 'Atmosphere_components_1ppb'


PSG_Directory = "/Users/elitzer/Desktop/PSG/NASA_PSG-main/Docker/"
# atm_1ppb_failed = PSG_Directory + '1ppb_atmosphere/try/'
Atmosphere = PSG_Directory + 'Atmosphere/'
Lakes = PSG_Directory + 'Lakes/'
Ices = PSG_Directory + 'Ices/'

Full_File = PSG_Directory + 'Base_Titan_Atmosphere_SR' + '.txt'

# Fig_Titles = ['Atmosphere_components_1ppb_noNitriles22', 'Atmosphere_components_1ppb_Difference_noNitriles22']
# Pic_Titles = ['Titan PSG Simulation for Different Atmospheric \n components at R' + R,
#               'Titan PSG Simulation Difference between Atmospheric \n Components and Standard Titan Atmosphere at R' + R]

def Load_Spec(file):
    # print(file[-:-4])
    (Data_array) = np.genfromtxt(file, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
    return Data_array

Titan_Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])

def files_from_dir(dir_PATH, molecule_type, data_dict_diff, data_dict, Ratio, types):
    # Pull files from directory specified from dir_PATH and add molecule name to Ratio, 
    # Spectral radience data to data_dict and molecule type (atmosphere, surface, lakes, ices) to types
    files = sorted(glob.glob(dir_PATH  + '*.txt'))

    for i, filename in enumerate(files):
        species = filename[len(dir_PATH):-4]
        Ratio.append(species)
        data = Load_Spec(filename)
        data_dict_diff[species] = np.array(data['Spectral_Radiance']) - Titan_Full['Spectral_Radiance']
        data_dict[species] = np.array(data['Spectral_Radiance'])

        types[species] = molecule_type
    
    return data_dict_diff, data_dict, Ratio, types #, data

# Initiallize empty dicts and lists to be filled when loading in data
Ratio = []
data_dict_diff = {}
data_dict = {}
types = {}

# Load in files from directories. Identify where the molecule is on Titan
data_dict_diff, data_dict, Ratio, types = files_from_dir(Atmosphere, 'Atmosphere', data_dict_diff, data_dict, Ratio, types)
# data_dict_diff, data_dict, Ratio, types = files_from_dir(atm_1ppb_failed, 'Surface', data_dict_diff, data_dict, Ratio, types)
data_dict_diff, data_dict, Ratio, types = files_from_dir(Lakes, 'Lakes', data_dict_diff, data_dict, Ratio, types)
data_dict_diff, data_dict, Ratio, types = files_from_dir(Ices, 'Ice', data_dict_diff, data_dict, Ratio, types)

# Initialize Wavelength refrence array
data_dict_diff['Wavelength'] = [Titan_Full['Wavelength']]
data_dict['Wavelength'] = [Titan_Full['Wavelength']]
types['Wavelength'] = 'None'
Ratio.append('None')
Ratio = np.array(Ratio)
# a = np.arange(len(data_dict['Wavelength']))
# Ratio_names = np.tile(a, Ratio)
# Ratio_names = np.repeat(Ratio, len(data_dict['Wavelength']), axis=0)

# """
# Create dash app with interactive plot of data
app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
    html.H4('Molecules on Titan: A Comparison with a Standard Titan Atmosphere'),
    dcc.Graph(id='Diff'),
    dcc.Graph(id='Full'),
    dcc.Checklist(
        id='checklist',
        options=['Atmosphere','Surface', 'Lakes', 'Ice'],
        value=['Atmosphere'],
        inline=True
    )]),

])

@app.callback(
    Output("Diff", "figure"),
    Input('checklist', 'value')
)

def update_line_chart1(pick_type):
    np_mask = np.isin(list(types.values()), pick_type)
    data_array_diff = np.array(list(data_dict_diff.values()), dtype=object)
    data_array_diff = data_array_diff[np_mask]
    # data_array = np.array(list(data_dict.values()))
    # data_array = data_array[np_mask]

    fig1 = px.line(data_array_diff, x = data_dict_diff['Wavelength'][0], y=data_array_diff, title='Molecule Spectral Radience Differance from Standard Titan Atmosphere', log_y=True)
    # fig2 = px.line(data_array, x = data_dict['Wavelength'][0], y=data_array, title='Molecule Spectral Radience Differance from Standard Titan Atmosphere', log_y=True)
    for i, newname in enumerate(Ratio[np_mask]):
        fig1.data[i].name = newname
        # fig2.data[i].name = newname
    return fig1 # .write_html("SR.html")

@app.callback(
    Output("Full", "figure"),
    Input('checklist', 'value')
)

def update_line_chart2(pick_type):
    np_mask = np.isin(list(types.values()), pick_type)
    # data_array_diff = np.array(list(data_dict_diff.values()))
    # data_array_diff = data_array_diff[np_mask]
    data_array = np.array(list(data_dict.values()), dtype=object)
    data_array = data_array[np_mask]

    # fig1 = px.line(data_array_diff, x = data_dict_diff['Wavelength'][0], y=data_array_diff, title='Molecule Spectral Radience Differance from Standard Titan Atmosphere', log_y=True)
    fig2 = px.line(data_array, x = data_dict['Wavelength'][0], y=data_array, title='Molecule Spectral Radience Differance from Standard Titan Atmosphere', log_y=False)
    for i, newname in enumerate(Ratio[np_mask]):
        # fig1.data[i].name = newname
        fig2.data[i].name = newname
    return fig2 # .write_html("SR.html")

app.run_server(debug=False)

# """