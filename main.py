from flask import Flask, jsonify, request

from storage import all_movies, liked_movies, not_liked_movies, did_not_watch
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
   

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch_view():
    

@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    for movie in output:
        _d = {
           
        }
        movie_data.append(_d)
    return jsonify({
        
@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for liked_movie in liked_movies:
        output = get_recommendations(liked_movie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "poster_link": recommended[1],
            "release_date": recommended[2] or "N/A",
            "duration": recommended[3],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()
