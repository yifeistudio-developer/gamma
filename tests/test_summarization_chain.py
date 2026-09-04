import pytest
import logging
from gamma.research_engine_chain import summarization_chain
from gamma.assistant_instructions_chain import assistant_instructions_chain

log = logging.getLogger(__name__)
@pytest.mark.parametrize('question', ['What can I see and do in the Hangzhou of China?'])
def test_summarization_chain(question: str):
    result = summarization_chain.invoke(question)
    log.info('result %s', result)
