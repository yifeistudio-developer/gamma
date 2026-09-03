from gamma.research_engine_seq import research

def test_research_engine_seq():
    question = 'What can I see and do in the Spanish town of Astorga?'
    research_report = research(question)
    assert isinstance(research_report, str)
