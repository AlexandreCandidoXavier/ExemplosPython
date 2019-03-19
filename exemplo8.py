import xarray as xr
import matplotlib.pyplot as plt
"""
Abrindo e plotando a normal da temperatura media do mês janeiro, período 1981-01-01-2009-12-31, 
utilizando as grade Tmax e Tmin, v2.1, resolução 0,1 graus. Arquivos necessários:
Tmax_daily_UT_Brazil_v2.1_19800101_19891231.nc
Tmax_daily_UT_Brazil_v2.1_19900101_19991231.nc
Tmax_daily_UT_Brazil_v2.1_20000101_20061231.nc
Tmax_daily_UT_Brazil_v2.1_20070101_20131231.nc
Tmax_daily_UT_Brazil_v2.1_20140101_20170731.nc
Tmin_daily_UT_Brazil_v2.1_19800101_19891231.nc
Tmin_daily_UT_Brazil_v2.1_19900101_19991231.nc
Tmin_daily_UT_Brazil_v2.1_20000101_20061231.nc
Tmin_daily_UT_Brazil_v2.1_20070101_20131231.nc
Tmin_daily_UT_Brazil_v2.1_20140101_20170731.nc
"""

#definição da dadas para calculo das normais
day_first, day_last = '1981-01-01', '2009-12-31'

# pegando Tmax e Tmin, v2.1 e calculando as msuas respectivas medias mensais
path = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/'
tmax = xr.open_mfdataset(path + 'Tmax_daily_UT_Brazil_v2.1*.nc').Tmax
tmax_month = tmax.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

tmin = xr.open_mfdataset(path + 'Tmin_daily_UT_Brazil_v2.1*.nc').Tmin
tmin_month = tmin.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

# plotando normal, mes de Janeiro
month = 1 # janeiro
((tmax_month.sel(month=month)+tmin_month.sel(month=month)) / 2).plot(cmap=plt.cm.jet)
