import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data
df = pd.read_csv("movies.csv")

# Convert genres to lowercase
df['genres'] = df['genres'].str.lower()

# TF-IDF Vectorization on genres
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['genres'])

# Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix)

# Function to get recommendations
def recommend(movie_title, top_n=3):
    idx = df[df['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Example usage
movie = "Inception"
print(f"Recommended for '{movie}':")
print(recommend(movie))
