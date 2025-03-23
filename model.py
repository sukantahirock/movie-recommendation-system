import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv('dataset.csv')


# Handling missing values
movies.fillna('', inplace=True)

# Create a 'tags' column combining genre and overview
movies['tags'] = movies['genre'] + " " + movies['overview']

# Select necessary columns
new_df = movies[['id', 'title', 'tags']]

# Text vectorization
cv = CountVectorizer(max_features=10000, stop_words='english')
vec = cv.fit_transform(new_df['tags'].values.astype('U')).toarray()

# Compute cosine similarity
sim = cosine_similarity(vec)


# Recommendation function
def recommend(movie_title):
    if movie_title not in new_df['title'].values:
        return ["Movie not found!"]

    index = new_df[new_df['title'] == movie_title].index[0]
    distances = sorted(list(enumerate(sim[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [new_df.iloc[i[0]].title for i in distances]
    return recommended_movies
print(recommend("Iron Man"))
