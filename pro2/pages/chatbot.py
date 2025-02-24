import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Check out my fun YouTube channel 'CodeVerse': https://www.youtube.com/@my_codeverse",
            "Hi! What's up? It's Great, Don't forget to subscribe to 'CodeVerse':https://www.youtube.com/@my_codeverse",
            "Hello! Need assistance? My YouTube channel 'CodeVerse' is full of great tips: https://www.youtube.com/@my_codeverse",
            "Hey! Got a question? Also, subscribe to 'CodeVerse' for awesome tutorials: https://www.youtube.com/@my_codeverse",
            "Hi there! How can I help? BTW, my channel 'CodeVerse' is super cool: https://www.youtube.com/@my_codeverse",
            "Hello! Looking for help? Check out 'CodeVerse' on YouTube: https://www.youtube.com/@my_codeverse",
            "Hey! Need assistance? 'CodeVerse' YouTube channel has you covered: https://www.youtube.com/@my_codeverse",
            "Hi! Got any coding questions? Don't forget to watch 'CodeVerse': https://www.youtube.com/@my_codeverse",
            "Hello! Need help? 'CodeVerse' on YouTube is a must-see: https://www.youtube.com/@my_codeverse",
            "Hey there! Any questions? My channel 'CodeVerse' rocks: https://www.youtube.com/@my_codeverse",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})