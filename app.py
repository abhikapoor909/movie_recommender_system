import streamlit as st
import pickle
import pandas as pd
movies_dict=pickle.load(open("movie_list_dict.pkl",'rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
        
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

st.title("Movie Recommender System")



option = st.selectbox(
    "Select the movie",
    (movies["title"].values)
    

)

if st.button("Recommend"):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
