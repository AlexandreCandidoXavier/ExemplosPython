import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

""" Extraindo para uma posicao (Umuarama-PR) a serie historica diaria 
da temperatura maxima (Tmax), calculando a sua media 
mensal (01/1980-12/2010) e exportando dados diarios em arquivo cvs:

Tmax_daily_UT_Brazil_v2_19800101_19891231.nc
Tmax_daily_UT_Brazil_v2_19900101_19991231.nc
Tmax_daily_UT_Brazil_v2_20000101_20061231.nc
Tmax_daily_UT_Brazil_v2_20070101_20131231.nc
Tmax_daily_UT_Brazil_v2_20140101_20170731_s1.nc
"""

# versoes
print(xr.__version__) # 0.14.1
print(np.__version__) # 1.16.4

# set correct path of the variables
path_var = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/'
ds = xr.open_mfdataset(path_var + 'Tmax_daily_UT_Brazil_v2*.nc', combine='by_coords')

# pegando a variavel Tmax entre 01/01/1980 a 31/12/2010
Tmax_data = ds.Tmax.sel(time=slice('1980-01-01','2010-12-31'))

# pegando os dados para o posicao de Umuarama/Parana
Tmax_data_temporal = Tmax_data.sel(latitude=-23.76,longitude=-53.30,
                                   method='nearest')
# plotando dados diarios
_, (ax1, ax2) = plt.subplots(1, 2)
Tmax_data_temporal.plot(ax=ax1)

# plotando a media mensal
Tmax_mean_month = Tmax_data_temporal.groupby('time.month').mean('time')
Tmax_mean_month.plot(ax=ax2)
plt.show()

# exportando dados diarios em cvs: nome do arquivo 'Tmax.cvs'
fileName = 'Tmax.csv'
days = np.array(Tmax_data_temporal.time)
data_dataframe = pd.Series(np.array(Tmax_data_temporal), index=days)
data_dataframe.to_csv(fileName)
