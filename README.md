# Music Recommender Website

A modern, AI-powered music recommendation web application that suggests songs based on user input using content-based filtering and cosine similarity.

## Features

- **Song Search & Recommendations**: Enter a song name to get personalized recommendations
- **Content-Based Filtering**: Uses TF-IDF vectorization and cosine similarity on song names
- **Beautiful UI**: Responsive design with glass morphism effects, animations, and interactive elements
- **Song Statistics**: Displays duration, energy, danceability, and tempo for each recommendation
- **Interactive Cards**: Clickable song cards with play/pause animations
- **Filtering Options**: Mood-based filtering and customizable energy/danceability sliders

## Technologies Used

- **Backend**: Python, Flask
- **Data Processing**: Pandas, Scikit-learn
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Dataset**: Top 100 streamed songs CSV

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/music_recommender_website.git
   cd music_recommender_website
   ```

2. Install Python dependencies:
   ```bash
   pip install flask pandas scikit-learn
   ```

3. Ensure the dataset file `top 100 streamed_songs.csv` is in the project root.

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter a song name in the search box and click "Get Recommendations"

4. Browse through the recommended songs with their statistics

## Dataset

The application uses a dataset of top 100 streamed songs with features including:
- Song name
- Artist ID
- Duration
- Energy level
- Danceability
- Tempo (BPM)

## How It Works

1. **Data Loading**: Loads and cleans the song dataset
2. **Feature Extraction**: Creates TF-IDF vectors from song names
3. **Similarity Calculation**: Computes cosine similarity between songs
4. **Recommendation**: Finds songs most similar to the user's input
5. **Display**: Presents recommendations in an interactive web interface

## Project Structure

```
music_recommender_website/
├── app.py                 # Main Flask application
├── music.py               # Recommendation logic
├── test_music.py          # Unit tests
├── top 100 streamed_songs.csv  # Dataset
├── static/
│   └── style.css          # Additional styles (if any)
├── templates/
│   └── index.html         # Main web page
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Dataset source: Top 100 streamed songs
- UI inspiration: Modern web design trends
- Libraries: Flask, Pandas, Scikit-learn, Bootstrap
