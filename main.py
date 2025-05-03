import streamlit as st
from model import model

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from prompts import INITIAL_MESSAGE, BREIF_TOPIC, DETAILED_TOPIC

messages = []

programming_language = st.sidebar.selectbox(
    'Select Language!',
    ('Python', 'Javascript', 'Go')
)

explanation_type = st.sidebar.radio(
     "Explanation type",
     ["Breif", "Detailed"]
 )

prompts = ChatPromptTemplate.from_messages([
    ("system", INITIAL_MESSAGE )
])

system_prompt = prompts.invoke({"language" : programming_language})
messages.append(system_prompt.to_string())



human_message = st.chat_input("Ask any topic you want to learn")

if(human_message):
    with st.chat_message("user"):
     st.write(human_message)
    human_prompt = ChatPromptTemplate.from_template(BREIF_TOPIC if explanation_type == 'Breif' else DETAILED_TOPIC).invoke({"topic" : human_message, "language" : programming_language})
    messages.append(human_prompt.to_string())

    result = model.invoke(messages)

    messages.append(AIMessage(result))

    with st.chat_message("ai"):
     st.write(result)







