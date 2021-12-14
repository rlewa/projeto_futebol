# Football EPL - Project

This project's objective is to evaluate the impact that historical statistics, as well as news and bookmakers have on predicting the final results of Premier League matches for three possible outcomes: Home, Away and Draw.

We have divided this repository into 2 main parts: The first one has all clean data that we have used as input for the Machine Learning models and the second part has everything related to the models, such as general and specific functions. 

--------------
## Summary

1. [Data](#1)
    1. [Historical](#1.1)
    2. [News](#1.2)
    3. [Bookmakers](#1.3)
2. [Models](#2)
    1. [NLP](#2.1)
    2. [Classification](#2.2)
--------------

<a name="1"></a>

## 1\. Data

As mentioned above, we have three different football related data: Historical, Bookmakers and News. We shall explain them below. 

<a name="1.1"></a>
### 1.1\. Historical

The Historical data was obtained from the [Football-Data](https://www.football-data.co.uk/englandm.php) website, which contains historical results and betting odds for the English Premier League games. We used the 2000/2001 season up to the 2020/2021 season. Each season is a **.csv** file and has many variables, which are present here:

 |FEATURE|MEANING| 
|:------ | -----:|
|**Date** | Date (YYYY-MM-DD)|
|**HomeTeam** | Nome do time da casa|
**AwayTeam** | Nome do time de fora
**FTHG** | Número de gols do time da casa na partida
**FTAG** | Número de gols do time de fora na partida 
**FTR** | Resultado da partida (H, A or D)
**HS** | Qtd. de chutes do time da casa
**AS** | Qtd. de chutes do time de fora
**HST** | Qtd. de chutes do time da casa ao gol
**AST** | Qtd. de chutes do time de fora ao gol
**HC** | Qtd. Escanteios do time da casa
**AC** | Qtd. Escanteios do time de fora
**HF** | Qtd. de faltas que o time da casa fez
**AF** | Qtd. de faltas que o time de fora fez
**HY** | Qtd. de cartões amarelos que o time da casa recebeu
**AY** | Qtd. de cartões amarelos que o time de fora recebeu
**HR** | Qtd. de cartões vermelhos que o time da casa recebeu
**AR** | Qtd. de cartões vermelhos que o time de fora recebeu

It is worth noting that our **Target** variable is **FTR** and it has three classes that are treated as: **Home = 2**, **Away = 0** and **Draw = 1**.

For each .csv file, we created more statistics using the features above and code given by [](), resulting in the following features:

 |FEATURE|MEANING| 
|:------ | -----:|
**HTGS** | Acumulado de gols feitos do time da casa 
**ATGS** | Acumulado de gols feitos do time de fora
**HTGC** | Acumulado de gols recebidos do time da casa
**ATGC** | Acumulado de gols recebidos do time de fora
**HTP** | Qtd. de pontos totais do time da casa
**ATP** | Qtd. de pontos totais do time de fora
**HM1** | Resultado do primeiro jogo mais recente para o time da casa
**AM1** | Resultado do primeiro jogo mais recente para o time de fora
**HM2** | Resultado do segundo jogo mais recente para o time da casa
**AM2** | Resultado do segundo jogo mais recente para o time de fora
**HM3** | Resultado do terceiro jogo mais recente para o time da casa
**AM3** | Resultado do terceiro jogo mais recente para o time de fora
**HM4** | Resultado do quarto jogo mais recente para o time da casa
**AM4** | Resultado do quarto jogo mais recente para o time de fora
**HM5** | Resultado do quinto jogo mais recente para o time da casa
**AM5** | Resultado do quinto jogo mais recente para o time de fora
**HomeTeamLP** | Posição na tabela do time da casa no ano correspondente 
**AwayTeamLP** | Posição na tabela do time de fora no ano correspondente
**MW** | Semana da partida 
**TFormPtsStr** | Sequência de vitórias, empates ou derrotas para o time da casa 
**ATFormPtsStr** | Sequência de vitórias, empates ou derrotas para o time de fora
**HTFormPts** | Pontos acumulados de acordo com o resultado do jogo do time da casa (ganhou = 3, empatou = 1, perdeu = 0) 
**ATFormPts** | Pontos acumulados de acordo com o resultado do jogo do time de fora (ganhou = 3, empatou = 1, perdeu = 0)
**HTGD** | Diferença do acumulado de gols feitos e recebidos do time da casa 
**ATGD** | Diferença do acumulado de gols feitos e recebidos do time de fora
**DiffPts** | Diferença do acumulado de pontos do time da cada e do time de fora
**DiffFormPts** | Diferença do total de pontos acumulados da casa e do time de fora
**DiffLP** | Diferença da posição do time da casa e do time de fora 

 After creating these features, we performed standardization for the date to the 'YYYY-MM-DD' format, the teams names as presented here[]() and the real-valued features. The dataframes are then concatenated and we have the historical features with shape of 7980 rows and 74 columns.


-------------------------

## Data Standardization:

We consider a clean dataframe (.csv file) if its column 'Date' is formated as: 'YYYY-MM-DD'; And both for home and away teams, their names must not be abbreviated. For ex.: 'Man Utd' goes to 'Manchester United'.

Dataframe with historical features (```historical_features``` file) = (7980, 46)



It can be used to develop more sophisticated techniques of predicting results as we pre-trained NLP models using news from many websites to many football championships around the world.
