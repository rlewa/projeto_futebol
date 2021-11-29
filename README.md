# Football EPL - Project

This project's objective is to evaluate the impact that historical statistics, as well as news and bookmakers have on predicting the final results of Premier League matches.
It can be used to develop more sophisticated techniques of predicting results as we pre-trained NLP models using news from many websites to many football championships around the world.

We shall present each result individually and briefly explain them. 

-------------------------


historical_data - https://www.football-data.co.uk/englandm.php


## Data Standardization:

We consider a clean dataframe (.csv file) if its column 'Date' is formated as: 'YYYY-MM-DD'; And both for home and away teams, their names must not be abbreviated. For ex.: 'Man Utd' goes to 'Manchester United'.

Dataframe with historical features (```historical_features``` file) = (7980, 46)
