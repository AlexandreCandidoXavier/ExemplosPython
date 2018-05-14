import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pylab as plt
import time

# limits of the area, West-South and East-North
lat_min, lat_max = -32.375, -30.825
lon_min, lon_max = -54.825, -53.475

# variables names
var_names = ['prec', 'Rs', 'u2','Tmax', 'Tmin', 'RH', 'ETo']

# set correct path of the variables
path_var = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/'

# set correct path of the controls
path_control = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/controls/'

# getting NetCDF files
prec = xr.open_mfdataset(path_var + 'prec_daily_UT_Brazil_v2*.nc')
rs = xr.open_mfdataset(path_var + 'Rs_daily_UT_Brazil_v2*.nc')
u2 = xr.open_mfdataset(path_var + 'u2_daily_UT_Brazil_v2*.nc')
tmax = xr.open_mfdataset(path_var + 'Tmax_daily_UT_Brazil_v2*.nc')
tmin = xr.open_mfdataset(path_var + 'Tmin_daily_UT_Brazil_v2*.nc')
rh = xr.open_mfdataset(path_var + 'RH_daily_UT_Brazil_v2*.nc')
eto = xr.open_mfdataset(path_var + 'ETo_daily_UT_Brazil_v2*.nc')

# all latitude and longitude in the area
latitude = prec.latitude.values
longitude = prec.longitude.values

# getting controls data
prec_count = xr.open_mfdataset(path_control + 'prec_daily_UT_Brazil_v2*.nc')['count']
eto_count = xr.open_mfdataset(path_control + 'ETo_daily_UT_Brazil_v2*.nc')['count']

# creating a mask of the area
mask = (lon_min < prec_count.longitude) & \
       (lon_max > prec_count.longitude) & \
       (lat_min < prec_count.latitude) & \
       (lat_max > prec_count.latitude)

# getting control data in the mask area
prec_count = prec_count.where(mask, drop=True)
eto_count = eto_count.where(mask, drop=True)

# plotting controls in the area.
# number of rain gauges and weather data into the area along the time
prec_count.sum('latitude').sum('longitude').plot()
plt.ylabel('Number of rain gauges')
plt.figure()
eto_count.sum('latitude').sum('longitude').plot()
plt.ylabel('Number of weather stations')
plt.show(block=False)
# starting to export variables into the area
# each file will have the data of all variables for just one cell
# where rows are days and columns are:
# 'time', 'prec', 'Rs', 'u2','Tmax', 'Tmin', 'RH', 'ETo'
latToColect = np.array(np.nonzero((latitude >= lat_min) &
                                  (latitude <= lat_max))).flatten()
lonToColect = np.array(np.nonzero((longitude >= lon_min) &
                                  (longitude <= lon_max))).flatten()
number_cell = len(latToColect) * len(lonToColect)
precStation = np.zeros((len(rs.time), len(lonToColect)))*np.nan
lon, lat = np.meshgrid(lonToColect,latToColect)
lon, lat = lon.flatten(), lat.flatten()

start = time.time()
precStation = np.zeros((len(rs.time), len(lon)))*np.nan
precStation[:len(prec.time), :] = prec.prec.isel(longitude=xr.DataArray(lon, dims='z'), latitude=xr.DataArray(lat, dims='z')).values
mat2 = np.c_[precStation,
            rs.Rs.isel(longitude=xr.DataArray(lon, dims='z'), latitude=xr.DataArray(lat, dims='z')).values,
            u2.u2.isel(longitude=xr.DataArray(lon, dims='z'), latitude=xr.DataArray(lat, dims='z')).values,
            tmax.Tmax.isel(longitude=xr.DataArray(lon, dims='z'), latitude=xr.DataArray(lat, dims='z')).values,
            tmin.Tmin.isel(longitude=xr.DataArray(lon, dims='z'), latitude=xr.DataArray(lat, dims='z')).values,
            rh.RH.isel(longitude=xr.DataArray(lon, dims='z'), latitude=xr.DataArray(lat, dims='z')).values,
            eto.ETo.isel(longitude=xr.DataArray(lon, dims='z'), latitude=xr.DataArray(lat, dims='z')).values
]


for n in range(len(lat)):
    print('arquivo {} de um total de {}'.format(n+1, number_cell))
    name_file = 'lat{}_lon{}.csv'.format((latitude[lat[n]]), longitude[lon[n]])
    if ~np.isnan(mat2[0, n]):
        file = mat2[:, n::len(lon)]
        pd.DataFrame(file, index=rs.time, columns=var_names).to_csv(name_file)

print(time.time() - start)
