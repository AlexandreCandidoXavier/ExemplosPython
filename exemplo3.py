import xarray as xr                 # versao '0.9.6'
import matplotlib.pyplot as plt
# versao '2.0.2'
"""Plotando media mensal da Umidade Relativa (01/01/2006-31/12/2016) 
para todo Brasil. Arquivos necessarios:

RH_daily_UT_Brazil_v2_19800101_19891231.nc
RH_daily_UT_Brazil_v2_19900101_19991231.nc
RH_daily_UT_Brazil_v2_20000101_20061231.nc
RH_daily_UT_Brazil_v2_20070101_20131231.nc
RH_daily_UT_Brazil_v2_20140101_20170731_s1.nc"""

# pegando variavel
path_var = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/'
ds = xr.open_mfdataset(path_var + 'RH_daily_UT_Brazil_v2*1.nc')

# pegando a variavel RH entre 01/01/2006-31/12/2016
RH_data = ds.RH.sel(time=slice('2006-01-01', '2016-12-31'))

# agrupando em media mensal
RH_mean_month = RH_data.groupby('time.month').mean('time')

# plotando
RH_mean_month.plot(x='longitude', y='latitude', col='month',
                   cmap='RdBu', col_wrap=4)
plt.show()
