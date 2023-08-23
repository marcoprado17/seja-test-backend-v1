import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from utils import get_response

load_dotenv()

if 'llm' not in st.session_state:
    st.session_state['llm'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] =[]
if 'agent' not in st.session_state:
    st.session_state['agent'] = None

st.set_page_config(page_title="Assistente de mapas da cidade de São Paulo", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Assistente de mapas da cidade de São Paulo</h1>", unsafe_allow_html=True)

response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Entre com o texto:", key='input', height=100)
        submit_button = st.form_submit_button(label='Enviar')

        if submit_button:
            model_response=get_response(user_input)
            st.session_state['messages'].append(user_input)
            st.session_state['messages'].append(model_response)

            with response_container:
                for i in range(len(st.session_state['messages'])):
                        if (i % 2) == 0:
                            message(st.session_state['messages'][i], is_user=True, key=str(i) + '_user')
                        else:
                            message(st.session_state['messages'][i], key=str(i) + '_AI')
