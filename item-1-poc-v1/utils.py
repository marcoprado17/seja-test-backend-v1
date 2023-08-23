import streamlit as st
from langchain import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
# TODO: Find a way to avoid token overflow and keep track of the conversation
from langchain.prompts.prompt import PromptTemplate

def get_response(user_input):

    if st.session_state['conversation'] is None:

        # TODO: Use an open source LLM
        llm = OpenAI(
            temperature=0.1,
            model_name='text-davinci-003'
        )

        template = """O texto a seguir é uma conversa amigável em portugês (Brasil) entre um humano e uma assistente AI. Se a assistente AI não souber a resposta a pergunta, ela diz que não sabe.

Conversa atual:
{history}
Humano: {input}
Assistente AI:"""
        PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)

        st.session_state['conversation'] = ConversationChain(
            prompt=PROMPT,
            llm=llm,
            verbose=True,
            memory=ConversationBufferMemory(
              llm=llm,
              ai_prefix="Assistente AI",
              human_prefix="Humano",
            )
        )

    response=st.session_state['conversation'].predict(input=user_input)
    
    print(st.session_state['conversation'].memory.buffer)

    return response
