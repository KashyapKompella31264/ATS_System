from src.scoring.semantic_score import semantic_search

def test_scemantic_search():
    results=semantic_search(10)
    for result in results:
        print(result)


if __name__=="__main__":
    test_scemantic_search()