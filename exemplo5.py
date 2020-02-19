import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Plotando e exportando em "csv" dados medios mensais de Tmax para 
algumas localidades (medias do periodo 01/01/1980 a 31/07/2017)

Arquivos:
Tmax_daily_UT_Brazil_v2.1_19800101_19891231.nc
Tmax_daily_UT_Brazil_v2.1_19900101_19991231.nc
Tmax_daily_UT_Brazil_v2.1_20000101_20061231.nc
Tmax_daily_UT_Brazil_v2.1_20070101_20131231.nc
Tmax_daily_UT_Brazil_v2.1_20140101_20170731.nc
"""

# pegando variavel
path_var = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/'
var = xr.open_mfdataset(path_var + 'Tmax_daily_UT_Brazil_v2.1*.nc', combine='by_coords')['Tmax']

# Nome dos pontos
Names = ['INPE-SP', 'UFCG-PB', 'UFC-CE']
lat_lon = [[-23.2, -45.9],
           [-7.2, -35.9],
           [-3.85, -38.6],]
varMonthly2Export = pd.DataFrame(np.empty((12, len(Names))),
                                 columns=Names,
                                 index=range(1, 13))
# media mensal
for n, names in enumerate(Names):
    tmaxCityDaily = var.sel(latitude=lat_lon[n][0],
                            longitude=lat_lon[n][1],
                            method='nearest')
    tmaxCityMonthly = tmaxCityDaily.groupby('time.month').mean('time')
    # ploting
    tmaxCityMonthly.plot(label=names)
    # concatenating in pandas
    varMonthly2Export[names] = tmaxCityMonthly

plt.ylim(22, 33)
plt.title('')
plt.legend()
plt.show(block=False)

# exporting
varMonthly2Export.to_csv('dadosMensais.csv')
