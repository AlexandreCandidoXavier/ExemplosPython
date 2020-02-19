import xarray as xr # versao '0.9.6'
import matplotlib.pyplot as plt # versao '2.0.2'

""" Para todas as variaveis existem dois controles, um he a distancia 
do centro da celula a estacao mais proxima ("dist_nearest") e o outro
he o numero de estacoes/pluviometros dentro da celula (informacoes 
ver "paper"). 

Aqui serao plotados os controles da grade precipitacaoo em duas 
localidades, Sorriso-MT e Campinas-SP (na verdade he da 
celula mais proxima a estas cidades).
"""

# lendo arquivo
path_var = '/home/alexandre/Dropbox/ParaUbuntu/netcdfgrid3/controls/'
ds = xr.open_mfdataset(path_var + 'prec_daily_UT_Brazil_v2*Control.nc', combine='by_coords')
dist_nearest = ds['dist_nearest']
count = ds['count']

# Nome dos pontos
Names = ['Sorriso-MT', 'Campinas-SP']
lat_lon = [[-12.5, -55.7],
           [-22.8, -47.0],]

# plotando distancia do pluviometro mais proximo, ao longo do tempo,
# que foi utilizado na interpolacao
_, (ax1, ax2) = plt.subplots(2, 1)
for n, names in enumerate(Names):
    dist_nearest.sel(latitude=lat_lon[n][0],
                     longitude=lat_lon[n][1],
                     method='nearest').plot(ax=ax1, label=names)

    # número de estações que contem na célula
    count.sel(latitude=lat_lon[n][0],
              longitude=lat_lon[n][1],
              method='nearest').plot(ax=ax2, label=names)

ax1.set_ylim(0, 150)
ax1.legend()
ax1.set_title('')
ax2.set_ylim(-1, 5)
ax2.legend()
ax2.set_title('')
