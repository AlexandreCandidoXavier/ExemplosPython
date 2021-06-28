# ExemplosPython

```diff
- ESTA PÁGINA NÃO SERA MAIS ATUALIZADA! EM CONSTRUÇÃO NO REPOSITÓRIO AlexandreCandidoXavier/BR-DWGD 
- CÓDIGOS PARA A GRADE QUE SERÁ ATUALIZADA.
```


Este repositório trata de vários exemplos de scripts para manuseio dos dados gradeado gerados por Xavier et al. (2016):

Xavier, A. C., King, C. W. and Scanlon, B. R. Daily gridded meteorological variables in Brazil (1980-2013), International Journal of Climatology, pg 2644–2659, May 2016. DOI: 10.1002/joc.4518 (http://onlinelibrary.wiley.com/doi/10.1002/joc.4518/full)

e do trabalho apresentado no SBSR2017:

Xavier, A. C., King, C. W. and Scanlon, B. R. An update of Xavier, King and Scanlon (2016) daily precipitation gridded data set for the Brazil. In Anais do XVIII Simpósio Brasileiro de Sensoriamento Remoto -SBSR. Santos-SP.2017. (http://marte2.sid.inpe.br/rep/sid.inpe.br/marte2/2017/10.23.17.08.52)

# Onde encontrar os dados gradeados

Para download dos arquivos, acessar [aqui](https://utexas.app.box.com/v/Xavier-etal-IJOC-DATA)

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

## [abrindo_relevo.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/abrindo_relevo.py) Abrindo relevo para a região do Brasil do modelo gmted2010, reamostrado para 0,1 grau

Infromações sobre os dados originais [aqui](https://pubs.usgs.gov/of/2011/1073/pdf/of2011-1073.pdf)

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/gmted2010_reamostrado.png)

## [koppen_rodando.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/koppen_rodando.py) Classificação do clima para o brasil de acordo com Koppen e os dados gradeados

![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/koppen_brasil.png)

## [avatar.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/avatar.py) Esboço de código para a construção do meu avatar
![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/avatar.png)

## [exemplo_paraview.py](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/exemplo_paraview.py) Gerando arquivo NetCDF para abrir no ParaView. Video demonstrativo [aqui](https://drive.google.com/file/d/1ghXjHY-xgXYKCIUsKcFgICHj4ZNjrOXn/view)
![](https://github.com/AlexandreCandidoXavier/ExemplosPython/blob/master/figuras/figure_ParaView.png). 
