from flask import Flask, redirect, render_template, request, url_for
import os
import sys
import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name,100)
    
    
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    positive = 0
    negative = 0
    neutral = 0
    
    analyzer = Analyzer(positives, negatives)
    if tweets != None:
        total = len(tweets)
        for tweet in tweets:
            score = analyzer.analyze(tweet)
            if score > 0.0:
                positive+=1
            elif score < 0.0:
                negative+=1
            else:
                neutral+=1
        
        positive=(positive/total)*100
        negative=(negative/total)*100
        neutral=(neutral/total)*100
    
    else:
        positive = 0
        negative = 0
        neutral = 100
    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
