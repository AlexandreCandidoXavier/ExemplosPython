import xarray as xr

# Lendo dados GMTED2010 reamostrados para resolucao 0,1 grau
path = r'D:\Dropbox\ParaUbuntu'
alt = xr.open_mfdataset(path + '/GMTED2010_RES_GPM_Community.nc')

# para plotar
alt.gmted2010_res_gpm.plot(cmap=plt.cm.terrain)

# altitude de determinada posicao
print(alt.gmted2010_res_gpm.sel(lon=-50, lat=-15, method='nearest').values)
