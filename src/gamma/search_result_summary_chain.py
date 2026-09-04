from gamma.utilties import to_obj
from gamma.web_scraping import web_scrap
from gamma.llm_models import get_llm
from gamma.prompts import SUMMARY_PROMPT_TEMPLATE
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

RESULT_TEXT_MAX_CHARACTERS = 1000

search_result_summary_chain = (
    RunnableLambda(lambda x: {
        'search_query': x['search_query'],
        'search_result_text': web_scrap(url=x['result_url'])[:RESULT_TEXT_MAX_CHARACTERS],
        'result_url': x['result_url'],
        'user_question': x['user_question']
    }) | RunnableParallel(
        {
            'text_summary': SUMMARY_PROMPT_TEMPLATE | get_llm() | StrOutputParser(),
            'result_url': lambda x: x['result_url'],
            'user_question': lambda x: x['user_question']
        }
    ) | RunnableLambda(lambda x: {
        'summary': f"Source Url: {x['result_url']}\nSummary: {x['text_summary']}",
        'user_question': x['user_question']
    })
)