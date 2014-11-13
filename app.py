from flask import Flask,request,url_for,redirect,render_template
import utils

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html", msg="")
    if request.method=="POST":
        m1 = request.form["movie1"]
        m2 = request.form["movie2"]
        button = request.form["b"]
        if ( (button=="Submit") and (m1!="") and (m2!="") ):
            return redirect(url_for('q', movie1=m1.upper(), movie2=m2.upper()))
        return render_template("index.html", msg="Enter movies!")
            

@app.route("/q/<movie1>&&<movie2>", methods=["GET","POST"])
def q(movie1=None, movie2=None):
    m1RT = utils.find_RT(movie1)
    if m1RT == "not found":
        return render_template("error.html", movie=movie1)
    m2RT = utils.find_RT(movie2)
    if m2RT == "not found":
        return render_template("error.html", movie=movie2)

    m1_ratings = {}
    m2_ratings = {}
    m1_ratings['RTC'] = utils.get_RTC(m1RT)
    m2_ratings['RTC'] = utils.get_RTC(m2RT)
    m1_ratings['RTA'] = utils.get_RTA(m1RT)
    m2_ratings['RTA'] = utils.get_RTA(m2RT)
    m1_ratings['avg'] = utils.avg_rtng(m1_ratings)
    m2_ratings['avg'] = utils.avg_rtng(m2_ratings)
    m1_ratings['title'] = movie1
    m2_ratings['title'] = movie2
    winner = utils.get_winner(m1_ratings,m2_ratings)
    tb1 = utils.get_thumb(m1RT)
    tb2 = utils.get_thumb(m2RT)
    l1 = utils.get_link(m1RT)
    l2 = utils.get_link(m2RT)
    return render_template("results.html",
                           winner = winner,
                           movie1 = movie1,
                           movie2 = movie2,
                           m1_ratings = m1_ratings, 
                           m2_ratings=m2_ratings, 
                           tb1 = tb1, 
                           tb2 = tb2, 
                           l1 = l1, 
                           l2 = l2)

if __name__=="__main__":
   app.debug=True
   app.run()
