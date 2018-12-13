import xarray as xr

# Lendo dados GMTED2010 reamostrados para resolucao 0,1 graus
path = r'D:\Dropbox\ParaUbuntu'
alt = xr.open_mfdataset(path + '/GMTED2010_RES_GPM.nc')

# para plotar
alt.gmted2010_res_gpm.plot()

# altitude de determinada posicao
alt.gmted2010_res_gpm.sel(lon=-50, lat=-15, method='nearest').values
