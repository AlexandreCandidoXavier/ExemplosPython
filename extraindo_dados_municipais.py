import xarray as xr
import numpy as np
import pandas as pd
import geopandas as gpd
import os
"""Este script gera arquivos diários de prec, Tmax e Tmin, referentes ao centroide de cada municipio brasileiro.
"""

# arquido shape em Brasil
# https://www.ibge.gov.br/geociencias/organizacao-do-territorio/15774-malhas.html?=&t=acesso-ao-produto
brasil = gpd.read_file(os.path.join('/home/alexandre/Dropbox/PythonCodes/juliana/', 'mapas/BR_Municipios_2019.shp'))

# centroides
lon = brasil.geometry.centroid.geometry.x.values
lat = brasil.geometry.centroid.geometry.y.values

# set correct path of the variables
path_var = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/'

# getting NetCDF files
prec = xr.open_mfdataset(path_var + 'prec_daily_UT_Brazil_v2*.nc')['prec']
Tmax = xr.open_mfdataset(path_var + 'Tmax_daily_UT_Brazil_v2*.nc')['Tmax']
Tmin = xr.open_mfdataset(path_var + 'Tmin_daily_UT_Brazil_v2*.nc')['Tmin']

# exportando
pd.DataFrame(prec.sel(longitude=xr.DataArray(lon, dims='z'),
                                          latitude=xr.DataArray(lat, dims='z'),
                                          method='nearest').values,
             columns=brasil.CD_MUN, index=prec.time.values).to_csv('prec_mun.csv', float_format='%.1f')

pd.DataFrame(Tmax.sel(longitude=xr.DataArray(lon, dims='z'),
                                          latitude=xr.DataArray(lat, dims='z'),
                                          method='nearest').values,
             columns=brasil.CD_MUN, index=Tmax.time.values).to_csv('Tmax_mun.csv', float_format='%.1f')

pd.DataFrame(Tmin.sel(longitude=xr.DataArray(lon, dims='z'),
                                          latitude=xr.DataArray(lat, dims='z'),
                                          method='nearest').values,
             columns=brasil.CD_MUN, index=Tmin.time.values).to_csv('Tmin_mun.csv', float_format='%.1f')
