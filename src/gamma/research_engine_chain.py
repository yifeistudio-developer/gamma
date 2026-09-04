from gamma.assistant_instructions_chain import assistant_instructions_chain
from gamma.web_searches_chain import web_searches_chain
from gamma.search_and_summarization_chain import search_and_summarization_chain
from gamma.prompts import RESEARCH_REPORT_PROMPT_TEMPLATE
from langchain_core.runnables import RunnableLambda
from gamma.llm_models import get_llm
from gamma.utilties import to_obj
from langchain_core.output_parsers import StrOutputParser

summarization_chain = (assistant_instructions_chain 
                        | web_searches_chain
                        | search_and_summarization_chain.map()
                        | RunnableLambda(lambda x: {
                           'research_summary': '\n'.join([r['summary'] for r in x]),
                           'user_question': x[0]['user_question'] if len(x) > 0 else 0})
                        | RESEARCH_REPORT_PROMPT_TEMPLATE | get_llm() | StrOutputParser() | to_obj)