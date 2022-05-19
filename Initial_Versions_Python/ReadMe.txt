# NASA_PSG

Conduct atmospheric and surface comparisons of planet and planet-like objects. 

Generate plots of the spectral radiance of the object (surface, atmosphere, and scattering aerosols) and their difference with a standard object spectral radiance. An excel file with wavelength and SR values for each component can be genrated and saved to local directory. 


To use this PSG data analyser:

* Configure a planet or planet-like object, instrument parameters, and viewing geometry in the Planetary Spectrum Generator (PSG) located at https://psg.gsfc.nasa.gov/index.php. I recommend downloading the object config file for easy loading later. 
* Generate spectra from PSG and download the resulting spectra text file. Rename the spectra file in downloads folder.
* To see the effects of one variable, change the variable in PSG and re-run as many times as needed
* Move all genrated files to a folder
* Load in all files (named appropriately) into Component_Difference.py by changing the PATH variables (PSG_Directory: directory where all PSG directories are saved, Surface_Directory: directory where desired files are, and Full_File: the basic file to compare to).
* Run the python file Component_Difference.py

To run PSG locally:
* Install docker and follow steps at https://psg.gsfc.nasa.gov/helpapi.php#installation
* Download desired packages (PROGRAMS, BASE, SURFACES, ATMOSPHERES)
* K-tables are nice and will speed up PSG but take up >250Gb  of drive space
* In a browser, open PSG (https://psg.gsfc.nasa.gov/index.php) and configure object atmosphere, surface, and aerosol composition
* In the terminal or cmd prompt go to desired directory and save config file as psg_cfg.txt
* curl --data-urlencode file@psg_cfg.txt http://localhost:3000/api.php > Save_Directory/XX_File_Name.txt
