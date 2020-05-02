# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:15:16 2020

@author: Gebruiker
"""
from flask import Flask, render_template
import pandas as pd

anime=pd.read_csv('anime2.csv',  usecols= ['anime_id', 'title', 'title_english', 'genre'])

app = Flask(__name__)

@app.route('/', methods=['GET'])
def my_form():
    return render_template('index.html')

@app.route('/',methods=['GET', 'POST'])
    
def recommender():
    
    recommer=anime.head()
        
    recani='Zero no Tsukaima'
    
    return render_template('index.html',  recani=recani, tables=[recommer.to_html(classes='data')], titles=recommer.columns.values)

if __name__ == "__main__":
    app.run()


