import pandas as pd
import numpy as np
import re
import os

os.chdir("C:/Users/Asus/Desktop/DATA SCIENCE/MAESTRIA/Data Mining/tp_data_mining")
filename = "data/en_lyrics.csv"

lyrics = pd.read_csv(filename, encoding='iso-8859-1')

from collections import Counter

def get_corpus_splitted(serie): 
  text = " ".join(serie)
  return re.findall(r'\b\S+\b', text)

def wordcount_df_from_serie(serie): 
  counter = Counter()
  text = get_corpus_splitted(serie)
  for word in text:
    counter[word] +=1
  return pd.DataFrame(counter.items(), columns=['word', 'counts']).sort_values(by="counts", ascending=False).reset_index(drop=True)

word_count = wordcount_df_from_serie(lyrics.lyrics_cleaning)

word_count.to_csv("data/en_lyrics_word_count.csv", index=False)