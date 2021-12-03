import pandas as pd 
import numpy as np
import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('english')
nltk.download('stopwords')
import regex as re
from ftfy import fix_text
import pattern
from pattern.en import lemma, lexeme
from datetime import datetime, date


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

def replaces_ordinal_date_talksport(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:

  '''
    Replaces ordinal dates for dates formated as: YYYY-MM-DD to the talksport website dataframe
  
    Input:
      pd.DataFrame: dataframe to be replaced
      str: date column 

    Return:
      pd.DataFrame: formated dataframe

    Example:
      '2nd July 2021' -> '2021-07-02'
  '''

  dataframe[column] = dataframe[column].str.replace('th', '').str.replace('st', '').str.replace('rd', '').str.replace('nd', '')
  dataframe[column] = dataframe[column].apply(lambda dataframe_date: date.isoformat(datetime.strptime(dataframe_date, '%d %B %Y').date()))

  return dataframe

def replaces_ordinal_date_worldsoccer(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:

  '''
    Replaces ordinal dates for dates formated as: YYYY-MM-DD to the worldsoccer website dataframe
  
    Input:
      pd.DataFrame: dataframe to be replaced
      str: date column 

    Return:
      pd.DataFrame: formated dataframe

    Example:
      'July 2, 2021' -> '2021-07-02'
  '''

  dataframe[column] = dataframe[column].apply(lambda dataframe_date: date.isoformat(datetime.strptime(dataframe_date, '%B %d, %Y').date()))

  return dataframe

def replaces_date_thesun(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:

  '''
    Replaces dates for dates formated as: YYYY-MM-DD to the thesun website dataframe
  
    Input:
      pd.DataFrame: dataframe to be replaced
      str: date column 

    Return:
      pd.DataFrame: formated dataframe

    Example:
      '2 Dec 2021' -> '2021-12-02'
  '''

  dataframe[column] = dataframe[column].apply(lambda dataframe_date: date.isoformat(datetime.strptime(dataframe_date, '%d %b %Y').date()))

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



def cleanhtml(raw_html):

  '''
    Remove usual stopwords and specif ones

    Input:
      str: raw string

    Return:
      np.array: array with clean string (no stopwords)
  '''

  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  
  return cleantext

def remove_stopwords(raw_string: str) -> np.array:

  '''
    Remove usual stopwords and specif ones

    Input:
      str: raw string

    Return:
      np.array: array with clean string (no stopwords)
  '''

  clean_strings = np.array([])

  stop_words = stopwords.words("english")
  stop_words.append('classembedyoutube')
  stop_words.append('styletextaligncenter')
  stop_words.append('blockiframe')
  stop_words.append('allowfullscreentrue')
  stop_words.append('classyoutubeplayer')
  stop_words.append('sandboxallowscript')
  stop_words.append('allowsameorigin')
  stop_words.append('allowpopup')
  stop_words.append('allowpresentation')
  stop_words.append('srchttpswwwyoutubecomembedcxl')
  stop_words.append('crxvxawversion')
  stop_words.append('amprel')
  stop_words.append('ampshowsearch')
  stop_words.append('ampshowinfo')
  stop_words.append('ampivloadpolicy')
  stop_words.append('ampf')
  stop_words.append('amphlenusampautohide')
  stop_words.append('ampwmodetransparent')
  stop_words.append('styleborder width')
  stop_words.append('srchttpswwwyoutubecomembedrlosmhbpfswversion')
  stop_words.append('srchttpswwwyoutubecomembedrlosmhbpf wversion')
  stop_words.append('srchttpswwwyoutubecomembedrlosmhbpfswversion')
  stop_words.append('srchttpswwwyoutubecomembedrlosmhbpf wversion')
  stop_words.append("'ll")
  stop_words.append("'t")
  stop_words.append("'d")
  stop_words.append("'re")
  stop_words.append("'s")
  stop_words.append("'ve")
  stop_words.append("i'm")
  stop_words.append("h")
  stop_words.append('getty')
  stop_words.append('image')

  split_string = [str(each_raw_string) for each_raw_string in raw_string if not each_raw_string in stop_words]
  clean_string = " ".join(split_string)
  clean_strings = np.append(clean_strings, clean_string)

  return np.array(clean_strings)

def clean_text(text: str) -> str:
    '''
      Cleans and replaces all the following patterns for specified characters

      Input:
      str: text

      Return:
      str: clean text
    '''

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = fix_text(text)
    text = cleanhtml(text)    
    text = text.replace('\n\t','')
    text = re.sub(' +', ' ', text)
    text = re.sub(r"\'s", " 's ", text)
    text = re.sub(r"\'ve", " 've ", text)
    text = re.sub(r"n\'t", " 't ", text)
    text = re.sub(r"\'re", " 're ", text)
    text = re.sub(r"\'d", " 'd ", text)
    text = text.replace('open new windowclick', ' ')
    text = text.replace('windowclick', ' ')
    text = text.replace('whatsapp', ' ')
    text = text.replace('facebook', ' ')
    text = text.replace('twitter', ' ')
    text = re.sub(r"\'ll", " 'll ", text)
    text = re.sub(r"'", "", text)
    text = text.replace("[math]23^{24}[/math]", "")
    text = re.sub(r"[0-9]", " ", text)
    text = re.sub(r"[,.;!?#$%&@~|()*+,-./:;<=>?@[\]^_{|}~]\/\'|]\/\'", " ", text)
    text = re.sub(r"\(", " ( ", text)
    text = re.sub(r"\)", " ) ", text)
    text = re.sub(r"\?", " ", text)
    text = re.sub(r'[?|$|.|£|•|!|€|°|ª|º|"|""|\']',r'',text)
    text = re.sub(r"\s{2,}", " ", text)
    text = " ".join([lemma(wd) for wd in text.split()])
    text = text.replace("’",'')
    text = text.replace("‘",'')
    text = text.replace("‘",'')
    text = text.replace("–",' ')
    text = text.replace("-",' ')
    text = re.sub(r' +',  ' ', text)
    text = text.split()

    spec_char = ['www', '…']
    
    for i, j in enumerate(text):
      for chars in spec_char:
        if chars in j:
          del text[i]
    
    text = remove_stopwords(text)[0]


    return text
