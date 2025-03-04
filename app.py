from flask import Flask, request, jsonify # type: ignore
from imdb import IMDb # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend access

# IMDb instance
ia = IMDb()

@app.route('/get-rating', methods=['GET'])
def get_movie_rating():
    movie_name = request.args.get('movie')
    
    if not movie_name:
        return jsonify({"error": "Movie name is required"}), 400

    movies = ia.search_movie(movie_name)

    if movies:
        movie = movies[0]  # Taking the first search result
        ia.update(movie)
        rating = movie.get('rating', 'N/A')  # Fetch the rating, default to 'N/A' if not found

        return jsonify({"title": movie['title'], "rating": rating})
    
    return jsonify({"error": "Movie not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
