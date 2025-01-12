from packages.packages import *

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

def replace_ordinal_date_talksport(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:

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

  dataframe[column] = dataframe[column].str.replace('th', '', 1).str.replace('rd', '', 1).str.replace('nd', '', 1)

  # special cases when for ex.: 31st August 2021 and 28th August 2021 
  dataframe[column] = dataframe[column].apply(lambda x: x.split(' ')[0].replace('st', '', 1) + ' ' + x.split(' ')[1] + ' ' + x.split(' ')[2])
  
  # converts to YYYY-MM-DD
  dataframe[column] = dataframe[column].apply(lambda dataframe_date: date.isoformat(datetime.strptime(dataframe_date, '%d %B %Y').date()))

  return dataframe


def replace_ordinal_date_worldsoccer(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:

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

def change_team_name(df: pd.DataFrame) -> pd.DataFrame:

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

  df.replace('Man United','Manchester United',inplace=True)
  df.replace('Man Utd','Manchester United',inplace=True)
  df.replace('Man City','Manchester City',inplace=True)
  df.replace('West Ham','West Ham United',inplace=True)
  df.replace('Leeds','Leeds United',inplace=True)
  df.replace('Leeds Utd','Leeds United',inplace=True)
  df.replace('Chelsea','Chelsea FC',inplace=True)
  df.replace('Aston Villa\tSat 3pm','Aston Villa',inplace=True)

  df.replace('Liverpool','Liverpool FC',inplace=True)
  df.replace('Fulham','Fulham FC',inplace=True)
  df.replace('Burnley','Burnley FC',inplace=True)
  df.replace('Southampton','Southampton FC',inplace=True)
  df.replace('Everton','Everton FC',inplace=True)
  df.replace('Arsenal','Arsenal FC',inplace=True)
  df.replace('Newcastle','Newcastle United',inplace=True)
  df.replace('West Brom','West Bromwich Albion',inplace=True)
  df.replace('Wolves','Wolverhampton Wanderers',inplace=True)
  df.replace('Tottenham','Tottenham Hotspur',inplace=True)
  df.replace('Spurs','Tottenham Hotspur',inplace=True)
  df.replace('Norwich','Norwich City',inplace=True)
  df.replace('QPR','Queens Park Rangers',inplace=True)
  df.replace('Reading','Reading FC',inplace=True)
  df.replace('Stoke','Stoke City',inplace=True)
  df.replace('Sunderland','Sunderland AFC',inplace=True)
  df.replace('Leicester','Leicester City',inplace=True)
  df.replace('Bournemouth','AFC Bournemouth',inplace=True)
  df.replace('Middlesbrough','Middlesbrough FC',inplace=True)
  df.replace('Brighton','Brighton & Hove Albion',inplace=True)
  df.replace('Huddersfield','Huddersfield Town',inplace=True)
  df.replace('Blackburn','Blackburn Rovers',inplace=True)
  df.replace('Birmingham','Birmingham City',inplace=True)
  df.replace('Bolton','Bolton Wanderers',inplace=True)
  df.replace('Bradford','Bradford City',inplace=True)
  df.replace('Tottenham Hostpur', 'Tottenham Hotspur', inplace = True)
  df.replace('Derby', 'Derby County', inplace = True)
  df.replace('Cardiff', 'Cardiff City', inplace = True)
  df.replace('Hull', 'Hull City', inplace = True)
  df.replace('Newcastle Utd', 'Newcastle United', inplace = True)
  df.replace('Sheff Wed', 'Sheffield Wednesday FC', inplace = True)
  df.replace('Sheffield Wednesday', 'Sheffield Wednesday FC', inplace = True)
  df.replace('Squad sheets Queens Park Rangers', 'Queens Park Rangers', inplace = True)
  df.replace('Swansea', 'Swansea City', inplace = True)
  df.replace('West Bromwich', 'West Bromwich Albion', inplace = True)
  df.replace('Blackburn Rovers\tSat 3pm', 'Blackburn Rovers'  , inplace = True)
  df.replace('Bolton Wanderers\tSat 3pm','Bolton Wanderers' , inplace = True)
  df.replace('Charlton','Charlton Athletic' , inplace = True)
  df.replace('Chelsea\tSat 5.30pm', 'Chelsea FC' , inplace = True)
  df.replace('Coventry', 'Coventry City', inplace = True)

  df.replace('Everton \tSat 3pm', 'Everton FC', inplace = True)
  df.replace('Holland team news', 'Holland', inplace = True)
  df.replace('Ipswich Town', 'Ipswich', inplace = True)
  df.replace('Italy team news', 'Italy', inplace = True)
  df.replace('Manchester United\tSunday 4pm', 'Manchester United', inplace = True)
  df.replace('Manchester city', 'Manchester City', inplace = True)

  df.replace('New Zealand team news','New Zealand', inplace = True)
  df.replace('Notts County | Sunday 3pm', 'Notts County', inplace = True)
  df.replace('Portsmouth\tSunday 1.30pm', 'Portsmouth', inplace = True)
  df.replace('Sheffield Wednesday', 'Sheffield Wednesday FC', inplace = True)
  df.replace('Stoke City\tMonday 8pm', 'Stoke City', inplace = True)
  df.replace('Tottenham Hotpsur', 'Tottenham Hotspur', inplace = True)
  df.replace('Tottenham Hotspur\tSaturday 3pm', 'Tottenham Hotspur', inplace = True)
  df.replace( 'West Bromwich albion',  'West Bromwich Albion', inplace = True)
  df.replace('Wolverhampton Wanderers\tSat 3pm', 'Wolverhampton Wanderers', inplace = True)
  df.replace('MK Dons', 'Milton Keynes Dons', inplace = True)
  df.replace('Wigan', 'Wigan Athletic', inplace = True)
  
  return df


def cleanhtml(raw_html):

  '''
    Remove usual stopwords and specif ones
    Input:
      str: raw string
    Return:
      np.array: array with clean string (no stopwords)
  '''

  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, ' ', raw_html)
  
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

  raw_string = raw_string.split(' ')
  split_string = [str(each_raw_string) for each_raw_string in raw_string if not each_raw_string in stop_words]
  clean_string = " ".join(split_string)
  clean_strings = np.append(clean_strings, clean_string)

  return np.array(clean_strings)

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r' ', string)

def clean_text(text: str) -> str:
    '''
      Cleans and replaces all the following patterns for specified characters
      Input:
      str: text
      Return:
      str: clean text
    '''

    text = text.lower()
    text = text.replace('.', ' ')
    text = text.translate(str.maketrans(' ', ' ', string.punctuation))
    text = fix_text(text)
    text = remove_emoji(text)
    text = cleanhtml(text)    
    text = text.replace('\n\t','')
    text = re.sub(' +', ' ', text)
    text = re.sub(r"\'s", " 's ", text)
    text = re.sub(r"\'ve", " 've ", text)
    text = re.sub(r"n\'t", " 't ", text)
    text = re.sub(r"\'re", " 're ", text)
    text = re.sub(r"\'d", " 'd ", text)
    #print(text)
    text = text.replace('open new windowclick', ' ')
    text = text.replace('windowclick', ' ')
    text = text.replace('whatsapp', ' ')
    text = text.replace('facebook', ' ')
    text = text.replace('twitter', ' ')
    text = re.sub(r"\'ll", " 'll ", text)
    text = re.sub(r"'", "", text)
    text = text.replace("[math]23^{24}[/math]", " ")
    text = re.sub(r"[0-9]", " ", text)
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#)|(\w+:\/\/\S+)", " ", text).split())
    text = re.sub(r'pic.twitter.com/[\w]*'," ", text) 
    text = re.sub(r"[,.;!?#$%&@~|()*+,-./:;<=>?@[\]^_{|}~]\/\'|]\/\'", " ", text)
    text = re.sub(r"\(", " ( ", text)
    text = re.sub(r"\)", " ) ", text)
    text = re.sub(r"\?", " ", text)
    text = re.sub(r'[?|$|.|£|•|!|…|€|°|ª|º|"|""|\']',' ',text)
    text = re.sub(r"\s{2,}", " ", text)
    text = " ".join([lemma(wd) for wd in text.split()])
    text = text.replace("’",'')
    text = text.replace("‘",'')
    text = text.replace("‘",'')
    text = text.replace("–",' ')
    text = text.replace("-",' ')
    text = re.sub(r' +',  ' ', text)    
    text = remove_stopwords(text)[0]
    
    return text
  
def get_scraping_paths(scraping: str, team: str = '*'):

  '''
    Gets all paths to where the WorldSoccer website data is and creates a dataframe with this data

    Input:
      scraping: string ('Scraping1', 'Scraping2', 'Scraping3', 'Scraping4', 'Scraping5'). 
      team: string, which by default is '*' (all available teams). 'Scraping2', 'Scraping3', 'Scraping4' must have team = '*'
    
    Return:
      df1: dataframe with 2 columns: 'date' and 'text' for all available news 
  '''


  if scraping.lower().strip() == 'scraping2' or scraping.lower() == 'scraping3' or scraping.lower() == 'scraping4':
    team = '*'

  scraping = scraping.capitalize()
  scraping_paths = np.array([])   
  for path in glob.glob(f'/content/drive/MyDrive/GitHub/Dados/Noticias/clean_data/{scraping}/{team}.csv'):
    scraping_paths = np.append(scraping_paths, path)

  df1 = pd.read_csv(scraping_paths[0], encoding = 'UTF-8', usecols = ['date', 'text'])

  for i in range(1, len(scraping_paths)):
    df2 = pd.read_csv(scraping_paths[i], encoding = 'UTF-8', usecols = ['date', 'text'])
    df1 = pd.concat([df1, df2], axis = 0, ignore_index = True)  

  df1.drop_duplicates(inplace = True)
  
  # selects news with more than 150 chars to avoid 'empty' news
  df1 = df1.loc[df1['text'].str.len() > 150]
  df1.reset_index(inplace = True, drop = True)


  return df1
