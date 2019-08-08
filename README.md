# ExemplosPython
Este repositório trata de vários exemplos de scripts para manuseio dos dados gradeado gerados por Xavier et al. (2016):

Xavier, A. C., King, C. W. and Scanlon, B. R. Daily gridded meteorological variables in Brazil (1980-2013), International Journal of Climatology, pg 2644–2659, May 2016. DOI: 10.1002/joc.4518 (http://onlinelibrary.wiley.com/doi/10.1002/joc.4518/full)

e do trabalho apresentado no SBSR2017:

Xavier, A. C., King, C. W. and Scanlon, B. R. An update of Xavier, King and Scanlon (2016) daily precipitation gridded data set for the Brazil. In Anais do XVIII Simpósio Brasileiro de Sensoriamento Remoto -SBSR. Santos-SP.2017. (http://marte2.sid.inpe.br/rep/sid.inpe.br/marte2/2017/10.23.17.08.52)

# Onde encontrar os dados gradeados

Para download dos arquivos, acessar [aqui](https://www.dropbox.com/sh/awb2ghit03kf39c/AAD69uHiLxVN6IoAwIyXLQ3Pa?dl=0)

# Arquivos necessários
A lista completa dos arquivos NetCDF para rodar os scripts, são apresentados no arquivo [arquivos_NetCDF.txt](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/arquivos_NetCDF.txt).

# Informações sobre atualizações [aqui](https://sites.google.com/site/alexandrecandidoxavierufes/dados-meteorologicos-do-brasil)

# Para exportar todos os dados em CSV

Exportando todos as variáveis diárias de uma ou mais localidades para o formato "cvs". Cada arquivo "csv" corresponde aos dados da célula mais próxima à posição requerida (coordenada, latitude e longitude). [Aqui](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/lat-21.0_lon-44.1.csv) é apresentado exemplo do arquivo exportado, para um pequeno período.

[expor_dados_csv2.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/expor_dados_csv2.py)

# Os resultados gráficos dos scripts

## [exemplo1.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo1.py) Plotando dados e controles

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_1.png)

## [exemplo2.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo2.py) Plotando dados diários e média mensal para uma posição

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_2.png)


## [exemplo3.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo3.py) Plotando média mensal de RH para o Brasil

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_3.png)

## [exemplo4.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo4.py) Plotando média mensal de ETo para algumas cidades

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_4.png)

## [exemplo5.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo5.py) Plotando normais de Tmax para algumas  cidades/instituições

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_5.png)

## [exemplo6.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo6.py) Plotando controles ao longo do tempo para duas localidade

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_6.png)


## [exemplo7.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo7.py) Calculo da diferenca sazonal entre a precipitacao e a ETo para o Brasil 

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_7.png)


## [exemplo8.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo8.py) Plotando temperatura média histórica

Temperatura média (T<sub>média</sub>) para o mês de janeiro, período 01/01/1981-31/12/2009, em que:

T<sub>média</sub>=(T<sub>max</sub>+T<sub>min</sub>)/2

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/Figure_8.png)


## [abrindo_relevo.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/abrindo_relevo.py) Abrindo relevo para a região do Brasil do modelo gmted2010, reamostrado para 0,1 graus

Infromações sobre os dados originais [aqui](https://pubs.usgs.gov/of/2011/1073/pdf/of2011-1073.pdf)

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/gmted2010_reamostrado.png)

## [temp_media_historica_regioes.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/temp_media_historica_regioes.py) Avaliando a variação temperal da temperatura média anual em diferentes regiões no Brasil 

**Regiões**

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/regioes.png)

**Variação temporal**

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/tmean_temporal_regioes.png)


**Resultado das estatisticas (variável "df_stat_region")**

| Regiao        |   slope  | intercept   | r_value   |     p_value |   std_err |
| ------------- | -------- | ----------- | --------- | ----------- | --------- |
| sul           | 0.000010 |  20.512220  | 0.000214  | 9.989955e-01|  0.007881 |
| sudeste       | 0.021973 | -20.729965  | 0.629384  | 3.006463e-05|  0.004586 |
| nordeste      | 0.028534 | -31.322058  | 0.704672  | 1.126270e-06|  0.004856 |
| centro-oeste  | 0.025890 | -26.423567  | 0.790216  | 6.013308e-09|  0.003394 |
| norte         | 0.035253 | -43.624015  | 0.829851  | 2.159944e-10|  0.004007 |


## [koppen_rodando.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/koppen_rodando.py) Classificação de do clima para o brasil de acordo com Koppen e os dados gradeados

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/koppen_brasil.png)
