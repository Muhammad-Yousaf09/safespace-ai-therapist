# Step1: Setup Streamlit
import streamlit as st
import requests

# BACKEND_URL = # front_end.py
BACKEND_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("🧠 SafeSpace – AI Mental Health Therapist")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Step2: User is able to ask question
# Chat input
user_input = st.chat_input("What's on your mind today?")
if user_input:
    # Debug: Show that input was received
    # st.write(f"DEBUG: Received input: {user_input}")
    
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # AI Agent exists here
    try:
        response = requests.post(BACKEND_URL, json={"message": user_input})
        response.raise_for_status()  # Raises an HTTPError for bad responses
        response_data = response.json()
        assistant_message = f'{response_data["response"]} WITH TOOL: [{response_data["tool_called"]}]'
    except requests.exceptions.RequestException as e:
        assistant_message = f"Error connecting to backend: {str(e)}"
    except KeyError as e:
        assistant_message = f"Unexpected response format: {str(e)}"
    
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})

    #st.session_state.chat_history.append({"role": "assistant", "content": f'{response.json()["response"]} WITH TOOL: [{response.json()["tool_called"]}]'})


# Step3: Show response from backend
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])