import json, urllib2

def get_rating(movie):
    rating = 0
    num_ratings = 0
    url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=re8z35f3uhrea4vc46jz4wcg&q=%s"
    m = movie.replace(" ","+")
    url = url%(m)
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    for r in d['movies']:
        if 'ratings' in r.keys():
            if ((r['ratings']['critics_score'])!=-1):
                rating += (r['ratings']['critics_score'])
                num_ratings+=1
            if ((r['ratings']['audience_score'])!=-1):
                rating += (r['ratings']['audience_score'])
                num_ratings+=1
            else:
                pass
    if num_ratings!=0:
        return (rating/num_ratings)
    else:
        return 999#movie not found

def get_winner(r1, r2, m1, m2):
    if max(r1, r2) == r1:
        return m1,m2
    else:
        return m2, m1
