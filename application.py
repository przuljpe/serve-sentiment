from flask import Flask, session, request, redirect, url_for, render_template
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
SECRET_KEY = "BRUH"
app.config.from_object(__name__)

def load_model():
    loaded_model = None
    with open("basic_classifier.pkl", "rb") as fid:
        loaded_model = pickle.load(fid)
    vectorizer = None
    with open("count_vectorizer.pkl", "rb") as vd:
        vectorizer = pickle.load(vd)

    return loaded_model, vectorizer

@app.route("/")
def index():
    return "Your Flask App Works!"

@app.route("/model", methods=["GET", "POST"])
def use_model():
    loaded_model, vectorizer = load_model()
    news = request.args.get("news")
    print(news)
    if news:
        prediction = loaded_model.predict(vectorizer.transform([news]))[0]
        print(prediction)
        outputted = True
    else:
        prediction = None
        outputted = False
    return render_template("index.html", output=prediction, outputted=outputted)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
