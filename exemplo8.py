import xarray as xr
import matplotlib.pyplot as plt
"""
Abrindo e plotando a normal da temperatura media do mês janeiro, período 1981-01-01-2009-12-31, 
utilizando as grade Tmax e Tmin, v2.1, resolução 0,1 graus. Arquivos necessários:


"""

#definição da dadas para calculo das normais
day_first, day_last = '1981-01-01', '2009-12-31'

# pegando "Tmax v2.1" para o dia e latitude em questao
path = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/'
tmax = xr.open_mfdataset(path + 'Tmax_daily_UT_Brazil_v2.1*.nc').Tmax
tmax_month = tmax.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

tmin = xr.open_mfdataset(path + 'Tmin_daily_UT_Brazil_v2.1*.nc').Tmin
tmin_month = tmin.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

# plotando normal, mes de Janeiro
month = 1 # janeiro
((tmax_month.sel(month=month)+tmin_month.sel(month=month)) / 2).plot(cmap=plt.cm.jet)
