import streamlit as st
import requests
from func import start_bot

# API endpoint
api_endpoint = "https://basic-sales-ai.fly.dev"

# Mapping of prompt and voice_id
voice_map = {
"British Lady" : "79a125e8-cd45-4c13-8a67-188112f4dd22" ,
"California Girl" : "b7d50908-b17c-442d-ad8d-810c63997ed9" ,
"Child" : "2ee87190-8f84-4925-97da-e52547f9462c" ,
"Classy British Man" : "95856005-0332-41b0-935f-352e296aa0df" ,
"Confident British Man" : "63ff761f-c1e8-414b-b969-d1833d1c870c" ,
"Doctor Mischief" : "fb26447f-308b-471e-8b00-8e9f04284eb5" ,
"Female Nurse" : "5c42302c-194b-4d0c-ba1a-8cb485c84ab9" ,
"Friendly Reading Man" : "69267136-1bdc-412f-ad78-0caad210fb40" ,
"Helpful Woman" : "156fb8d2-335b-4950-9cb3-a2d33befec77" ,
"Kentucky Man" : "726d5ae5-055f-4c3d-8355-d9677de68937" ,
"Madame Mischief" : "e13cae5c-ec59-4f71-b0a6-266df3c9bb8e" ,
"Movieman" : "c45bc5ec-dc68-4feb-8829-6e6b2748095d" ,
"Newsman" : "d46abd1d-2d02-43e8-819f-51fb652c1c61" ,
"Polite Man" : "ee7ea9f8-c0c1-498c-9279-764d6b56d189" ,
"Salesman" : "820a3788-2b37-4d21-847a-b65d8a68c99a" ,
"Southern Woman" : "f9836c6e-a0bd-460e-9d3c-f7299fa60f94" ,
"Storyteller Lady" : "996a8b96-4804-46f0-8e05-3fd4ef1a87cd" ,
"The Merchant" : "50d6beb4-80ea-4802-8387-6c948fe84208"
}

voice_map_el= {
    "Aria": "9BWtsMINqrJLrRacOk9x",
    "Roger": "CwhRBWXzGAHq8TQ4Fs17",
    "Sarah": "EXAVITQu4vr4xnSDxMaL",
    "Laura": "FGY2WhTYpPnrIDTdsKH5",
    "Charlie": "IKne3meq5aSn9XLyUdCD",
    "George": "JBFqnCBsd6RMkjVDRZzb",
    "Callum": "N2lVS1w4EtoT3dr4eOWO",
    "River": "SAz9YHcvj6GT2YYXdXww",
    "Liam": "TX3LPaxmHKxFdv7VOQHJ",
    "Charlotte": "XB0fDUnXU5powFXDhCwa",
    "Alice": "Xb7hH8MSUJpSbSDYk0k2",
    "Matilda": "XrExE9yKIg1WjnnlVkGX",
    "Will": "bIHbv24MWmeRgasZH58o"
}


# Set page config
st.set_page_config(page_title="EasyCloser", layout="centered")

# Sidebar with instructions
st.sidebar.title("Instructions")
st.sidebar.write("""1. Give a scenario and avatar.
2. Customize additional parameters.
3. Click "Start Call" to join.
4. Use the "Join Now" button to enter the call.""")

# Title centered
st.markdown("<h1 style='text-align: center;'>EasyCloser</h1>", unsafe_allow_html=True)

# Prompt selection (Text input instead of dropdown)
prompt = st.text_input("Enter Scenario", "")

# Voice ID selection
selected_voice_id = st.selectbox("Select Avatar", list(voice_map_el.keys()))

# Additional customization options
emotion = st.selectbox("Select Emotion", ["Neutral", "Happy", "Frustrated", "Curious"])
difficulty_level = st.slider("Select Difficulty Level", 1, 5, 3)

# Start Call button with spinner and room URL as "Join Now" button
if st.button("Start Call"):
    with st.spinner("Starting call..."):
        # API request payload
        voice_id = voice_map_el[selected_voice_id]
        response = start_bot(prompt, voice_id)
        room_url = response['room_url']
        room_id = response['room_id']

        st.success("Call setup complete!")

        # Display Join Now button that redirects to the room URL
        st.markdown(f"""
            <a href="{room_url}" target="_blank">
                <button style="background-color: #4CAF50; color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer;">
                    Join Now
                </button>
            </a>
        """, unsafe_allow_html=True)


        Path = f'''{room_id}'''
        st.write("Room Id")
        st.code(Path, language="python")
