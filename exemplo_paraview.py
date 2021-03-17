import numpy as np
import xarray as xr

# Gerando arquivo NetCDF da média da Tmax mensal para abrir no programa
# "ParaView", disponível em https://www.paraview.org/
# Baseado em: https://www.youtube.com/watch?v=xdrcMi_FB8Q

# abrindo arquivos Tmax "nc"
var_xr = xr.open_mfdataset('/home/alexandre/Dropbox/grade_2020/data/netcdf_files/Tmax*.nc')['Tmax']

# calculando a media mensal para todo o periodo
var = var_xr.groupby('time.month').mean('time')
var_np = var.values

# criando dimensoes para lat (y) lon (x) e mes (z)
x = var_xr.longitude.values
y = var_xr.latitude.values
z = np.arange(12) # 12 meses
coords = {'z': z, 'y': y, 'x': x}

# criando/gravando DataArray com as informacoes
para_paraview = xr.DataArray(var_np, dims=('z', 'y', 'x'), coords=coords)
para_paraview.to_netcdf('teste_paraview.nc')
