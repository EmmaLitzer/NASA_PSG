from telnetlib import DO
import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash, dcc, html, Input, Output

R = str(15000)
Double_File = True

PSG_Directory = "/Users/elitzer/Desktop/PSG/NASA_PSG-main/Docker/"
# atm_1ppb_failed = PSG_Directory + '1ppb_atmosphere/try/'
Atmosphere = PSG_Directory + 'Fails/' + '1ppb_atm/' #Atmosphere/'
Lakes = PSG_Directory + 'Lakes/'
Ices = PSG_Directory + 'Ices/'

Full_File1 = PSG_Directory + 'Base_Titan_Atmosphere_SR1' + '.txt'
Full_File2 = PSG_Directory + 'Base_Titan_Atmosphere_SR2' + '.txt'
Full_File = PSG_Directory + 'Base_Titan_Atmosphere_SR' + '.txt'

def Load_Spec(file, data_type):
    # print(file[-:-4])
    (Data_array) = np.genfromtxt(file, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
    Data_array = np.array(Data_array)
    Data_array = Data_array[data_type]
    return Data_array

# Titan_Full = np.genfromtxt(Full_File, comments="#", dtype=np.float64, names=['Wavelength', 'Spectral_Radiance','Noise', 'Titan'])
if Double_File == True:
    Wavelength1 = Load_Spec(Full_File1, 'Wavelength')
    Wavelength2 = Load_Spec(Full_File2, 'Wavelength')
    Wavelength = np.concatenate((Wavelength1, Wavelength2))
    
    Titan_SR1 = Load_Spec(Full_File1, 'Spectral_Radiance')
    Titan_SR2 = Load_Spec(Full_File2, 'Spectral_Radiance')
    Titan_SR = np.concatenate((Titan_SR1, Titan_SR2))
else:
    Wavelength = Load_Spec(Full_File, 'Wavelength')
    Titan_SR=Load_Spec(Full_File, 'Spectral_Radiance')



def files_from_dir(dir_PATH, molecule_type, data_dict_diff, data_dict, Ratio, types):
    # Pull files from directory specified from dir_PATH and add molecule name to Ratio, 
    # Spectral radience data to data_dict and molecule type (atmosphere, surface, lakes, ices) to types
    files = sorted(glob.glob(dir_PATH  + '*.txt'))
    # print(files)
    for i, filename in enumerate(files):
        if Double_File==False:
            species = filename[len(dir_PATH):-5]
            Ratio.append(species)
            data1 = Load_Spec(filename, 'Spectral_Radiance')
            # data2 = Load_Spec(files[i+1], 'Spectral_Radiance')
            # data = np.concatenate((data1, data2))
            # data_dict_diff[species] = data - Titan_SR
            # data_dict[species] = data
            data1 = np.array(data1)
            data_dict_diff.append(data1 - Titan_SR)
            data_dict.append(data1)

            types[species] = molecule_type

        elif ((i % 2) ==0) & (i !=len(files)): #if i odd:
            species = filename[len(dir_PATH):-5]
            Ratio.append(species)
            data1 = Load_Spec(filename, 'Spectral_Radiance')
            data2 = Load_Spec(files[i+1], 'Spectral_Radiance')
            data = np.concatenate((data1, data2))
            # data_dict_diff[species] = data - Titan_SR
            # data_dict[species] = data
            data_dict_diff.append(np.absolute(data - Titan_SR))
            data_dict.append(data)

            types[species] = molecule_type

    return data_dict_diff, data_dict, Ratio, types #, data

# Initiallize empty dicts and lists to be filled when loading in data
Ratio = []
data_dict_diff = [] #{}
data_dict = [] #{}
types = {}

# Load in files from directories. Identify where the molecule is on Titan
# data_dict_diff, data_dict, Ratio, types = files_from_dir(Atmosphere, 'Atmosphere', data_dict_diff, data_dict, Ratio, types)
# data_dict_diff, data_dict, Ratio, types = files_from_dir(atm_1ppb_failed, 'Surface', data_dict_diff, data_dict, Ratio, types)
data_dict_diff, data_dict, Ratio, types = files_from_dir(Lakes, 'Lakes', data_dict_diff, data_dict, Ratio, types)
# data_dict_diff, data_dict, Ratio, types = files_from_dir(Ices, 'Ice', data_dict_diff, data_dict, Ratio, types)

Ratio = np.array(Ratio)

"""
fig = plt.figure(dpi=300) #, figsize=(10, 2))
N = len(data_dict) + 1
colors = plt.cm.jet(np.linspace(0,1,N))

for i, Isotope in enumerate(data_dict):
    r = Ratio[i]
    plt.plot(Wavelength, data_dict[i], label=( r), color=colors[i+1], linewidth=.75, alpha=1)
# plt.plot(Wavelength, Titan_SR, label='Titan SR', color=colors[1], linewidth=.75, alpha=1)


plt.title("Base Titan Configuration Spectral Radiance")
plt.ylabel("Spectral Radiance"+ r' ($\frac{W}{sr *m^2 *µm}$)') 
plt.xlabel("Wavelength" + ' (µm)')
plt.yscale('log')
plt.xlim(4.5,5)
plt.ylim(1e-3,5e-3)
plt.legend()

plt.tight_layout()
# fig.savefig("Figures/" + 'Lakes_Log' + ".png", dpi=300)
plt.show()
"""
# Create dash app with interactive plot of data
app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
    html.H4('Molecules on Titan: A Comparison with a Standard Titan Atmosphere'),
    dcc.Graph(id='Diff'),
    dcc.Graph(id='Full'),
    dcc.Interval(
        id='interval-component',
        interval=15000,
    ),
    dcc.Checklist(
        id='checklist',
        options=['Atmosphere','Surface', 'Lakes', 'Ice'],
        value=['Atmosphere','Surface', 'Lakes', 'Ice'],
        inline=True
    )]),

])

@app.callback(
    Output("Diff", "figure"),
    Input('checklist', 'value')
)

def update_line_chart1(pick_type):
    np_mask = np.isin(list(types.values()), pick_type)
    data_array_diff = np.array(data_dict_diff)

    # data_array_diff = np.array(list(data_dict_diff.values()), dtype=object)
    data_array_diff = data_array_diff[np_mask]

    # print(data_array_diff.shape)
    df_diff = pd.DataFrame(data_array_diff.T, index=Wavelength, columns=Ratio[np_mask])


    # fig1 = px.line(data_array_diff, x = Wavelength, y=data_array_diff, title='Titan Molecule Spectra Comparison with Basic Titan Model', log_y=False)
    fig1 = px.line(df_diff, title='Titan Molecule Spectra Comparison with Basic Titan Model', log_y=True, labels=dict(index=('Wavelength (µm)'), value=("Spectral Radiance W/(sr*m^2*µm)"), variable='Molecule'))
    # for i, newname in enumerate(Ratio[np_mask]):
    #     fig1.data[i].name = newname
    return fig1#.write_html("SR_dif.html")

@app.callback(
    Output("Full", "figure"),
    Input('checklist', 'value')
)

def update_line_chart2(pick_type):
    np_mask = np.isin(list(types.values()), pick_type)
    data_array = np.array(data_dict)

    # data_array = np.array(list(data_dict.values()), dtype=object)
    data_array = data_array[np_mask]

    # print(np_mask)
    # Wavelength_rep= np.tile(Wavelength, (12, 1))
    # print("wav",Wavelength_rep.shape, np_mask)

    # for i in range(0, len(np_mask)):
    df = pd.DataFrame(data_array.T, index=Wavelength, columns=Ratio[np_mask])
    # fig2 = px.line(data_array, x = Wavelength, y=data_array, title='Titan Molecule Spectral Radience', log_y=False)
    fig2 = px.line(df, title='Titan Molecule Spectral Radience', log_y=False, labels=dict(index=('Wavelength (µm)'), value=("Spectral Radiance W/(sr*m^2*µm)"), variable='Molecule'))
    # for i, newname in enumerate(Ratio[np_mask]):
    #     fig2.data[i].name = newname
    return fig2#.write_html("SR.html")

app.run_server(debug=True)

# """