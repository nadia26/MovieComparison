import json, urllib2


def find_RT(movie):
    url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=re8z35f3uhrea4vc46jz4wcg&q=%s"
    m = movie.replace(" ","+")
    url = url%(m)
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    if len(d['movies']) == 0:
        return "not found"
    a = d['movies'][0]
    for r in d['movies']:
        if r['title'].upper() == movie:
            if a['title'] != movie:
                a = r
            elif r['year'] > a['year']:
                a = r
    if a['title'].upper() == movie:
        return a
    return "not found"

def get_RTC(movie):
    return movie['ratings']['critics_score']

def get_RTA(movie):
    return movie['ratings']['audience_score']
    
def avg_rtng(m):
    return (m['RTC'] + m['RTA']) / 2

def get_thumb(movie):
    if 'posters' in movie.keys() and 'thumbnail' in movie['posters'].keys():
        return movie['posters']['thumbnail']
    return ""

def get_link(movie):
    if 'links' in movie.keys() and 'alternate' in movie['links'].keys():
        return movie['links']['alternate']
    return "http://www.rottentomatoes.com/"

def get_winner(m1, m2):
    if m1['avg'] > m2['avg']:
        return m1['title']
    return m2['title']
