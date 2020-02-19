import xarray as xr
import matplotlib.pylab as plt

""" Plotando dados e controles para todo Brasil em um dia:
Todos os arquivos da variavel diarios de Rs sao necessarios, ou seja,
os de controle tambem
"""

# versoes
print(xr.__version__) # 0.14.1
print(plt.__version__) # 1.16.4

# set correct path of the variables
path_var = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/'

# set correct path of the controls
path_control = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/controls/'

data = xr.open_mfdataset(path_var + 'Rs_daily_UT_Brazil_v2*1.nc', combine='by_coords')
data_control = xr.open_mfdataset(path_control + '/Rs_daily_UT_Brazil_v2*_Control.nc', combine='by_coords')
Rs = data['Rs']
Rs_count = data_control['count']
Rs_dist_nearest = data_control['dist_nearest']

# escolhendo o dia
day2get = '2008-05-15'

# Plotando
_, (ax1, ax2, ax3) = plt.subplots(1, 3)
Rs.sel(time=day2get).plot(ax=ax1), ax1.axis('off')
Rs_count.sel(time=day2get).plot(ax=ax2), ax2.axis('off')
Rs_dist_nearest.sel(time=day2get).plot(ax=ax3), ax3.axis('off')
