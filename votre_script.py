from flask import Flask, render_template
from haystack.nodes import WebSearch

app = Flask(__name__)

def search_alternance_offers():
    # Initialiser WebSearch sans l'argument 'engine'
    web_search = WebSearch(api_key=None)  # Pas besoin de clé API

    # Effectuer une recherche
    query = "alternance France"
    results = web_search.run(query=query)

    # Formater les résultats
    offers = []
    for result in results["documents"]:
        offers.append({
            "title": result.meta.get("title", "Sans titre"),
            "description": result.content,
            "url": result.meta.get("link", "#"),
        })

    return offers

@app.route('/')
def home():
    offers = search_alternance_offers()
    return render_template('index.html', offers=offers)

if __name__ == '__main__':
    app.run(debug=True)