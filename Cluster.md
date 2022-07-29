# How to use the Illinois Campus Cluster
##### Python Edition

## Logging on to the cluster
- Download Bitvise SSH Client (off of Google) and Cisco AnyConnect (off of the UIUC Webstore)
- Connect to the vpn.illinois.edu VPN and enter your username and password
- Open Bitvise SSH and log in using your UIUC credentials
  - Connect to cc-login.campuscluster.illinois.edu port 22
- Open the cluster terminal using the "New terminal console" icon or transfer files to the cluster directory using the "New SFTP window" icon
- In the terminal, you should see the available space in your directory and available space in your section of the scratch directory

## Initializing a python environment
- This works similarly to setting up an enviroment on your personal computer but without a GUI
- CAPS comes with anaconda installed but I have had issues with it. I install miniconda instead and add my own packages.
- Installing miniconda:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
conda --version
conda create -n fsps-test -c conda-forge python=3.9 numpy

conda activate env_name
python -m pip install fsps
python -c "import fsps; sp = fsps.StellarPopulation(); print(sp.libraries)"


conda activate env_name

pip install astro-sedpy
pip install astro-prosepctor
conda install astropy
conda install h5py
pip install matplotlib
pip install seaborn

pip install astroquery
pip install emcee
```
