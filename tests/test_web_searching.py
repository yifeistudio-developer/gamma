from gamma.web_searching import web_search


def test_web_search():
    result = web_search(web_query='How many titles did Michael Jordan win?', num_results=5)
    assert isinstance(result, list)
    assert len(result) == 5
