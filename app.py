from flask import Flask,request,url_for,redirect,render_template
from utils import get_rating, get_winner

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html", msg="")
    else:
        m1 = request.form["movie1"]
        m2 = request.form["movie2"]
        button = request.form["b"]
        if ((button == "Submit") and (m1!="") and (m2!="")):
            return redirect(url_for('q', movie1=m1, movie2=m2))
        else:
            return render_template("index.html", msg="Enter movies!")
            

@app.route("/q/<movie1>&<movie2>", methods=["GET","POST"])
def q(movie1=None, movie2=None):
    movie1_rating = get_rating(movie1)
    movie2_rating = get_rating(movie2)
    if ((movie1_rating==999)or(movie2_rating==999)):
        return render_template("error.html")#movie not found
    winner = get_winner(movie1_rating, movie2_rating, movie1, movie2)
    return render_template("results.html", winner=winner[0], loser=winner[1])#can do so much more with this...

if __name__=="__main__":
   app.debug=True
   app.run()
