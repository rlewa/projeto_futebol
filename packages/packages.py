import numpy as np
import pandas as pd
import scipy
from scipy.stats import uniform, norm
import pickle
import glob
import random
from random import choice
import seaborn as sns
from seaborn import heatmap
import matplotlib.pyplot as plt

import copy
import string
import regex as re
from ftfy import fix_text
import pattern
from pattern.en import lemma, lexeme
import ftfy
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('english')
nltk.download('stopwords')

import requests
from bs4 import BeautifulSoup

import dateutil.parser
import time
import datetime
from datetime import datetime, date
from datetime import timedelta


from tqdm import tqdm
import unidecode
import re

import xgboost as xgb
from xgboost import XGBClassifier

import gensim
from gensim.models import KeyedVectors, Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import datapath
from gensim import utils
import gensim.models

import tensorflow as tf
import tensorflow
from tensorflow.keras import optimizers, regularizers
from tensorflow.keras.constraints import unit_norm
from tensorflow.keras.layers import Input, Flatten, LSTM, Conv1D, Dense, TimeDistributed, GlobalMaxPooling1D, Lambda
from tensorflow.keras.models import Model, load_model, Sequential

import sklearn
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, log_loss, precision_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, scale
from sklearn.model_selection import RandomizedSearchCV 
from sklearn.pipeline import Pipeline

import transformers
from transformers import AutoModel, AutoTokenizer, AutoConfig
from transformers import BertForMaskedLM, BertModel, BertTokenizer
from transformers import Trainer, TrainingArguments

from google.colab import drive, files
from IPython.display import SVG, clear_output
from itertools import product
