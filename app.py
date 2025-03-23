from flask import Flask, request, jsonify
from model import recommend

app = Flask(__name__)


@app.route('/recommend', methods=['GET'])
def get_recommendation():
    movie_name = request.args.get('movie')
    recommended = recommend(movie_name)

    return jsonify({'recommendations': recommended})


if __name__ == '__main__':
    app.run(debug=True)
