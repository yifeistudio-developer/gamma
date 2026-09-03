from gamma.assistant_instructions_chain import assistant_instructions_chain

def test_assistant_instructions_chain():
    question = 'What can I see and do in the Spanish town of Astorga?'
    instructions = assistant_instructions_chain.invoke({'user_question': question})
    assert isinstance(instructions, dict)