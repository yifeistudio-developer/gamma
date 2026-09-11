from gamma.prompts import (
    ASSISTANT_SELECTION_PROMPT_TEMPLATE,
    WEB_SEARCH_PROMPT_TEMPLATE,
    
)
from gamma.llm_models import get_llm
from gamma.web_scraping import web_scrap
from gamma.utilties import to_obj
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

def select_assistant(state: dict) -> dict:
    """Select the appropriate research assistant."""
    user_question = state['user_question']
    prompt = ASSISTANT_SELECTION_PROMPT_TEMPLATE.format(user_question=user_question)
    response = get_llm().invoke(prompt)
    assistant_info = to_obj(response.content)
    return {
        'assistant_info': assistant_info
    }


def generate_search_queries(state: dict) -> dict:
    """Generate search queries based on the question."""
    assistant_info = state['assistant_info']
    user_question = state['user_question']
    prompt = WEB_SEARCH_PROMPT_TEMPLATE.format(user_question=user_question, assistant_info=assistant_info['assistant_instructions'], num_search_queries=3)
    response = get_llm().invoke(prompt)
    search_queries = to_obj(response.content)
    return {
        'search_queries': search_queries
    }

def perform_web_searches(state: dict) -> dict:
    MAX_LEN = 1000
    search_queries = state['search_queries']
    user_question = state['user_question']


    chain = (
        RunnableParallel({
            'summary': {
                'search_result_text': lambda x: web_scrap(url=x['url'][:MAX_LEN]),
                'search_query': lambda x: x['search_query']
            } | get_llm() | StrOutputParser(),
            'user_question': user_question,
            'result_url':lambda x: x['url']
        }).map()
    )
    response = chain.invoke(search_queries)
    return {
        'search_results': response
    }


def summarize_search_results(state: dict) -> dict:

    return {

    }


def evaluate_search_relevance(state: dict) -> dict:

    return {

    }

def write_research_report(state: dict) -> dict:

    return {

    }