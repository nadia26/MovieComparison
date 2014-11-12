import json, urllib2

def get_rating(movie):
    rating = 0
    num_ratings = 0
    critics_r = 0
    num_cr = 0
    audience_r = 0
    num_ar = 0
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
                critics_r += (r['ratings']['critics_score'])                
                num_ratings+=1
                num_cr+=1
            if ((r['ratings']['audience_score'])!=-1):
                rating += (r['ratings']['audience_score'])
                audience_r += (r['ratings']['audience_score'])
                num_ratings+=1
                num_ar+=1
    if num_ratings!=0:
        return (rating/num_ratings), (critics_r/num_cr), (audience_r/num_ar)
    else:
        return 999#movie not found

    

def get_winner(r1s, r2s, m1, m2):
    if max(r1s[0], r2s[0]) == r1s[0]:
        return m1, r1s, m2, r2s
    else:
        return m2, r2s, m1, r1s
