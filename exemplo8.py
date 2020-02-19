import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature, BORDERS

""" Abrindo e plotando a normal da temperatura media do mês janeiro, período 1981-01-01-2009-12-31, 
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
path = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/'
tmax = xr.open_mfdataset(path + 'Tmax_daily_UT_Brazil_v2.1*.nc', combine='by_coords').Tmax
tmax_month = tmax.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

tmin = xr.open_mfdataset(path + 'Tmin_daily_UT_Brazil_v2.1*.nc', combine='by_coords').Tmin
tmin_month = tmin.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

# plotando normal, mes de Janeiro
month = 1 # 1=janeiro, 2=fevereiro, .... 12=dezembro
((tmax_month.sel(month=month)+tmin_month.sel(month=month)) / 2).plot(cmap=plt.cm.jet)

# plotando as medias para todos os meses
t_media = ((tmax_month + tmin_month) / 2)
p = t_media.plot(transform=ccrs.PlateCarree(), cmap=plt.cm.jet, col='month', col_wrap=4,
                                    subplot_kws={'projection': ccrs.PlateCarree()}, extend='both')

for ax in p.axes.flat:
    ax.coastlines()
    ax.add_feature(BORDERS)
    ax.set_extent([-75, -33, -33.5, 6])
