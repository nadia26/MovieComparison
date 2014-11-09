from flask import Flask,request,url_for,redirect,render_template
import json, urllib2

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#obvs doesnt work yet
@app.route("/results")
@app.route("/results/<movie>")
def results(movie="Dynamite"):
    url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=re8z35f3uhrea4vc46jz4wcg"
    url = url%q(movie)
    request = urlllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    page = ""
    return page

if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=8000)
