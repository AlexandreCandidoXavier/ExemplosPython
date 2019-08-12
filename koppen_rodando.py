import xarray as xr
import numpy as np
import matplotlib.pylab as plt
import scipy.interpolate
import cartopy.crs as ccrs
from cartopy.feature import NaturalEarthFeature
import matplotlib.patches as mpatches
import koppen

# EXEMPLO 1
# Testando para uma localidade, neste exemplo, cidade de Verdelandia na Bahia.
# precipitacao media mensal
prec = np.array([140.1, 87.3, 115.9, 35.7, 5.6,  1.7, 0.6, 1.8, 10.8, 53.7, 142.9, 189.7])
# temperatura media mensal
avgtemp = np.array([25.5, 25.9, 25.76, 25.1, 23.7, 22.2, 21.9, 23.0, 25.0, 26.3, 25.6, 25.3])
# latitude. So´ serve para a definicao dos hemisferios
lat = -15.5
# Definindo o clima
clima_localidade = koppen.koppen_classification(prec, avgtemp, lat)
print(clima_localidade)  # Cfa
# plotando os dados de precipitacao e temperatura
fig, ax1 = plt.subplots()
ax1.plot(prec)
ax1.set_ylabel('Precipitação mensal [mm]', color='b')
ax1.tick_params('y', colors='b')
ax2 = ax1.twinx()
ax2.plot(avgtemp, 'r')
ax2.set_ylabel('Temperatura média', color='r')
ax2.tick_params('y', colors='r')
fig.suptitle(clima_localidade)


# EXEMPLO 2
# Com base nos dados gradeados, gerando o clima segundo Koppen para o Brasil
# com definição das dadas para calculos das normais de 30 anos
day_first, day_last = '1981-01-01', '2009-12-31'

# caminho dos dados gradeados
path = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/'

# pegando Tmax e Tmin, v2.1 e calculando as msuas respectivas medias mensais
tmax = xr.open_mfdataset(path + 'Tmax_daily_UT_Brazil_v2.1*.nc', combine='nested', concat_dim='time').Tmax
tmax_month = tmax.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

tmin = xr.open_mfdataset(path + 'Tmin_daily_UT_Brazil_v2.1*.nc', combine='nested', concat_dim='time').Tmin
tmin_month = tmin.sel(time=slice(day_first, day_last)).groupby('time.month').mean('time')

# para ser reescalonar a reolucao espacial dos dados de precipitacao para as dos dados de temperatura
lon_grid, lat_grid = np.meshgrid(tmin.longitude.values, tmin.latitude.values)

# pegando dados de precipitacao
prec = xr.open_mfdataset(path + 'prec_daily_UT_Brazil_v*.nc', combine='nested', concat_dim='time').prec
mascara_prec = prec.isel(time=0).isnull().values
lon_prec, lat_prec = np.meshgrid(prec.longitude.values, prec.latitude.values)
prec = prec.sel(time=slice(day_first, day_last)).groupby('time.month').sum('time').values / 30  # media mensal de 30 anos

# temperatura media mensal em numpy.ndarray
Tmean = ((tmax_month + tmin_month) / 2).values

# reescalonando dados de precipitacao para mesma resolucao espacial da temperatura
prec_reescal = np.empty_like(Tmean)
for mes in range(12):
    prec_month = prec[mes]
    prec_month[mascara_prec] = np.nan
    prec_reescal[mes] = scipy.interpolate.griddata((lon_prec.flatten(), lat_prec.flatten()), prec_month.flatten(),
                                                   (lon_grid, lat_grid), method='nearest')

# criando variavel string para classes de clima em cada celula
climate = np.empty((Tmean.shape[1], Tmean.shape[2]), dtype='|U16')

# classificacao Koppen para cada celula da grade
for row in range(Tmean.shape[1]):
    for col in range(Tmean.shape[2]):
        prec_cell = prec_reescal[:, row, col]
        Tmean_cell = Tmean[:, row, col]
        if ~np.isnan(prec_cell).any() and ~np.isnan(Tmean_cell).any():
            climate[row, col] = koppen.koppen_classification(prec_cell, Tmean_cell, lat_grid[row, col])

# indexando os dados "climate" para serem plotados
climate_color = np.empty((Tmean.shape[1], Tmean.shape[2]), dtype=np.float)
climas = []
for n, clima in enumerate(np.unique(climate).tolist()):
    if n == 0:
        climate_color[climate == clima] = np.nan
    else:
        climate_color[climate == clima] = n
        climas.append(clima)

# definindo cores
color = ['darkblue', 'royalblue', 'cornflowerblue','lightblue', 'orange',
         'greenyellow', 'seagreen', 'darkseagreen', 'yellowgreen']
cmap = plt.mpl.colors.ListedColormap(color)

# para plotar estados
states = NaturalEarthFeature(category='cultural', scale='50m',
                             facecolor='none',
                             name='admin_1_states_provinces_shp')

# plotando o mapa do clima segundo Koppen
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
im = ax.pcolormesh(lon_grid, lat_grid, climate_color, cmap=cmap)
ax.add_feature(states, edgecolor='gray', facecolor='none')
ax.set_extent([-75, -34, -34, 6])
ax.legend(handles=[mpatches.Patch(color=color[n], label=climas[n]) for n in range(len(climas))],
          handlelength=0.7, bbox_to_anchor=(1.05, 0.4), loc='lower left', borderaxespad=0.)
plt.tight_layout()
plt.show()
