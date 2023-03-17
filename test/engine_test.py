from search.engine import Engine


def test_engine():
    search_engine = Engine()
    # Index documents
    search_engine.index(1, {"text:": "The cat is on the mat"})
    search_engine.index(2, {"text:": "My dog and cat are the best"})
    search_engine.index(3, {"text:": "The locals are playing"})
    # Perform a search
    results = list(search_engine.search("The cat"))

    assert len(results) == 2
    assert results[0]["score"] == 0.06757751801802739
