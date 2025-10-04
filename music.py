# music.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv(r"C:\Users\SHUBHANGI\Desktop\archive (2)\top 100 streamed_songs.csv")

# Clean data
data = data.dropna(subset=['name', 'id'])
data = data.drop_duplicates(subset=['name'])

# TF-IDF features
data['Song_Features'] = data['name']
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['Song_Features'])
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_songs(song_name, top_n=5):
    # Case-insensitive substring match to find matching songs
    matches = data[data['name'].str.contains(song_name, case=False, na=False)]
    if matches.empty:
        return [{"error": f"❌ '{song_name}' not found in the dataset."}]

    # Use the first matched song for recommendations
    matched_song_name = matches.iloc[0]['name']
    idx = data[data['name'] == matched_song_name].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    final_indices = [i for i, score in sim_scores]

    results = []
    for i in final_indices:
        results.append({
            "name": data.iloc[i]['name'],
            "id": data.iloc[i]['id'],
            "duration": data.iloc[i]['duration'],
            "energy": f"{int(data.iloc[i]['energy'] * 100)}%",
            "danceability": f"{int(data.iloc[i]['danceability'] * 100)}%",
            "tempo": f"{int(data.iloc[i]['tempo'])}"
        })
    return results

