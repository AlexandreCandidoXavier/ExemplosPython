import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from scipy import stats
import seaborn as sns

"""
Arquivos necessários:
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

# definição da dadas para calculos
day_first, day_last = '1980-01-01', '2016-12-31'

# pegando Tmax e Tmin, v2.1 e calculando as msuas respectivas medias mensais
path = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/'
tmax = xr.open_mfdataset(path + 'Tmax_daily_UT_Brazil_v2.1*.nc').Tmax
tmax_yearly = tmax.sel(time=slice(day_first, day_last)).resample(time='Y').mean('time')

tmin = xr.open_mfdataset(path + 'Tmin_daily_UT_Brazil_v2.1*.nc').Tmin
tmin_yearly = tmin.sel(time=slice(day_first, day_last)).resample(time='Y').mean('time')

# Temperatura anual
temp_mean_yearly = (tmax_yearly+tmin_yearly) / 2

# figura regioes
fig, ax = plt.subplots(1)
temp_mean_yearly.isel(time=0).plot(ax=ax)

# definindo regioes
# sul, sudeste, nordeste, centro-oeste, norte
names_regions = ['sul', 'sudeste', 'nordeste', 'centro-oeste', 'norte']
names_regions_abre = ['S', 'SE', 'NE', 'CO', 'N',]
regiao_lat = [[-34, -22],
              [-25.6, -13.8],
              [-18.6, -1],
              [-24.3, -7],
              [-12.7, 6]]

regiao_lon = [[-58, -47.2],
              [-51.5, -39],
              [-49, -34.4],
              [-62, -45.6],
              [-74, -46.3]]

# calculation of the regions yearly Tmean
for n in range(5):
    print(names_regions[n])
    lat_min, lat_max = regiao_lat[n][0], regiao_lat[n][1]
    lon_min, lon_max = regiao_lon[n][0], regiao_lon[n][1]

    ax.plot([lon_min, lon_max, lon_max, lon_min, lon_min],
            [lat_min, lat_min, lat_max, lat_max, lat_min], label=names_regions[n])

    # creating a mask of the region
    mask = (lon_min < tmax_yearly.longitude) & (lon_max > tmax_yearly.longitude) & \
           (lat_min < tmax_yearly.latitude) &  (lat_max > tmax_yearly.latitude)
    # yearly mean
    temp_mean_yearly_region = temp_mean_yearly.where(mask).mean(['latitude', 'longitude']).values
    df_region = pd.DataFrame(np.c_[np.arange(37), temp_mean_yearly_region], columns=['year', 't_mean'])
    df_region['region'] = names_regions[n]
    if n == 0:
        df_all = df_region
    else:
        df_all = pd.concat([df_all, df_region])

ax.legend(loc=2, prop={'size': 6})
ax.set_xlim(-75,-34)
ax.set_ylim(-35,7)

# grafico simple linear regression
g = sns.lmplot(x='year', y="t_mean", hue="region", data=df_all, legend=False)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
       ncol=2, mode="expand", borderaxespad=0.)
plt.tight_layout()


# estatiticas
df_all['year_ano'] = df_all['year'] + 1980
df_all['datas'] = df_all.index.values
df_all['name_legend'] = ''
# estatisticas por regiao
stat_region = np.zeros((5,5))
for n in np.arange(5):
    x = df_all[df_all['region'] == names_regions[n]].year_ano.values
    y = df_all[df_all['region'] == names_regions[n]].t_mean.values
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    stat_region[n] = np.array([slope, intercept, r_value, p_value, std_err])
