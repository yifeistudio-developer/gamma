from gamma.llm_models import get_llm
from gamma.prompts import ASSISTANT_SELECTION_PROMPT_TEMPLATE
from langchain_core.runnables import RunnablePassthrough
from gamma.utilties import to_obj
from langchain_core.output_parsers import StrOutputParser

assistant_instructions_chain = (
    {'user_question': RunnablePassthrough()}
    | ASSISTANT_SELECTION_PROMPT_TEMPLATE
    | get_llm()
    | StrOutputParser() | to_obj
)
