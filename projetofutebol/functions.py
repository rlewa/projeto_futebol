import pandas as pd 

def format_date(dataframe: pd.DataFrame, date_column: str) -> pd.DataFrame:

  '''
  Formats date to: YYYY-MM-DD

  Input:
    pd.DataFrame: dataframe to be changed
    str: name of date column
  
  Return:
    pd.DataFrame: new dataframe with formated date

  Example:
    '12/08/2021' -> '2021-08-12'
  '''

  dataframe[date_column] = dataframe[date_column].apply(lambda x: str(pd.to_datetime(x, dayfirst=True)).split()[0])
  return dataframe


def change_team_name(dataframe: pd.DataFrame) -> pd.DataFrame:

  '''
  Changes teams names 

  Input:
    pd.Dataframe: dataframe to be changed

  Return 
    pd.DataFrame: new dataframe with names changed

  Example:
    'Man Utd' -> 'Manchester United'
    'Man City' -> 'Manchester City'
  '''

  dataframe.replace('Man United','Manchester United',inplace=True)
  dataframe.replace('Man City','Manchester City',inplace=True)
  dataframe.replace('West Ham','West Ham United',inplace=True)
  dataframe.replace('Chelsea','Chelsea FC',inplace=True)
  dataframe.replace('Liverpool','Liverpool FC',inplace=True)
  dataframe.replace('Fulham','Fulham FC',inplace=True)
  dataframe.replace('Burnley','Burnley FC',inplace=True)
  dataframe.replace('Southampton','Southampton FC',inplace=True)
  dataframe.replace('Everton','Everton FC',inplace=True)
  dataframe.replace('Arsenal','Arsenal FC',inplace=True)
  dataframe.replace('Newcastle','Newcastle United',inplace=True)
  dataframe.replace('West Brom','West Bromwich Albion',inplace=True)
  dataframe.replace('Wolves','Wolverhampton Wanderers',inplace=True)
  dataframe.replace('Tottenham','Tottenham Hotspur',inplace=True)
  dataframe.replace('Norwich','Norwich City',inplace=True)
  dataframe.replace('QPR','Queens Park Rangers',inplace=True)
  dataframe.replace('Reading','Reading FC',inplace=True)
  dataframe.replace('Stoke','Stoke City',inplace=True)
  dataframe.replace('Sunderland','Sunderland AFC',inplace=True)
  dataframe.replace('Leicester','Leicester City',inplace=True)
  dataframe.replace('Bournemouth','AFC Bournemouth',inplace=True)
  dataframe.replace('Middlesbrough','Middlesbrough FC',inplace=True)
  dataframe.replace('Brighton','Brighton & Hove Albion',inplace=True)
  dataframe.replace('Huddersfield','Huddersfield Town',inplace=True)

  return dataframe