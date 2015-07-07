from bs4 import BeautifulSoup
from urllib2 import quote
import unicodedata
import requests
import json
import glob
import pandas as pd

movie_list = []

for page in glob.glob('*.html'):
    with open(page, 'r+') as f:
        my_page = f.read()
        my_soup = BeautifulSoup(my_page)
        for div in my_soup.find_all('div', class_='lockup'):
            try:
                movie_list.append(div.img.get('alt'))
            except:
                movie_list.append('movie could not be extracted from page')
['movie could not be extracted from page' for movie in movie_list if movie is None]


movie_list2 = []


for movie in movie_list:
    try:
        movie = quote(movie)
        movie_list2.append(movie)
    except:
        try:
            movie = unicodedata.normalize('NFKC', movie).encode('ascii','ignore')
            movie = quote(movie)
            movie_list2.append(movie)
        except:
            print movie
            movie_list2.append('movie could not be processed')


all_movies_us = {}
for movie in movie_list2:
    try:
        query_url = 'http://www.omdbapi.com/?t=' + movie + '&y=&plot=full&r=json'
        response = requests.get(query_url)
        my_dict = json.loads(response.text)
        all_movies_us[movie] = my_dict
    except:
        all_movies_us[movie] = 'No response'
    
    print movie






    

# movies/single year shows
years_dict = {}
counter = 0    
for k,v in all_movies.iteritems():
    try:
        if len(v['Year']) == 4:
            try:
                years_dict[v['Year']] += 1
            except:
                years_dict[v['Year']] = 1
                continue
        
    except:
        counter += 1
        continue
print counter
my_frame = pd.DataFrame.from_dict(years_dict, orient = 'index')
my_frame.to_csv('single_years.csv')



counter=0
score_dict = {}
for k,v in all_movies.iteritems():
    try:
        if v['imdbRating'] != 'N/A':
            score_dict[v['Title']] = v['imdbRating']
    except:
        counter +=1 
        continue     
print counter


score_dict2 ={}    
for title, score in score_dict.iteritems():
    try:
        score_dict2[title] = float(score)
    except:
        print score
score_dict = score_dict2
        
average_score = (sum(score_dict.values()))/len(score_dict)
top_25 = 

print average_score







years = []
country = []
language  =[]
actors = []

for movie, results in all_movies.iteritems():
    try:
        years.append(results['Year'])
    except:
        continue
    try:
        country.append(results['Country'])
    except:
        continue
    try:
        language.append(results['Language'])
    except:
        continue
    try:
        for actor in results['Actors'].split(','):
            actors.append(actor)
    except:
        continue

        
# Ongoing shows
years_dict = {}
counter = 0    
for k,v in all_movies.iteritems():
    try:
        print v['Year'][4]
    except:
        continue
        
        
# Languages
lang_list = []
for lang in language:
    for x in lang.split(','):
        lang_list.append(x)
lang_list
Counter(lang_list)
Counter(lang_list).most_common(10)


