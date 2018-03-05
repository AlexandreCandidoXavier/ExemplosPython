import xarray as xr # versao '0.9.6'
import matplotlib.pyplot as plt # versao '2.0.2'

"""Para todas as variaveis existem dois controles, um he a distancia 
do centro da celula a estacao mais proxima ("dist_nearest") e o outro
he o numero de estacoes/pluviometros dentro da celula (informacoes 
ver "paper"). 

Aqui serao plotados os controles da grade precipitacaoo em duas 
localidades, Sorriso-MT e Campinas-SP (na verdade he da 
celula mais proxima a estas cidades).

Arquivos necessarios:
prec_daily_UT_Brazil_v2.2_19800101_19891231_Control.nc
prec_daily_UT_Brazil_v2.2_19900101_19991231_Control.nc
prec_daily_UT_Brazil_v2.2_20000101_20091231_Control.nc
prec_daily_UT_Brazil_v2.2_20100101_20151231_Control.nc"""

# lendo arquivo
path_var = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/controls/'
ds = xr.open_mfdataset(path_var + 'prec_daily_UT_Brazil_v2*control.nc')
dist_nearest = ds['dist_nearest']
count = ds['count']

# Nome dos pontos
Names = ['Sorriso-MT', 'Campinas-SP']
lat_lon = [[-12.5, -55.7],
           [-22.8, -47.0],]

# plotando distancia do pluviometro mais proximo, ao longo do tempo,
# que foi utilizado na interpolacao
ax = plt.subplot(2, 1, 1)
for n, names in enumerate(Names):
    dist_nearest.sel(latitude=lat_lon[n][0],
                     longitude=lat_lon[n][1],
                     method='nearest').plot(label=names)
plt.legend()
plt.title('')

# plotando o numero de pluviometros existentes dentro das
# celulas que contem os municipios
ax = plt.subplot(2, 1, 2)
for n, names in enumerate(Names):
    count.sel(latitude=lat_lon[n][0],
              longitude=lat_lon[n][1],
              method='nearest').plot(label=names)

plt.legend()
plt.title('')
plt.show()