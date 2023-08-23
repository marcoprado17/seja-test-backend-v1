import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
# TODO: Find a way to avoid token overflow and keep track of the conversation
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import CTransformers
from langchain import OpenAI
import consts
import os

def _get_llm():
    llm_type = os.environ['LLM_TYPE']

    if llm_type == consts.OPENAI_LLM_TYPE:
        return OpenAI(
            temperature=0.1,
            model_name=os.environ['OPENAI_LLM_MODEL_NAME']
        )
    elif llm_type == consts.LOCAL_LLAMA_LLM_TYPE:
        return CTransformers(
            model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
            model_type='llama',
            config={
                'max_new_tokens': 1024,
                'temperature': 0.01
            }
        )
    else:
        raise Exception("Invalid LLM type")

def get_response(user_input):

    if st.session_state['conversation'] is None:
        llm = _get_llm()

        template = """O texto a seguir é uma conversa amigável em portugês (Brasil) entre um humano e uma assistente AI. Se a assistente AI não souber a resposta à pergunta, ela diz que não sabe. A assistente deve completar o texto respondendo uma única vez. A assistente não deve escrever o texto do humano.

Conversa atual:
{history}
Humano: {input}
A próxima resposta da assistente AI é: """
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
