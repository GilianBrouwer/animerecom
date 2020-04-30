# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:15:16 2020

@author: Gebruiker
"""
from flask import Flask, render_template, request
import pandas as pd
from fuzzywuzzy import fuzz
from sklearn.neighbors import NearestNeighbors



df2 = pd.read_parquet('data/matrix.parquet')
anime=pd.read_csv('anime2.csv',  usecols= ['anime_id', 'title', 'title_english', 'genre'])
model_knn=NearestNeighbors(metric='cosine', algorithm='brute')

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/',methods=['POST'])
    
def recommender():
    my_favorite = request.form['text']

    def fuzzy_ratio(mapper, fav_anime, verbose=True):
        sugtitle=[]
        indk=-1
        for i in mapper.title:
            ratio=fuzz.ratio(i, my_favorite)
            indk= indk+1
            if ratio > 60:
                sugtitle.append((i,indk, ratio))
        sugtitle = sorted(sugtitle, key=lambda x: x[2])[::-1]
        return sugtitle[0][1]
    
    def make_recommendation(model_knn, data, mapper, fav_anime, n_recommendations):
        # fit
        model_knn.fit(data)
        # get input anime
        idx = fuzzy_ratio(mapper, fav_anime, verbose=True)
        distances, indices = model_knn.kneighbors(data.iloc[idx, :].values.reshape(1, -1), n_neighbors=n_recommendations+1)
        # print recommendations
        ind= indices.tolist()
        dist=sorted(list(zip(distances.tolist(), indices.tolist())))
        ds=pd.DataFrame(dist[0]).transpose()
        recom = mapper.iloc[ind[0], :]
        
        ds[1]=ds[1].astype('int64')
        recom=recom.reset_index(drop=True)
        
        recommer= pd.concat([recom, ds], axis=1)
        recani=recommer.loc[0, 'title']
        recommer= recommer.drop([0])
        recommer=recommer.sort_values(by=[0], ascending=False)
        recommer=recommer.drop([0, 1], axis=1)
        recommer=recommer.rename(columns={'anime_id': 'ID', 'title' : 'Title', 'title_english' : 'English Title', 'genre' : 'Genre'})
        recommer=recommer.set_index('Title')
        
        return recani, recommer
    
        
    recani, recommer=make_recommendation(
        model_knn=model_knn,
        data=df2,
        fav_anime=my_favorite,
        mapper=anime,
        n_recommendations=5)
    
    return render_template('index.html',  recani=recani, tables=[recommer.to_html(classes='data')], titles=recommer.columns.values)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

