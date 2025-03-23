import streamlit as st
from model import recommend

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name:
        recommended_movies = recommend(movie_name)
        st.write("🎥 **Recommended Movies:**")
        for movie in recommended_movies:
            st.write(f"✅ {movie}")
    else:
        st.write("⚠️ Please enter a movie name.")
