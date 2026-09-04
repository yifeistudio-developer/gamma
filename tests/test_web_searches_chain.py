import pytest
from gamma.web_searches_chain import web_searches_chain
import logging

log = logging.getLogger(__name__)

@pytest.mark.parametrize("question, instructions", [
    ('What can I see and do in the Hangzhou of China?', 
     {
        'assistant_type': 'Tour guide assistant', 
        'assistant_instructions': 'You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights.', 
        'user_question': 'What can I see and do in the Hangzhou of China?'
    })])
def test_web_search_chain(question, instructions):
    result = web_searches_chain.invoke({'user_question': question, 'assistant_instructions': instructions})
    log.info("Result: %s", result)
