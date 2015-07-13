from collections import Counter
import urlparse

class Title_stats:
    # returns stats based on the dictionary of titles created.  Movies is a synonym for titles    
    def __init__(self, all_movies):
        self.all_movies = all_movies
        score_dict = {}
        for k,v in all_movies.iteritems():
            try:
                if v['imdbRating'] != 'N/A':
                    score_dict[v['Title']] = float(v['imdbRating'])
            except:
                continue
        self.score_dict = score_dict
        
        self.years = []
        self.country = []
        self.language  =[]
        self.actors = []
        self.year_list = []
        
        for movie, results in all_movies.iteritems():
            try:
                self.years.append(results['Year'])
            except:
                continue
            try:
               self.country.append(results['Country'])
            except:
                continue
            try:
                self.language.append(results['Language'])
            except:
                continue
            try:
                for actor in results['Actors'].split(','):
                    self.actors.append(actor)
            except:
                continue
    
    def average_score(self):
        return sum(self.score_dict.values())/len(self.score_dict)

    def top_movies(self, num = 1):
        self.num = num
        return Counter(self.score_dict).most_common(self.num)
        
    def bottom_movies(self, num = 1):
        self.num = num
        return Counter(self.score_dict).most_common()[-num:]
        
    def ratings_distribution(self):
        self.hist_list = []
        self.hist_list = [int(x) for x in self.score_dict.values()]
        return self.hist_list

    def top_actors(self, num = 1):
        self.num = num
        return Counter(actors).most_common(num)
    
    def nz_origin(self):
        counter = 0
        for thing in self.country:
            if 'New Zealand' in thing:
                counter += 1
        return counter 
    
    def year_first_release_count(self):        
        for year in self.years:
            self.year_list.append(year[:4])
        return Counter(self.year_list)
        

class Compare_regions:
    # returns stats based on the two dictionaries of titles created.    
    def __init__(self, all_movies1, all_movies2):
        self.all_movies1 = all_movies1
        self.all_movies2 = all_movies2
        
    def common_titles(self):
         return [urlparse.unquote(title) for title in (set(self.all_movies1).intersection(set(self.all_movies2)))]
    
    def unique_to_first(self):
        return [urlparse.unquote(title) for title in (set(self.all_movies1).difference(set(self.all_movies2)))]
    
    def combined(self):
        return [urlparse.unquote(title) for title in (set(self.all_movies1).union(set(self.all_movies2)))]
        
        
        
         
        
    