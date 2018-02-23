# -*- coding: utf-8 -*-

import xarray as xr # versao '0.9.6'
import matplotlib.pyplot as plt # versao '2.0.2'

# codigo original: testeFilesNetcdf
# lendo ETo
# em '~', colocar o caminho correto onde se encontram os arq 'ETo'
ds = xr.open_mfdataset('D:/Dropbox/netcdfgrid3/ETo_daily_UT_Brazil_v2*.nc')
var = ds['ETo']

# cidades e coordenadas
cityNames = ['Santa Maria-RS', 'Manaus-AM',
             'Petrolina-PE', 'Alegre-ES']
cityCoord = [[-29.7, -53.7],
             [-3., -60.],
             [-9.4, -40.5],
             [-20.7, -41.5]]
# calculando a media mensal
varMean = var.resample('M', 'time', how='mean')

# plotando
for n, city in enumerate(cityNames):
    varMean.sel(latitude=cityCoord[n][0], longitude=cityCoord[n][1],
                method='nearest').plot(label=city)

plt.title('')
plt.legend(ncol=2)
plt.show(block=False)



import xarray as xr # versao '0.9.6'
import matplotlib.pyplot as plt # versao '2.0.2'
import pandas as pd # versao '0.20.1'
import numpy as np # versao '1.12.1'

# codigo original: testeFilesNetcdf
# lendo Tmax
# em '~', colocar o caminho correto onde se encontram os arq 'Tmax'
ds = xr.open_mfdataset('D:/Dropbox/netcdfgrid3/Tmax_daily_UT_Brazil_v2*.nc')
var = ds['Tmax']

# Nome dos pontos
Names = ['INPE-SP', 'UFCG-PB', 'UFC-CE']
lat_lon = [[-23.2, -45.9],
             [-7.2, -35.9],
             [-3.8, -38.6],]
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

plt.title('')
plt.legend()
plt.show(block=False)

# exporting
varMonthly2Export.to_csv('dadosMensais.csv')


# controles
import xarray as xr # versao '0.9.6'
import matplotlib.pyplot as plt # versao '2.0.2'

# codigo original: testeFilesNetcdf
# lendo Tmax
# em '~', colocar o caminho correto onde se encontram os arq 'prec'
ds = xr.open_mfdataset('D:/Dropbox/netcdfgrid3/prec_daily_UT_Brazil_v2*control.nc')
dist_nearest = ds['dist_nearest']
count = ds['count']

# Nome dos pontos
Names = ['Sorriso-MT', 'Campinas-SP']
lat_lon = [[-12.5, -55.7],
           [-22.8, -47.0],]

# plotando distância do pluviômetro mais próximo, ao longo do tempo,
# que foi utilizado na interpolação
ax = plt.subplot(2, 1, 1)
for n, names in enumerate(Names):
    dist_nearest.sel(latitude=lat_lon[n][0],
                     longitude=lat_lon[n][1],
                     method='nearest').plot(label=names)
plt.legend()
plt.title('')


# plotando o número de pluviômetros existentes dentro das
# células que contêm os municípios
ax = plt.subplot(2, 1, 2)
for n, names in enumerate(Names):
    count.sel(latitude=lat_lon[n][0],
              longitude=lat_lon[n][1],
              method='nearest').plot(label=names)

plt.legend()
plt.title('')




plt.figure()
count = ds['count']
dist_nearest = ds['dist_nearest']
count.isel(time=-1).plot()

var_data_temporal = var.sel(latitude=-23.76, longitude=-53.30, method='nearest')
# Brasilaa
var.sel(latitude=-15.72, longitude=-48, method='nearest').plot()
# Umuarama
var.sel(latitude=-23.76, longitude=-53.30, method='nearest').plot()
varMean = var.groupby('time.month').mean('time')

varMean.plot(x='longitude', y='latitude', col='month',
                   cmap='RdBu', col_wrap=4)

cityNames = ['Santa Maria-RS', 'Manaus-AM', 'Campina Grande-PB', 'Alegre-ES']
cityCoord = [[-29.7, -53.7],
             [-3., -60.],
             [-7.2, -35.9],
             [-20.7, -41.5]]

# calculado a media menssal ('M')
varMean = var.resample('M', 'time', how='mean')

for n, city in enumerate(cityNames):
    varMean.sel(latitude=cityCoord[n][0], longitude=cityCoord[n][1], method='nearest').plot(label=city)

plt.title('')
plt.legend(ncol=2)
plt.show(block=False)


plt.figure()
# Todos os arquivos da variavel diários de Rs sao necessarios, ou seja,
# os de controle tambem
# substituir ~ pelo caminho correto
data = xr.open_mfdataset('D:/Dropbox/netcdfgrid3//Rs_daily_UT_Brazil_v2*1.nc')
data_control = xr.open_mfdataset('D:/Dropbox/netcdfgrid3//Rs_daily_UT_Brazil_v2*_Control.nc')
Rs = data['Rs']
Rs_count = data_control['count']
Rs_dist_nearest = data_control['dist_nearest']

# escolhendo o dia
day2get = '2014-01-01'
Rs2_one_day = Rs.sel(time=day2get)
Rs2_one_day_count = Rs_count.sel(time=day2get)
Rs2_one_dist_nearest = Rs_dist_nearest.sel(time=day2get)

# plotando
plt.subplot(131), Rs2_one_day.plot(), plt.axis('off')
plt.subplot(132), Rs2_one_day_count.plot(), plt.axis('off')
plt.subplot(133), Rs2_one_dist_nearest.plot(), plt.axis('off')
plt.show()


# exemplo de reamostragem mas com nan quando houver falha
ds = xr.open_mfdataset('D:/Dropbox/netcdfgrid3/prec_daily_UT_Brazil_v2*.nc')
var = ds['prec']
a = var.sel(latitude=-20.7, longitude=-41.5, method='nearest')
com_nan = a.to_dataframe()
com_nan.prec.iloc[1:30] = np.nan
g = pd.Grouper(freq='1MS')
pd.concat([com_nan.groupby(g)[c].filter(lambda x: x.isnull().sum()<10).groupby(g).sum()
                    for c in com_nan.columns], axis=1)



# outros exemploscom mascara
import xarray as xr # versao '0.9.6'
import matplotlib.pyplot as plt # versao '2.0.2'
import numpy as np
import cartopy.feature as cfeature

ds = xr.open_mfdataset('D:/Dropbox/netcdfgrid3/prec_daily_UT_Brazil_v2*.nc')
var = ds.prec
# plotando precipitacao mensal
# note que o oceano apresenta valor igual a zero
var.resample('M', dim='time', how='sum').sel(time='1980-01-31').plot()

# criando mascara para o continende e mar
mask_ocean = 2 * np.ones(ds.prec.shape[1:]) * np.isnan(ds.prec.isel(time=0))
mask_land = 1 * np.ones(ds.prec.shape[1:]) * ~np.isnan(ds.prec.isel(time=0))
mask_array = mask_ocean + mask_land

# incorporando mascada no ds
ds.coords['mask'] = (('latitude', 'longitude'), mask_array)

# plotando com mascara
var.resample('M', dim='time', how='sum').sel(time='1980-01-31').where(ds.mask == 1).plot()


primeiro_mes = var.resample('M', dim='time', how='sum').sel(time='1980-01-31')
primeiro_mes.where(ds.mask == 1).where(primeiro_mes<50).plot()

# plotando dados para um intervalo de tempo
mensal2plot = var.resample('M', dim='time', how='sum').sel(time='1980-01-31')
mensal2plot.where(ds.mask == 1).plot()

# plotando seria em um intervalo de tempo
ds['prec'].sel(latitude=-7.2, longitude=-35.9, method='nearest').sel(time=slice('1989-01-01', '1989-06-01')).plot()

# plotando com cartopy
# https://ocefpaf.github.io/python4oceanographers/blog/2013/09/30/natural_earth/
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.feature import NaturalEarthFeature, LAND, COASTLINE, BORDERS
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

def brazil_states(projection=ccrs.PlateCarree()):
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(projection=projection))
    ax.set_extent([-82, -32, -45, 10])
    ax.stock_img()
    ax.add_feature(LAND)
    ax.add_feature(COASTLINE)
    gl = ax.gridlines(draw_labels=True)
    gl.xlabels_top = False
    gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    return fig, ax

fig, ax = brazil_states()
states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',
                             name='admin_1_states_provinces_shp')
_ = ax.add_feature(states, edgecolor='gray', facecolor='none')

# exemplo com estados brasileiros
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import xarray as xr
from cartopy.feature import NaturalEarthFeature, LAND, COASTLINE, BORDERS

data = xr.open_mfdataset('D:/Dropbox/netcdfgrid3//Rs_daily_UT_Brazil_v2*1.nc')
Rs = data['Rs']
fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(projection=ccrs.PlateCarree()))
ax.set_extent([-75, -31, -35, 6])
states = NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',
                             name='admin_1_states_provinces_shp')
ax.coastlines()
ax.add_feature(BORDERS)
ax.set_frame_on(False)
_ = ax.add_feature(states, edgecolor='gray', facecolor='none')
day2get = '2014-01-01'
Rs.sel(time=day2get).plot.pcolormesh(ax=ax, transform=ccrs.PlateCarree())

# arquivo original: testeFilesNetcdf
# calculo sazonais das diferencas entre
# precipitacao e a ETo
# necessarios os arquivos "prec" e ETo"
import xarray as xr # versao '0.9.6'
import matplotlib.pyplot as plt # versao '2.0.2'
import numpy as np
from cartopy.feature import NaturalEarthFeature, BORDERS
import cartopy.crs as ccrs

# pegando dados
# em "~" colocar o caminho correto.
ETo = xr.open_mfdataset('D:/Dropbox/netcdfgrid3//ETo_daily_UT_Brazil_v2*1.nc')
prec = xr.open_mfdataset('D:/Dropbox/netcdfgrid3//prec_daily_UT_Brazil_v2*1.nc')

# criando mascara para o continente e mar
mask_ocean = 2 * np.ones(prec['prec'].shape[1:]) * \
             np.isnan(prec['prec'].isel(time=0))
mask_land = 1 * np.ones(prec['prec'].shape[1:]) * \
            ~np.isnan(prec['prec'].isel(time=0))
mask_array = mask_ocean + mask_land

# incorporando mascara em ETo
ETo.coords['mask'] = (('latitude', 'longitude'), mask_array)

# definindo limites estaduais
states = NaturalEarthFeature(category='cultural', scale='50m',
                             facecolor='none',
                             name='admin_1_states_provinces_shp')

# intervalo da seria historica para os calculos e
# reamostrando para a media mensal diaria
date_start, date_end = '1980-01-01', '2009-12-31'

EToSlice = ETo['ETo'].loc[dict(
    time=slice(date_start, date_end))].resample(
    'M', 'time', how='mean')

precSlice = prec['prec'].loc[dict(
    time=slice(date_start, date_end))].resample(
    'M', 'time', how='mean')

# agrupando nas estacoes ('DJF', 'MAM', 'JJA', 'SON')
EToSeason = EToSlice.groupby('time.season').mean(dim='time')
precSeason = precSlice.groupby('time.season').mean(dim='time')

# calculando diferenças sazonais
diff = precSeason - EToSeason

# plotando
fig, axes = plt.subplots(nrows=4, ncols=3,
                         figsize=(12,10),
                         subplot_kw={'projection':ccrs.Miller()})

for i, season in enumerate(('DJF', 'MAM', 'JJA', 'SON')):
    precSeason.where(ETo.mask == 1).sel(season=season).plot(
        ax=axes[i, 0], transform=ccrs.Miller(), cmap='Spectral',
        vmin=0, vmax=10, extend='both',)

    EToSeason.where(ETo.mask == 1).sel(season=season).plot(
        ax=axes[i, 1],  transform=ccrs.Miller(), cmap='Spectral_r',
        vmin=2, vmax=6, extend='both',)

    diff.where(ETo.mask == 1).sel(season=season).plot(
        ax=axes[i, 2],  transform=ccrs.Miller(), cmap='RdBu',
        vmin=-5, vmax=5, extend='both',)

    axes[i, 0].text(-78, -15, season,
                    rotation='vertical',
                    rotation_mode='anchor',)
    axes[i, 1].set_ylabel('')
    axes[i, 2].set_ylabel('')

for ax in axes.flat:
    ax.axes.get_xaxis().set_ticklabels([])
    ax.axes.get_yaxis().set_ticklabels([])
    ax.axes.axis('tight')
    ax.set_xlabel('')
    ax.set_title('')
    ax.coastlines()
    ax.add_feature(states, edgecolor='gray', facecolor='none')
    ax.add_feature(BORDERS)
    ax.set_extent([-75, -33, -34, 6])

axes[0, 0].set_title('Prec (mm dia$^{-1}$)')
axes[0, 1].set_title('ETo (mm dia$^{-1}$)')
axes[0, 2].set_title('Prec - ETo')

fig.suptitle(u'Diferença sazonal entre '
             u'precipitação e ETo',
             fontsize=16, y=.98)


date = '2015-06-16T12:00:00'
precSemCemadem = xr.open_mfdataset('D:/Dropbox/ProjetoDaviUFPB//prec_daily_UFPB_Brazil_v2_Sem_CEMADEN20150101_20161231.nc')
precSemCemadem['prec'].sel(time=date).plot()
plt.title('media Sem Cemaden Final')

precConv2 = xr.open_mfdataset('D:/Dropbox/ProjetoDaviUFPB//prec_daily_UFPB_Brazil_v3_ADW_Sem_CEMADEN20150101_20161231_Control.nc')
plt.figure()
precConv2['count'].sel(time=date).plot()
plt.title('ADW controle')


precSemCemadem = xr.open_mfdataset('D:/Dropbox/ProjetoDaviUFPB//prec_daily_UFPB_Brazil_v3_ADW_Sem_CEMADEN20150101_20161231.nc')
plt.figure()
precSemCemadem['prec'].sel(time=date).plot()
plt.title('media inicial')
