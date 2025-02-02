from haystack.nodes import WebSearch

def test_web_search():
    web_search = WebSearch(api_key=None, engine="duckduckgo")
    results = web_search.run(query="alternance France")
    for result in results["documents"]:
        print(f"Titre : {result.meta.get('title')}")
        print(f"Description : {result.content}")
        print(f"URL : {result.meta.get('link')}")
        print("---")

if __name__ == '__main__':
    test_web_search()