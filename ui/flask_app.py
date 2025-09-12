from flask import Flask, request, render_template
from recommender import Recommender

app = Flask(__name__)
recommender = Recommender()

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    query = ""
    if request.method == 'POST':
        query = request.form.get("What Kind of Ted Talk Are You Looking For?", "")
        if query:
            recommendations = recommender.recommend(query, top_k=5)
    return render_template("index.html", query=query, recommendations=recommendations)


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=2509, debug=True)