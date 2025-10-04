from flask import Flask, render_template, request
from music import recommend_songs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    query = ""
    if request.method == 'POST':
        query = request.form['song_name']
        recommendations = recommend_songs(query)
    return render_template('index.html', recommendations=recommendations, query=query)

if __name__ == '__main__':
    app.run(debug=True)
