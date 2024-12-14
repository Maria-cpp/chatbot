import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAsd9AE90gxmyHsrziKLl_7MxTCJLWWWMQ")
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

#Display Form title 
st.title("Chat with Google Gemini")


def role_to_streamlit(role):
     if role == "model":
          return "assistant"
     else:
          return role

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        


if prompt := st.chat_input("What can I do for you?"):
    st.chat_message("user").markdown(prompt)
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
	    st.markdown(response.text)


