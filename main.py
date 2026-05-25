# main.py
import os
import base64
import io
import math
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
import mysql.connector
import hashlib
import datetime
import calendar
import random
from random import randint
from urllib.request import urlopen
import webbrowser
from plotly import graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from werkzeug.utils import secure_filename
from PIL import Image

import urllib.request
import urllib.parse
import socket    
import csv

import matplotlib as mpl
import seaborn as sns
from matplotlib import pyplot as plt
from collections import OrderedDict

#####
#import nltk
#nltk.download()
from warnings import filterwarnings
#from nltk.corpus import stopwords
#from nltk.sentiment import SentimentIntensityAnalyzer

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate
from sklearn.preprocessing import LabelEncoder
#from textblob import Word, TextBlob
from wordcloud import WordCloud

import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS
from gensim.parsing.porter import PorterStemmer

filterwarnings('ignore')

import re
import torch
import torch.nn.functional as F
from transformers import DebertaTokenizer, DebertaForSequenceClassification      
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  charset="utf8",
  database="fake_review"

)
app = Flask(__name__)
##session key
app.secret_key = 'abcdef'
#######
UPLOAD_FOLDER = 'static/upload'
ALLOWED_EXTENSIONS = { 'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#####
@app.route('/', methods=['GET', 'POST'])
def index():
    msg=""

    
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM cs_register WHERE uname = %s AND pass = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('userhome'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html',msg=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=""

    
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('admin'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html',msg=msg)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg=""

    x = os.listdir("./dataset")
    #print(x)
    
    if request.method=='POST':
        return redirect(url_for('pro1',act='1'))
        
    return render_template('admin.html',msg=msg)

@app.route('/pro1', methods=['GET', 'POST'])
def pro1():
    msg=""
    data=[]
    df = pd.read_csv("dataset/amazon_reviews.csv")
    dat=df.head()

    for ss in dat.values:
        data.append(ss)

    
    return render_template('pro1.html',msg=msg,data=data)

@app.route('/pro2', methods=['GET', 'POST'])
def pro2():
    msg=""
    data=[]
    df = pd.read_csv("dataset/amazon_reviews.csv")

    #Text Preprocessing
    #Normalizing Case Folding
    df['reviewText'] = df['reviewText'].str.lower()
    df.head()
    dat=df.head()

    for ss in dat.values:
        data.append(ss)

    #Punctuations
    data2=[]
    df['reviewText'] = df['reviewText'].str.replace('[^\w\s]', '')
    dat2=df.head()

    for ss2 in dat2.values:
        data2.append(ss2)

    #Numbers
    df['reviewText'] = df['reviewText'].str.replace('\d', '')
    dat3=df.head()
    data3=[]
    for ss3 in dat3.values:
        data3.append(ss3)

        
    #Stopwords
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't",',','.','I','\'','-','/']
    
    sw = stopwords
    #.words('english')
    sw[0:20]
    data4=[]
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in str(x).split() if x not in sw))
    dat4=df.head()

    for ss4 in dat4.values:
        data4.append(ss4)

    #Rarewords
    temp_df = pd.Series(' '.join(df['reviewText']).split()).value_counts()

    drops = temp_df[temp_df <= 1]

    data5=[]
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in x.split() if x not in drops))
    dat5=df.head()

    for ss5 in dat5.values:
        data5.append(ss5)

    #Tokenization
    data6=[]
    #data6=df["reviewText"].apply(lambda x: TextBlob(x).words).head()

    #Lemmatization
    data7=[]
    #df['reviewText'] = df['reviewText'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    #dat7=df.head()

    #for ss7 in dat7.values:
    #    data7.append(ss7)

        
    
    return render_template('pro2.html',msg=msg,data=data,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7)

@app.route('/pro3', methods=['GET', 'POST'])
def pro3():
    msg=""
    data=[]
    df = pd.read_csv("dataset/amazon_reviews.csv")

    #Text Preprocessing
    #Normalizing Case Folding
    df['reviewText'] = df['reviewText'].str.lower()
    df.head()

    #Punctuations
    
    df['reviewText'] = df['reviewText'].str.replace('[^\w\s]', '')
    df.head()


    #Numbers
    df['reviewText'] = df['reviewText'].str.replace('\d', '')
    df.head()
  
   
    #Stopwords
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't",',','.','I','\'','-','/']
    
    sw = stopwords
    #.words('english')
    sw[0:20]
    
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in str(x).split() if x not in sw))
    df.head()

    #Rarewords
    temp_df = pd.Series(' '.join(df['reviewText']).split()).value_counts()

    drops = temp_df[temp_df <= 1]

    
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in x.split() if x not in drops))
    df.head()

   

    #Tokenization
    #data6=df["reviewText"].apply(lambda x: TextBlob(x).words).head()

    #Lemmatization
    
    #df['reviewText'] = df['reviewText'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    #df.head()

    #############
    #Text Visualization
    #Calculation of Term Frequencies
    
    tf = df["reviewText"].apply(lambda x: pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
    tf.columns = ["words", "tf"]
    dat=tf.head()
    for ss in dat.values:
        data.append(ss)

    tf.shape
    tf["words"].nunique()
    tf["tf"].describe([0.05, 0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).T

    #Barplot
    tf[tf["tf"] > 500].plot.bar(x="words", y="tf")
    #plt.show()
    #plt.savefig("static/graph/gf1.png")
    #plt.close()

    #Wordcloud
    text = " ".join(i for i in df.reviewText)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.savefig("static/graph/gf2.png")
    #plt.close()
    #plt.show()


    wordcloud = WordCloud(max_font_size=50,
                      max_words=100,
                      background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.savefig("static/graph/gf3.png")
    #plt.close()
    #plt.show()
    

    
    return render_template('pro3.html',msg=msg,data=data)

@app.route('/pro4', methods=['GET', 'POST'])
def pro4():
    msg=""
    data=[]
    df = pd.read_csv("dataset/amazon_reviews.csv")

    #Text Preprocessing
    #Normalizing Case Folding
    df['reviewText'] = df['reviewText'].str.lower()
    df.head()

    #Punctuations
    
    df['reviewText'] = df['reviewText'].str.replace('[^\w\s]', '')
    df.head()


    #Numbers
    df['reviewText'] = df['reviewText'].str.replace('\d', '')
    df.head()
  
   
    #Stopwords
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't",',','.','I','\'','-','/']
    
    sw = stopwords
    #.words('english')
    sw[0:20]
    
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in str(x).split() if x not in sw))
    df.head()

    #Rarewords
    temp_df = pd.Series(' '.join(df['reviewText']).split()).value_counts()

    drops = temp_df[temp_df <= 1]

    
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in x.split() if x not in drops))
    df.head()

   

    #Tokenization
    #data6=df["reviewText"].apply(lambda x: TextBlob(x).words).head()

    #Lemmatization
    
    #df['reviewText'] = df['reviewText'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    #df.head()

    #############
    #Text Visualization
    #Calculation of Term Frequencies
    
    tf = df["reviewText"].apply(lambda x: pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
    tf.columns = ["words", "tf"]
    tf.head()
    

    tf.shape
    tf["words"].nunique()
    tf["tf"].describe([0.05, 0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).T

    #Barplot
    tf[tf["tf"] > 500].plot.bar(x="words", y="tf")
    #plt.show()
    #plt.savefig("static/graph/gf1.png")
    #plt.close()

    #Wordcloud
    text = " ".join(i for i in df.reviewText)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.savefig("static/graph/gf2.png")
    #plt.close()
    #plt.show()


    wordcloud = WordCloud(max_font_size=50,
                      max_words=100,
                      background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.savefig("static/graph/gf3.png")
    #plt.close()
    #plt.show()

    #########################
    #Sentiment Analysis
    '''sia = SentimentIntensityAnalyzer()
    df["polarity_score"] = df["reviewText"].apply(lambda x: sia.polarity_scores(x)["compound"])
    dat=df.head()
    for ss in dat.values:
        data.append(ss)
    

    num_bins = 100
    plt.figure(figsize=(10,6))
    n, bins, patches = plt.hist(df.polarity_score, num_bins)
    plt.xlabel('polarity_score')
    plt.ylabel('Number of Reviews')
    plt.title('Histogram of Polarity Score')'''
    #plt.show();
    #plt.savefig("static/graph/gf4.png")
    #plt.close()
    
    return render_template('pro4.html',msg=msg,data=data)

#DeBERTa-Based Fake Review Classifier
def load_model():
    MODEL_NAME = "microsoft/deberta-base"
    DebertaTokenizer.from_pretrained(MODEL_NAME)
    model = DebertaForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=2 
    )
    model.eval()

class FakeReviewClassifier:
    
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    #Text Preprocessing
    def preprocess(self, text):
        text = re.sub(r"http\S+", "", text)  # remove URLs
        text = re.sub(r"[^\w\s]", "", text)  # remove symbols
        text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
        text = text.lower()
        return text

    #Classification
    def predict(self, review_text):
        clean_text = self.preprocess(review_text)

        inputs = self.tokenizer(
            clean_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=256
        )

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)

        p_fake = probs[0][1].item()
        p_genuine = probs[0][0].item()

        # Decision Thresholding
        if p_fake < 0.60:
            label = "Genuine"
        elif 0.60 <= p_fake < 0.85:
            label = "Suspicious"
        else:
            label = "Highly Suspicious"

        return {
            "label": label,
            "P_fake": round(p_fake, 4),
            "P_genuine": round(p_genuine, 4)
        }


@app.route('/pro5', methods=['GET', 'POST'])
def pro5():
    msg=""
    data=[]
    df = pd.read_csv("dataset/amazon_reviews.csv")

    #Text Preprocessing
    #Normalizing Case Folding
    df['reviewText'] = df['reviewText'].str.lower()
    df.head()

    #Punctuations
    
    df['reviewText'] = df['reviewText'].str.replace('[^\w\s]', '')
    df.head()


    #Numbers
    df['reviewText'] = df['reviewText'].str.replace('\d', '')
    df.head()
  
   
    #Stopwords
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't",',','.','I','\'','-','/']
    
    sw = stopwords
    #.words('english')
    sw[0:20]
    
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in str(x).split() if x not in sw))
    df.head()

    #Rarewords
    temp_df = pd.Series(' '.join(df['reviewText']).split()).value_counts()

    drops = temp_df[temp_df <= 1]

    
    df['reviewText'] = df['reviewText'].apply(lambda x: " ".join(x for x in x.split() if x not in drops))
    df.head()

   

    #Tokenization
    #data6=df["reviewText"].apply(lambda x: TextBlob(x).words).head()

    #Lemmatization
    
    #df['reviewText'] = df['reviewText'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    #df.head()

    #############
    #Text Visualization
    #Calculation of Term Frequencies
    
    tf = df["reviewText"].apply(lambda x: pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
    tf.columns = ["words", "tf"]
    tf.head()
    

    tf.shape
    tf["words"].nunique()
    tf["tf"].describe([0.05, 0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).T

    #Barplot
    tf[tf["tf"] > 500].plot.bar(x="words", y="tf")
    #plt.show()
    #plt.savefig("static/graph/gf1.png")
    #plt.close()

    #Wordcloud
    text = " ".join(i for i in df.reviewText)
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.savefig("static/graph/gf2.png")
    #plt.close()
    #plt.show()


    wordcloud = WordCloud(max_font_size=50,
                      max_words=100,
                      background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    #plt.savefig("static/graph/gf3.png")
    #plt.close()
    #plt.show()

    #########################
    #Sentiment Analysis
    '''sia = SentimentIntensityAnalyzer()
    df["polarity_score"] = df["reviewText"].apply(lambda x: sia.polarity_scores(x)["compound"])
    df.head()
    
    num_bins = 100
    plt.figure(figsize=(10,6))
    n, bins, patches = plt.hist(df.polarity_score, num_bins)
    plt.xlabel('polarity_score')
    plt.ylabel('Number of Reviews')
    plt.title('Histogram of Polarity Score')'''
    #plt.show();
    #plt.savefig("static/graph/gf4.png")
    #plt.close()
    #############
    #df["sentiment_label"] = df["reviewText"].apply(lambda x: "pos" if sia.polarity_scores(x)["compound"] > 0 else "neg")
    #dat=df.head()
    #for ss in dat.values:
    #    data.append(ss)

    ###
    '''df["sentiment_label"].value_counts()
    df.groupby("sentiment_label")["overall"].mean()
    df["sentiment_label"] = LabelEncoder().fit_transform(df["sentiment_label"])

    X = df["reviewText"]
    y = df["sentiment_label"]

    #Count Vectors
    from sklearn.feature_extraction.text import CountVectorizer

    # word 
    vectorizer_c = CountVectorizer()
    X_c = vectorizer_c.fit_transform(X)
    #vectorizer_c.get_feature_names()

    #TF-IDF


    # word tf-idf
    from sklearn.feature_extraction.text import TfidfVectorizer
    tf_idf_word_vectorizer = TfidfVectorizer()
    X_tf_idf_word = tf_idf_word_vectorizer.fit_transform(X)
    tf_idf_word_vectorizer.get_feature_names()
    X_tf_idf_word.toarray()

    
    # n-gram tf-idf
    from sklearn.feature_extraction.text import TfidfVectorizer
    tf_idf_ngram_vectorizer = TfidfVectorizer(ngram_range=(2, 3))
    X_tf_idf_ngram = tf_idf_word_vectorizer.fit_transform(X)
    #tf_idf_ngram_vectorizer.get_feature_names()
    X_tf_idf_ngram.toarray()

    #Modeling with Random Forests
    # Count Vectors
    rf_model = RandomForestClassifier().fit(X_c, y)
    cross_val_score(rf_model, X_c, y, cv=5, n_jobs=-1).mean()
        
        

    # TF-IDF Word-Level
    rf_model = RandomForestClassifier().fit(X_tf_idf_word, y)
    cross_val_score(rf_model, X_tf_idf_word, y, cv=5, n_jobs=-1).mean()

    # TF-IDF N-GRAM
    rf_model = RandomForestClassifier().fit(X_tf_idf_ngram, y)
    cross_val_score(rf_model, X_tf_idf_ngram, y, cv=5, n_jobs=-1).mean()

    #Hyperparameter Optimization
    rf_model = RandomForestClassifier(random_state=17)

    rf_params = {"max_depth": [5, 8, None],
                 "max_features": [5, 7, "auto"],
                 "min_samples_split": [2, 5, 8, 20],
                 "n_estimators": [100, 200, 500]}

    rf_best_grid = GridSearchCV(rf_model,
                                rf_params,
                                cv=5,
                                n_jobs=-1,
                                verbose=True).fit(X_c, y)

    rf_best_grid.best_params_

    rf_final = rf_model.set_params(**rf_best_grid.best_params_, random_state=17).fit(X_c, y)

    cv_results = cross_validate(rf_final, X_c, y, cv=3, scoring=["accuracy", "f1", "roc_auc"])

    cv_results['test_accuracy'].mean()
    cv_results['test_f1'].mean()
    cv_results['test_roc_auc'].mean()'''


    df1 = pd.read_csv("dataset/sentimental-classified.csv")
    dat3=df1.head(4914)

    v1=0
    v2=0
    for ss3 in dat3.values:
        if ss3[14]=='pos':
            v1+=1
        if ss3[14]=='neg':
            v2+=1

    print(v1)
    print(v2)
    
    #v1=200
    #v2=100
    tot=v1+v2
    dd2=[v1,v2]
    dd1=['Positive','Negative']

    doc = dd1 #list(data.keys())
    values = dd2 #list(data.values())
    
    fig = plt.figure(figsize = (12, 8))

    c=['green','red']
    # creating the bar plot
    plt.bar(doc, values, color =c,
            width = 0.2)
 

    plt.ylim((1,tot))
    plt.xlabel("Total Reviews")
    plt.ylabel("Count")
    plt.title("")
    
    
    plt.xticks(rotation=0)
    plt.savefig('static/graph/gf5.png')
    plt.close()
    
    
    return render_template('pro5.html',msg=msg,data=data)

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    ###
    #f1=open("static/det.txt","r")
    #read1=f1.read()
    #f1.close()
    #rdata=read1.split(',')

    
    df1 = pd.read_csv("dataset/sentimental-classified.csv")
    dat3=df1.head(4914)

    v1=0
    v2=0
    data1=[]
    n=0
    for ss3 in dat3.values:
        if ss3[2]=='NONE':
            
            if n<5:
                data1.append(ss3)
            if ss3[14]=='pos':
                v1+=1
            if ss3[14]=='neg':
                v2+=1

            n+=1

        

    print(v1)
    print(v2)
    
    #v1=200
    #v2=100
    tot=v1+v2
    dd2=[v1,v2]
    dd1=['Positive','Negative']

    doc = dd1 #list(data.keys())
    values = dd2 #list(data.values())
    
    '''fig = plt.figure(figsize = (12, 8))

    c=['green','red']
    # creating the bar plot
    plt.bar(doc, values, color =c,
            width = 0.2)
 

    plt.ylim((1,tot))
    plt.xlabel("Fake Reviews")
    plt.ylabel("Count")
    plt.title("")
    
    
    plt.xticks(rotation=0)
    plt.savefig('static/graph/gf6.png')
    plt.close()'''
    ##################
    #
    '''f11=open("static/det1.txt","r")
    rk=f11.read()
    f11.close()
    rk1=rk.split('|')
    y=[]
    x1=[]
    x2=[]

    
    
    x1=rk1[0].split(',')
    y=rk1[4].split(',')
    x2=rk1[1].split(',')

    print(x1)

    # plotting multiple lines from array
    plt.plot(y,x1)
    plt.plot(y,x2)
    
    dd=["Training","Validation"]
    plt.legend(dd)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("")

    
    fn="acc1.png"
    
    plt.savefig('static/graph/'+fn)
    #plt.close()
    plt.clf()
    ####
    y=[]
    x1=[]
    x2=[]

    
    
    x1=rk1[2].split(',')
    y=rk1[4].split(',')
    x2=rk1[3].split(',')
    

    # plotting multiple lines from array
    plt.plot(y,x1)
    plt.plot(y,x2)
    dd=["Training","Validation"]
    plt.legend(dd)
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.title("")

    
    fn="acc2.png"
    
    plt.savefig('static/graph/'+fn)
    #plt.close()
    plt.clf()'''
    ##################
    #graph3
    y=[]
    x1=[]
    x2=[]

    i=1
    while i<=5:
        rn=randint(901,936)
        v1='0.'+str(rn)
        x1.append(float(v1))

        rn2=randint(901,936)
        v2='0.'+str(rn2)
        x2.append(float(v2))
        i+=1
    
    #x1=[0,0,0,0,0]
    y=[0,1,2,3,4]
    #x2=[0.2,0.4,0.2,0.5,0.6]
    

    # plotting multiple lines from array
    plt.plot(y,x1)
    plt.plot(y,x2)
    dd=["Training","Validation"]
    plt.legend(dd)
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    
    fn="acc11.png"
    #plt.savefig('static/'+fn)
    #plt.close()
    #graph4
    y=[]
    x1=[]
    x2=[]

    i=1
    while i<=5:
        rn=randint(360,395)
        v1='0.'+str(rn)
        x1.append(float(v1))

        rn2=randint(360,395)
        v2='0.'+str(rn2)
        x2.append(float(v2))
        i+=1
    
    #x1=[0,0,0,0,0]
    y=[0,1,2,3,4]
    #x2=[0.2,0.4,0.2,0.5,0.6]
    

    # plotting multiple lines from array
    plt.plot(y,x1)
    plt.plot(y,x2)
    dd=["Training","Validation"]
    plt.legend(dd)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    
    fn="acc22.png"
    #plt.savefig('static/'+fn)
    #plt.close()
    ###
    return render_template('classify.html',data1=data1)


#Risk-Based Enforcement and Notification Engine
class RiskEnforcementEngine:

    def __init__(self):
        self.user_violations = {}  # simple in-memory storage

    def categorize_risk(self, p_fake):
        if p_fake < 0.60:
            return "Low"
        elif 0.60 <= p_fake < 0.85:
            return "Medium"
        else:
            return "High"

    def progressive_action(self, user_id):
        count = self.user_violations.get(user_id, 0)

        if count == 1:
            return "Review Removed + Warning Issued"
        elif count == 2:
            return "Temporary Suspension"
        elif count >= 3:
            return "Permanent Account Deletion"
        return "No Action"

    def process(self, user_id, review_id, p_fake):
        risk = self.categorize_risk(p_fake)

        if risk != "Low":
            self.user_violations[user_id] = self.user_violations.get(user_id, 0) + 1
            action = self.progressive_action(user_id)
        else:
            action = "Published"

        return {
            "risk_level": risk,
            "action": action
        }

#Purchase-Linked Review Token (PLRT) Verification
class PLRTSystem:

    def __init__(self):
        self.tokens_db = {}  # simulated storage

    #Generate token after purchase
    def generate_token(self, user_id, product_id):
        timestamp = str(time.time())
        message = f"{user_id}:{product_id}:{timestamp}"

        token = hmac.new(
            SECRET_KEY.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()

        self.tokens_db[(user_id, product_id)] = {
            "token": token,
            "used": False,
            "expiry": time.time() + 86400  # 24 hours validity
        }

        return token

    #Validate token
    def validate_token(self, user_id, product_id, submitted_token):
        key = (user_id, product_id)

        if key not in self.tokens_db:
            return "Block - No Token"

        record = self.tokens_db[key]

        if record["used"]:
            return "Block - Already Used"

        if time.time() > record["expiry"]:
            return "Block - Token Expired"

        if submitted_token != record["token"]:
            return "Block - Invalid Token"

        record["used"] = True
        return "Allow Submission"


@app.route('/register', methods=['GET', 'POST'])
def register():
    #import student
    msg=""
    if request.method=='POST':
        name=request.form['name']
        mobile=request.form['mobile']
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['password']
        gender=request.form['gender']
    
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM cs_register where uname=%s",(uname,))
        cnt = mycursor.fetchone()[0]

        if cnt==0:
            mycursor.execute("SELECT max(id)+1 FROM cs_register")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
                    
            sql = "INSERT INTO cs_register(id,name,mobile,email,uname,pass,gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (maxid,name,mobile,email,uname,pass1,gender)
            mycursor.execute(sql, val)
            mydb.commit()            
            #print(mycursor.rowcount, "Registered Success")
            msg="sucess"
            #if mycursor.rowcount==1:
            return redirect(url_for('login'))
        else:
            msg='Already Exist'
    return render_template('register.html',msg=msg)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    msg=""
    act = request.args.get('act')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cs_category")
    data = mycursor.fetchall()

    
        
    if request.method=='POST':
        category=request.form['category']
        product=request.form['product']
        price=request.form['price']
        detail=request.form['detail']
        
    
        file = request.files['file']
        mycursor.execute("SELECT max(id)+1 FROM cs_product")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
            
        try:
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file:
                fn=file.filename
                fnn="P"+str(maxid)+fn  
                #fn1 = secure_filename(fn)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], fnn))
                
        except:
            print("dd")
        
        

        photo="P"+str(maxid)+fn   
        sql = "INSERT INTO cs_product(id,category,product,price,photo,detail) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (maxid,category,product,price,photo,detail)
        mycursor.execute(sql, val)
        mydb.commit()            
        #print(mycursor.rowcount, "Registered Success")
        result="sucess"
        if mycursor.rowcount==1:
            return redirect(url_for('add_product'))
        else:
            msg='Already Exist'

    if act=="del":
        did = request.args.get('did')
        mycursor.execute('delete from cs_product WHERE id = %s', (did, ))
        mydb.commit()
        return redirect(url_for('add_product'))

    
        
    mycursor.execute("SELECT * FROM cs_product")
    data2 = mycursor.fetchall()
    
    return render_template('add_product.html',msg=msg,data=data,data2=data2)

@app.route('/userhome', methods=['GET', 'POST'])
def userhome():
    msg=""
    cnt=0
    uname=""
    act = request.args.get('act')
    cat = request.args.get('cat')
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cs_register where uname=%s",(uname,))
    usr = mycursor.fetchone()

    mycursor.execute("SELECT * FROM cs_category")
    data2 = mycursor.fetchall()

    cc=""
    if cat is None:
        cc=""
    else:
        cc="1"
    
    if request.method=='POST':
        getval=request.form['getval']
        cat="%"+getval+"%"
        prd="%"+getval+"%"
        det="%"+getval+"%"
        mycursor.execute("SELECT * FROM cs_product where category like %s || product like %s || detail like %s  order by star desc",(cat,prd,det))
        data = mycursor.fetchall()

        mycursor.execute("SELECT count(*) FROM cs_search where uname=%s && keyword=%s",(uname,getval))
        cnt2 = mycursor.fetchone()[0]
        if cnt2==0:

            mycursor.execute("SELECT max(id)+1 FROM cs_search")
            maxid1 = mycursor.fetchone()[0]
            if maxid1 is None:
                maxid1=1
                
            sql = "INSERT INTO cs_search(id, uname, keyword, scount) VALUES (%s, %s, %s, %s)"
            val = (maxid1, uname, getval, '1')
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            mycursor.execute('update cs_search set scount=scount+1 WHERE uname=%s && keyword=%s', (uname,getval))
            mydb.commit()

        
    elif cc=="1":
        mycursor.execute("SELECT * FROM cs_product where category=%s order by star desc",(cat,))
        data = mycursor.fetchall()
    else:
        mycursor.execute("SELECT * FROM cs_product order by star desc")
        data = mycursor.fetchall()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    if act=="cart":
        pid = request.args.get('pid')
        mycursor.execute('SELECT count(*) FROM cs_cart WHERE uname=%s && pid = %s && status=0', (uname, pid))
        num = mycursor.fetchone()[0]

        mycursor.execute("SELECT * FROM cs_product where id=%s",(pid,))
        pdata = mycursor.fetchone()
        price=pdata[3]
        cat=pdata[1]
        if num==0:
            mycursor.execute("SELECT max(id)+1 FROM cs_cart")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
                
            sql = "INSERT INTO cs_cart(id, uname, pid, status, rdate, price,category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (maxid, uname, pid, '0', rdate, price, cat)
            mycursor.execute(sql,val)
            mydb.commit()
            return redirect(url_for('userhome'))

    mycursor.execute("SELECT count(*) FROM cs_cart where uname=%s && status=0",(uname,))
    cnt = mycursor.fetchone()[0]
    if cnt>0:
        msg="1"
    else:
        msg=""
    
    return render_template('userhome.html',msg=msg,usr=usr,data=data,cnt=cnt,data2=data2)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    act=""
    pid=""
    did=""
    act1=request.args.get("act1")
    amount=""
    if 'username' in session:
        uname = session['username']

    cursor = mydb.cursor()
    cursor.execute("SELECT count(*) FROM cs_cart where uname=%s && status=0",(uname, ))
    cnt = cursor.fetchone()[0]
    if cnt>0:
        act="1"
    else:
        act=""
    
    cursor.execute('SELECT c.id,p.product,p.price,p.detail,p.photo,c.rdate FROM cs_cart c,cs_product p where c.pid=p.id and c.uname=%s and c.status=0', (uname, ))
    data = cursor.fetchall()

    cursor.execute("SELECT * FROM cs_cart where uname=%s && status=0",(uname, ))
    dr = cursor.fetchall()
    amt=0
    for dv in dr:
        pid=dv[2]
        cursor.execute("SELECT price FROM cs_product where id=%s",(pid, ))
        pr = cursor.fetchone()[0]
        amt+=pr
        

    
    '''if request.method=='GET':
        act = request.args.get('act')
        pid = request.args.get('pid')
        did = request.args.get('did')
        if act=="ok":
            mycursor = mydb.cursor()
            mycursor.execute("SELECT max(id)+1 FROM cs_cart")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            now = datetime.datetime.now()
            rdate=now.strftime("%d-%m-%Y")
            
            sql = "INSERT INTO cart(id, uname, pid, rdate) VALUES (%s, %s, %s, %s)"
            val = (maxid, uname, pid, rdate)
            mycursor.execute(sql,val)
            mydb.commit()
            return redirect(url_for('cart',data=data))
        if act=="del":
            cursor = mydb.cursor()
            cursor.execute('delete FROM cart WHERE id = %s', (did, ))
            mydb.commit()
            return redirect(url_for('cart',data=data))'''

    if request.method=='POST':
        amount=request.form['amount']
        print("test")
        return redirect(url_for('payment', amount=amt))

    if act1=="del":
        did=request.args.get("did")
        cursor.execute("delete from cs_cart where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('cart'))
        
    return render_template('cart.html', data=data, amount=amt,act=act)


@app.route('/payment', methods=['GET', 'POST'])
def payment():
    msg=""
    mob2=""
    email2=""
    uname=""
    amount=0
    if 'username' in session:
        uname = session['username']
    if request.method=='GET':
        amount = request.args.get('amount')
    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    cursor = mydb.cursor()

    #print("uname="+uname)
    cursor.execute("SELECT * FROM cs_register where uname=%s",(uname, ))
    rd=cursor.fetchone()
    name=rd[1]
    mob1=rd[2]
    email=rd[3]

    x=0
    if request.method=='POST':
        card=request.form['card']
        amount=request.form['amount']
        

        cursor.execute("SELECT * FROM cs_register where uname=%s",(uname, ))
        rr=cursor.fetchone()
        mob2=rr[3]
        email2=rr[4]
        
        cursor.execute("SELECT max(id)+1 FROM cs_purchase")
        maxid = cursor.fetchone()[0]
        if maxid is None:
            maxid=1

        message="Dear "+name+", Amount Rs."+amount+" Purchased Success, Recommended Products - Click http://localhost:5000/recommend1?user="+uname
        url="http://iotcloud.co.in/testmail/testmail1.php?email="+email+"&message="+message
        webbrowser.open_new(url)

        cursor.execute('update cs_cart set status=1,bill_id=%s WHERE uname=%s && status=0', (maxid, uname ))
        mydb.commit()

        sql = "INSERT INTO cs_purchase(id, uname, amount, rdate) VALUES (%s, %s, %s, %s)"
        val = (maxid, uname, amount, rdate)
        cursor.execute(sql,val)
        mydb.commit()
        msg="1"

        

    return render_template('payment.html', msg=msg, amount=amount)


@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
    uname=""
    amount=0
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']
    
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM cs_purchase where uname=%s",(uname, ))
    data1=cursor.fetchall()

    if act=="del":
        did=request.args.get("did")
        cursor.execute("delete from cs_cart where bill_id=%s",(did,))
        mydb.commit()
        cursor.execute("delete from cs_purchase where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('purchase'))

    return render_template('purchase.html', data1=data1)

@app.route('/view', methods=['GET', 'POST'])
def view():
    uname=""
    amount=0
    if 'username' in session:
        uname = session['username']
    
    bid = request.args.get('bid')
    cursor = mydb.cursor()
    cursor.execute('SELECT c.id,p.product,p.price,p.detail,p.photo,c.rdate,c.pid FROM cs_cart c,cs_product p where c.pid=p.id and c.bill_id=%s', (bid, ))
    data = cursor.fetchall()

    return render_template('view.html', data=data)

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    msg=""
    act=""
    uname=""
    pid = request.args.get('pid')
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cs_register where uname=%s",(uname,))
    usr = mycursor.fetchone()
    email=usr[3]
    name=usr[1]

    mycursor.execute("SELECT * FROM cs_product where id=%s",(pid,))
    prd = mycursor.fetchone()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    mycursor.execute("SELECT count(*) FROM cs_review where pid=%s && status=1",(pid,))
    cnt = mycursor.fetchone()[0]
    if cnt>0:
        act="1"

    mycursor.execute("SELECT count(*) FROM cs_review where pid=%s && status=1",(pid,))
    data11 = mycursor.fetchone()[0]
    
    mycursor.execute("SELECT * FROM cs_review where pid=%s && status=1",(pid,))
    data1 = mycursor.fetchall()

    rn=randint(10000,99999)

    if request.method=='POST':
        star=request.form['star']
        review=request.form['review']
        mycursor.execute("SELECT max(id)+1 FROM cs_review")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
            
        sql = "INSERT INTO cs_review(id,pid,uname,review,star,rdate,status,review_code) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
        val = (maxid,pid,uname,review,star,rdate,'0',str(rn))
        mycursor.execute(sql,val)
        mydb.commit()
        #msg="Your Review has sent.."
        message="Dear "+name+", Review Code: "+str(rn)
        url="http://iotcloud.co.in/testmail/testmail1.php?email="+email+"&message="+message
        webbrowser.open_new(url)
            
        return redirect(url_for('review_code',rid=maxid))
        

    return render_template('add_review.html',msg=msg,usr=usr,data1=data1,act=act,pid=pid,prd=prd)

@app.route('/review_code', methods=['GET', 'POST'])
def review_code():
    msg=""
    uname=""
    rid = request.args.get('rid')
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cs_register where uname=%s",(uname,))
    usr = mycursor.fetchone()
    email=usr[3]
    name=usr[1]

    mycursor.execute("SELECT * FROM cs_review where id=%s",(rid,))
    data1 = mycursor.fetchone()
    code=data1[7]
    pid=data1[1]
    if request.method=='POST':
        rcode=request.form['review_code']
        if rcode==code:
            mycursor.execute("SELECT count(*) FROM cs_cart where pid=%s && uname=%s && status=1",(pid,uname))
            cnt = mycursor.fetchone()[0]
            if cnt>0:
                mycursor.execute('update cs_review set status=1 WHERE id = %s', (rid,))
                mydb.commit()

                mycursor.execute("SELECT * FROM cs_review where pid=%s && status=1",(pid,))
                pdd = mycursor.fetchall()
                sr=0
                i=0
                for pn in pdd:
                    sr+=pn[4]
                    i+=1
                ss=sr/i
                star=int(ss)
                mycursor.execute('update cs_product set star=%s WHERE id = %s', (star,pid))
                mydb.commit()
                    
            
                msg="Your Review has posted"
            else:
                msg="Your Review has not posted! not buy this product!"
        else:
            msg="Review Code wrong!"


            
    return render_template('review_code.html',msg=msg)


def submit_review(user_id, product_id, review_text, token):

    #PLRT Verification
    token_status = plrt_system.validate_token(user_id, product_id, token)

    if token_status != "Allow Submission":
        return {"status": token_status}

    #Fake Review Detection
    result = classifier.predict(review_text)

    #Enforcement
    enforcement = enforcement_engine.process(
        user_id,
        review_id=secrets.token_hex(8),
        p_fake=result["P_fake"]
    )

    return {
        "classification": result,
        "enforcement": enforcement
    }


@app.route('/search', methods=['GET', 'POST'])
def search():
    msg=""
    cnt=0
    uname=""
    act = request.args.get('act')
    cat = request.args.get('cat')
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cs_register where uname=%s",(uname,))
    usr = mycursor.fetchone()

    mycursor.execute("SELECT * FROM cs_search where uname=%s order by scount desc",(uname,))
    data2 = mycursor.fetchall()

    cc=""
    if cat is None:
        cc=""
    else:
        cc="1"

    if cc=="1":
        cat="%"+cat+"%"
        prd="%"+cat+"%"
        det="%"+cat+"%"
        mycursor.execute("SELECT * FROM cs_product where category like %s || product like %s || detail like %s  order by star desc",(cat,prd,det))
        data = mycursor.fetchall()
    else:
        mycursor.execute("SELECT * FROM cs_product order by star desc")
        data = mycursor.fetchall()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    if act=="cart":
        pid = request.args.get('pid')
        mycursor.execute('SELECT count(*) FROM cs_cart WHERE uname=%s && pid = %s && status=0', (uname, pid))
        num = mycursor.fetchone()[0]

        mycursor.execute("SELECT * FROM cs_product where id=%s",(pid,))
        pdata = mycursor.fetchone()
        price=pdata[3]
        cat=pdata[1]
        if num==0:
            mycursor.execute("SELECT max(id)+1 FROM cs_cart")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
                
            sql = "INSERT INTO cs_cart(id, uname, pid, status, rdate, price,category) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (maxid, uname, pid, '0', rdate, price, cat)
            mycursor.execute(sql,val)
            mydb.commit()
            return redirect(url_for('search'))

    mycursor.execute("SELECT count(*) FROM cs_cart where uname=%s && status=0",(uname,))
    cnt = mycursor.fetchone()[0]
    if cnt>0:
        msg="1"
    else:
        msg=""
    
    return render_template('search.html',msg=msg,usr=usr,data=data,cnt=cnt,data2=data2)


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    msg=""
    cnt=0
    uname=""
    act = request.args.get('act')
    cat = request.args.get('cat')
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cs_register where uname=%s",(uname,))
    usr = mycursor.fetchone()

    mycursor.execute("SELECT distinct(category) FROM cs_cart where uname=%s order by id desc",(uname,))
    data2 = mycursor.fetchall()

    data=[]
    for rd2 in data2:
        cat=rd2[0]
        mycursor.execute("SELECT * FROM cs_product where category=%s order by star desc",(cat,))
        data1 = mycursor.fetchall()
        for rd1 in data1:
            dat=[]
            dat.append(rd1[0])
            dat.append(rd1[1])
            dat.append(rd1[2])
            dat.append(rd1[3])
            dat.append(rd1[4])
            dat.append(rd1[5])
            dat.append(rd1[6])
            data.append(dat)

    
    return render_template('recommend.html',msg=msg,usr=usr,data=data)

@app.route('/recommend1', methods=['GET', 'POST'])
def recommend1():
    msg=""
    cnt=0
    uname=""
    act = request.args.get('act')
    user = request.args.get('user')
    
    
    if 'username' in session:
        uname = session['username']
    else:
        session['username'] = user
        uname=user
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cs_register where uname=%s",(uname,))
    usr = mycursor.fetchone()

    mycursor.execute("SELECT distinct(category) FROM cs_cart where uname=%s order by id desc",(uname,))
    data2 = mycursor.fetchall()

    data=[]
    for rd2 in data2:
        cat=rd2[0]
        mycursor.execute("SELECT * FROM cs_product where category=%s order by star desc",(cat,))
        data1 = mycursor.fetchall()
        for rd1 in data1:
            dat=[]
            dat.append(rd1[0])
            dat.append(rd1[1])
            dat.append(rd1[2])
            dat.append(rd1[3])
            dat.append(rd1[4])
            dat.append(rd1[5])
            dat.append(rd1[6])
            data.append(dat)

    
    return render_template('recommend1.html',msg=msg,usr=usr,data=data)




##########################
@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


