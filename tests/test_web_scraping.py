from gamma.web_scraping import web_scrap

def test_web_scraping():
    webpage_text = web_scrap("https://en.wikipedia.org/wiki/List_of_career_achievements_by_Michael_Jordan")
    assert "Michael Jordan" in webpage_text