import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
moviesnew=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index=moviesnew[moviesnew['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(moviesnew['title'][i[0]])
    return recommended_movies


st.title('Movie Recommender System') 

movie_name=st.selectbox("Select Movie",moviesnew['title'].values)

if(st.button('Recommend')):
    recommendations=recommend(movie_name)
    for i in recommendations:
        st.write(i)