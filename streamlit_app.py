import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Set API endpoint and API key
API_ENDPOINT = "https://agent-prod.studio.lyzr.ai/v3/inference/chat/"

API_KEY = os.getenv("x-api-key")
USER_ID = os.getenv("user_id")
AGENT_ID = os.getenv("agent_id")
SESSION_ID = os.getenv("session_id")
#os.environ["API_KEY"] = st.secrets["x-api-key"]

# Load configuration from TOML file
def load_config():
    try:
        #config = toml.load("config.toml")
        #os.environ["API_KEY"] = st.secrets["x-api_key"]
        #API_KEY = os.getenv("x-api_key")
        #os.environ["USER_ID"] = st.secrets["user_id"]
        #USER_ID = os.getenv("user_id")
        #os.environ["AGENT_ID"] = st.secrets["agent_id"]
        AGENT_ID = os.getenv("agent_id")
        os.environ["SESSION_ID"] = st.secrets["session_id"]
        SESSION_ID = os.getenv("session_id")
    except FileNotFoundError:
        st.error("Config file not found")
    except KeyError:
        st.error("Invalid config format")

# Load configuration
#load_config()

def chat_with_agent():
    # Check if environment variables are set
    if not all([API_KEY, USER_ID, AGENT_ID, SESSION_ID]):
        st.error("Environment variables not set")
    else:
        # Create a JSON payload
        payload = {
            "user_id": USER_ID,
            "agent_id": AGENT_ID,
            "session_id": SESSION_ID,
            "message": message
        }
        
        # Set headers
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        }
        
        # Send the request
        #response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(payload))
        try:
            #st.write('In try')
            response = requests.post(API_ENDPOINT, headers=headers, json=payload, timeout =9000 )
            response.raise_for_status()
            # Display the response
            if response.status_code == 200:
            #st.write("Response status code:"+str(response.status_code))
            #Display response in any case
            #st.write("Response:"+str(response.json()))
                return response.json()['response']
      
        except requests.exceptions.HTTPError as http_err:
            st.write(f"HTTP error occured: {http_err}")
            return None
        except Exception as err:
            st.write(f"Other error occured: {err}")
            return None
        
        

        
st.title("Product Space Lyzr AI App:mortar_board:")
st.write(
    "Educator AI app for all your Product Management Learning"
)

#message = "Hello this is Product Management Lyzr AI agent"

# Create a text input for message
message = st.text_area("Start a conversation or try one of these examples  '1.What are your main features'  2.'How do I get started ?'  3.'What knowledge are you trained on ?'", height=100)


# Create a button to send the request
if st.button("Send"):
    #st.write('Calling chat with agent')
    #st.write('message sent'+message)
    st.markdown('---')
    st.markdown('#### Response::robot_face:')
    st.toast("Processing... Please wait...", icon='⏳')
    st.markdown(chat_with_agent())
    st.toast("Processing complete!", icon='✅')
    st.markdown('---')
    #st.write(chat_with_agent())
