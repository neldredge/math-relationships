from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search/<query>')
def search(query):
    mathematicians = [
        {"id": 1, "name": 'Tatyana Afanasyeva'},
        {"id": 2, "name": 'Maria Gaetana Agnesi '},
        {"id": 3, "name": 'Agnes Sime Baxter'},
        {"id": 4, "name": 'Nicole Berline'},
        {"id": 5, "name": 'Christine Darden'}]

    results = {
        "results": [m for m in mathematicians if query.lower() in m["name"].lower()]
    }

    return jsonify(results)


@app.route('/relationship/<a>/<b>')
def relationship(a, b):
    results = {
        "a": [
            {"id": 1, "name": 'The Common Ancestor'},
            {"id": 2, "name": 'An Ancestor'},
            {"id": 3, "name": 'Another Ancestor'}],
        "b": [
            {"id": 1, "name": 'The Common Ancestor'},
            {"id": 2, "name": 'Some Ancestor'},
            {"id": 3, "name": 'Some Other Ancestor'},
            {"id": 3, "name": 'Yet Another Ancestor'}]
    }

    return jsonify(results)

if __name__ == "__main__":
    app.run()
