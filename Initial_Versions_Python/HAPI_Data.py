from hapi import *
import numpy as np
import matplotlib.pyplot as plt
import pylab

db_begin('HAPI_Database')

# fetch('CO', 5, 1, 4e-4, 5e-4)
# nu,coef = absorptionCoefficient_Lorentz(SourceTables='CO', Component=())


fetch_by_ids('CO', [26,27,28], 3900, 4360) #, ParameterGroups=('160-char','SDVoigt') ) 
# fetch_by_ids('CO', 5, 2, 3900, 4360) #, ParameterGroups=('160-char','SDVoigt') ) 
# fetch_by_ids('CO', 5, 3, 3900, 4360) #, ParameterGroups=('160-char','SDVoigt') ) 
print("CO Fetched\n")
# print(select('CO', Conditions=('=', 'local_iso_id', 1)))

# select('CO', DestinationTableName='FilteredCO', ParameterNames=('nu', 'sw'), Conditions=('>', 'sw', 1.0e-25),File='co_linelist.out')
nu1,coef1 = absorptionCoefficient_Voigt(((5,1),), 'CO', Environment={'p':1.45, 'T':93})#,SourceTables=select('CO', Conditions=('=', 'local_iso_id', 1))) 
nu2,coef2 = absorptionCoefficient_Voigt(((5,2),), 'CO', Environment={'p':1.45, 'T':93}) 
nu3,coef3 = absorptionCoefficient_Voigt(((5,3),), 'CO', Environment={'p':1.45, 'T':93})

# print(coef1, coef2, coef3)

nu1_um = (1e4)/nu1
nu2_um = (1e4)/nu2
nu3_um = (1e4)/nu3

plt.plot(nu1_um, coef1)
plt.plot(nu2_um, coef2)
plt.plot(nu3_um, coef3)
plt.xlabel("Wavelength (µm)")
plt.ylabel("Absorbtion Coefficient")
plt.yscale("log")


# nu1,coef = absorptionCoefficient_Lorentz(SourceTables='CO',HITRAN_units=False) 
nu11, radi1 = radianceSpectrum(nu1,coef1, Environment={'l':100, 'T':93})
nu22,radi2 = radianceSpectrum(nu2,coef2, Environment={'l':100, 'T':93})
nu33,radi3 = radianceSpectrum(nu3,coef3, Environment={'l':100, 'T':93})

nu11_um = (1e4)/nu11
nu22_um = (1e4)/nu22
nu33_um = (1e4)/nu33

print(radi1, radi2, radi3)

# plt.plot(nu11_um, radi1)
# plt.plot(nu22_um, radi2)
# plt.plot(nu33_um, radi3)
plt.show() 
