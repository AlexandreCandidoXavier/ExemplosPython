import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pylab as plt

# limits of the area
lat_min, lat_max = -23.375, -22.125
lon_min, lon_max = -48.625, -45.875

# set correct path of the variables
path_var = 'D:/Dropbox/netcdfgrid3/'

# set correct path of the controls
path_control = 'D:/Dropbox/netcdfgrid3/controls/'

var_names = ['prec', 'Rs', 'u2','Tmax', 'Tmin', 'RH', 'ETo']
# getting NetCDF files
prec = xr.open_mfdataset(path_var + 'prec_daily_UT_Brazil_v2*.nc')
rs = xr.open_mfdataset(path_var + 'Rs_daily_UT_Brazil_v2*.nc')
u2 = xr.open_mfdataset(path_var + 'u2_daily_UT_Brazil_v2*.nc')
tmax = xr.open_mfdataset(path_var + 'Tmax_daily_UT_Brazil_v2*.nc')
tmin = xr.open_mfdataset(path_var + 'Tmin_daily_UT_Brazil_v2*.nc')
rh = xr.open_mfdataset(path_var + 'RH_daily_UT_Brazil_v2*.nc')
eto = xr.open_mfdataset(path_var + 'ETo_daily_UT_Brazil_v2*.nc')

# all latitude and longitude
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

# getting data in the mask area
prec_count = prec_count.where(mask, drop=True)
eto_count = eto_count.where(mask, drop=True)

# plotting controls in the area.
# number of rain gauges and wheater data into the area along the time
prec_count.sum('latitude').sum('longitude').plot()
plt.ylabel('Number of rain gauges')
plt.figure()
eto_count.sum('latitude').sum('longitude').plot()
plt.ylabel('Number of wheather stations')

# starting export variables into the area
# each file will have the data of all variables in just one cell
# where rows are days and columns are:
# 'time', 'prec', 'Rs', 'u2','Tmax', 'Tmin', 'RH', 'ETo'
latToColect = np.array(np.nonzero((latitude >= lat_min) &
                                  (latitude <= lat_max))).flatten()
lonToColect = np.array(np.nonzero((longitude >= lon_min) &
                                  (longitude <= lon_max))).flatten()
number_cell = len(latToColect) * len(lonToColect)
precStation = np.zeros((len(rs.time), len(lonToColect)))*np.nan
count = 1
for n, lat in enumerate(latToColect):
    print('{} de {}:'.format((n + 1), len(latToColect)))
    precStation[:len(prec.time), :] = prec.prec.isel(latitude=lat, longitude=lonToColect).values
    mat = np.c_[precStation,
                rs.Rs.isel(latitude=lat, longitude=lonToColect).values,
                u2.u2.isel(latitude=lat, longitude=lonToColect).values,
                tmax.Tmax.isel(latitude=lat, longitude=lonToColect).values,
                tmin.Tmin.isel(latitude=lat, longitude=lonToColect).values,
                rh.RH.isel(latitude=lat, longitude=lonToColect).values,
                eto.ETo.isel(latitude=lat, longitude=lonToColect).values
                ]

    for n, lon in enumerate(lonToColect):
        print('arquivo {} de um total de {}'.format(count, number_cell))
        name_file = 'lat{}_lon{}.csv'.format((latitude[lat]), longitude[lon])
        file = mat[:, n::len(lonToColect)]
        pd.DataFrame(file, index=rs.time, columns=var_names).to_csv(name_file)
        count += 1


# second Methodology, too much slow
# n = 0
# number_station = len(latToColect)*len(lonToColect)
# for lat in latToColect:
#     for lon in lonToColect:
#         # get precipitation
#         all_variable = np.zeros((len(rs.time), len(var_names)))*np.nan
#         for n, var in enumerate(var_names):
#             print('{} de {}: var name = {}'.format((n + 1),number_station, var))
#             if var == 'prec':
#                 all_variable[:len(prec.time), n] = prec.prec.isel(latitude=lat, longitude=lon).values
#             elif var == 'Rs':
#                 all_variable[:, n] = rs.Rs.isel(latitude=lat, longitude=lon).values
#             elif var == 'u2':
#                 all_variable[:, n] = u2.u2.isel(latitude=lat, longitude=lon).values
#             elif var == 'Tmax':
#                 all_variable[:, n] = tmax.Tmax.isel(latitude=lat, longitude=lon).values
#             elif var == 'Tmin':
#                 all_variable[:, n] = tmin.Tmin.isel(latitude=lat, longitude=lon).values
#             elif var == 'RH':
#                 all_variable[:, n] = rh.RH.isel(latitude=lat, longitude=lon).values
#             else:
#                 all_variable[:, n] = eto.ETo.isel(latitude=lat, longitude=lon).values
#         n += 1
#
#         name_file = 'lixolat{}_lon{}.csv'.format((latitude[lat]), longitude[lon])
#         pd.DataFrame(all_variable, index=rs.time, columns=var_names).to_csv(name_file)