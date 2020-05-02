# Anime Recommendation App!

## 1. Introduction 

This recomendation app was made by using user data from myanimelist untill 2018. Their scores were used to create a sparse matrix against all anime they scored.
Unfortunatly the sheer amount of score was that I could not take all anime that were scored. All anime that had less then 50 scores were cut from the matrix.
This was done due to technical limitations. Though it fully functional on my localhost I unfortunantly could not get it to function on Heroku. 

## 2. Prerequisites
Before launching the app specific packages are required. You can find the required packages in the *requirements.txt* and the used python version in the *runtime.txt* file. The Procfile is used by Heroku and can be ignored.

## 3. Activation

To run the app locally on Windows use the command:

`waitress-serve app:app` 

To use it on UNIX, install gunicorn and run the command:

`gunicorn app:app`

## 4.'Features'

Currently the app only runs on the japanese titles. The Fuzzywuzzy algorithm is a bit strict so it can have issues with frequently used anime words such as *Gundam*.

### 5. Author
  - Gilian Brouwer
 
### 6. Ackowledgements

Big thanks to W3 for their css code and html format.
Many thanks to Nikita Sharma's [article](https://heartbeat.fritz.ai/recommender-systems-with-python-part-ii-collaborative-filtering-k-nearest-neighbors-algorithm-c8dcd5fd89b2) on the use of KNN.
