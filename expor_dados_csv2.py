import numpy as np
import xarray as xr
import pandas as pd
import time

# positions
lat = [-20.6, -21.0]
lon = [-44.6, -44.1]

# variables names
var_names = ['Rs', 'u2','Tmax', 'Tmin', 'RH', 'prec', 'ETo']

# set correct path of the netcdf files
path_var = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/'

# function to read the netcdf files
def rawData(var2get_xr, var_name2get):
    return var2get_xr[var_name2get].sel(longitude=xr.DataArray(lon, dims='z'),
                                          latitude=xr.DataArray(lat, dims='z'),
                                          method='nearest').values

# getting data from NetCDF files
for n, var_name2get in enumerate(var_names):
    var2get_xr = xr.open_mfdataset(path_var + var_name2get + '_daily_UT_Brazil_v2*.nc')
    if n == 0:
        var_ar = rawData(var2get_xr, var_name2get)
        n_lines = var_ar.shape[0]
        time = var2get_xr.time.values
    elif var_name2get != 'prec':
        var_ar = np.c_[var_ar, rawData(var2get_xr, var_name2get)]
    else:
        prec = rawData(var2get_xr, var_name2get)
        prec_size_var_ar = np.zeros((var_ar.shape[0], len(lon))) * np.nan
        prec_size_var_ar[:prec.shape[0], :] = prec
        var_ar = np.c_[var_ar, prec_size_var_ar]

#  saving
for n in range(len(lat)):
    print('arquivo {} de um total de {}'.format(n+1, len(lat)))
    name_file = 'lat{}_lon{}.csv'.format(lat[n], lon[n])
    if ~np.isnan(var_ar[0, n]):
        file = var_ar[:, n::len(lon)]
        pd.DataFrame(file, index=time, columns=var_names).to_csv(name_file, float_format='%.1f')
