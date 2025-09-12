from flask import Flask, request, render_template
from recommender import Recommender

app = Flask(__name__)

recommender = Recommender()

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    query = ""
    if request.method == 'POST':
        query = request.values.get("query", "").strip()
        print("DEBUG: Form data =", request.form)
        print("DEBUG: Query =", query)
        
        if query:
            recommendations = recommender.recommend(query, top_k=5)
            print("DEBUG:", recommendations)
    return render_template("index.html", query=query, recommendations=recommendations)


if __name__ =="__main__":
    app.run(host='0.0.0.0', port=2509, debug=True)