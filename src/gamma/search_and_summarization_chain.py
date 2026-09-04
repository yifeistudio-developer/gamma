from gamma.search_result_urls_chain import search_result_urls_chain
from gamma.search_result_summary_chain import search_result_summary_chain

from langchain_core.runnables import RunnableLambda

search_and_summarization_chain = (
    search_result_urls_chain
    | search_result_summary_chain.map()
    | RunnableLambda(lambda x: {
        'summary': '\n'.join([i['summary'] for i in x]),
        'user_question': x[0]['user_question'] if len(x) > 0 else ''
    })
)