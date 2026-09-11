from langgraph.graph import StateGraph, END
from gamma.graph.states import ResearchState
from gamma.graph.node_functions import (
    select_assistant,
    generate_search_queries,
    perform_web_searches,
    summarize_search_results,
    evaluate_search_relevance,
    write_research_report
)

graph = StateGraph(ResearchState)

graph.add_node('select_assistant', select_assistant)
graph.add_node('generate_search_queries', generate_search_queries)
graph.add_node('perform_web_searches', perform_web_searches)
graph.add_node('summarize_search_results', summarize_search_results)
graph.add_node('evaluate_search_relevance', evaluate_search_relevance)
graph.add_node('write_research_report', write_research_report)

def route_based_on_relevance(state):
    iteration_count = state.get('iteration_count', 0) + 1
    state['iteration_count'] = iteration_count
    if iteration_count >= 3:
        return 'write_research_report'
    if state.get('should_regnerate_queries', False):
        return 'generate_search_queries'
    return 'write_research_report'

graph.set_entry_point('select_assistant')

graph.add_edge('select_assistant', 'generate_search_queries')
graph.add_edge('generate_search_queries', 'perform_web_searches')
graph.add_edge('perform_web_searches', 'summarize_search_results')
graph.add_edge('summarize_search_results', 'evaluate_search_relevance')

graph.add_conditional_edges('evaluate_search_relevance', 
                            route_based_on_relevance, 
                            {
                                'generate_search_queries': 'generate_search_queries',
                                'write_research_report': 'write_research_report'
                            })


graph.add_edge('write_research_report', END)

app = graph.compile()
initial_state = {
    'user_question': "What can you tell me about Astorga's roman spas?",
    'assistant_info': None,
    'search_queries': None,
    'search_results': None,
    'search_summaries': None,
    'final_report': None,
    'used_fallback_search': False,
    'relevance_evaluation': None,
    'should_regenerate_queries': None,
    'iteration_count': 0
}

result = app.invoke(initial_state)
final_report = result['final_report']