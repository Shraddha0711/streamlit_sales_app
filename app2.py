import streamlit as st
import requests
from func import start_bot

# API endpoint
api_endpoint = "https://pipecat-default-example-wispy-cloud-99.fly.dev/"

voice_map = {
"Newsman" : "d46abd1d-2d02-43e8-819f-51fb652c1c61" ,
"Polite Man" : "ee7ea9f8-c0c1-498c-9279-764d6b56d189" ,
"Salesman" : "820a3788-2b37-4d21-847a-b65d8a68c99a" 
}

prompt_dic = {
    "Specsaver Scenario" :"""You are a customer named John, a 28-year-old who recently bought BARBOUR 11 glasses from Specsavers. Three months after purchasing, you accidentally damaged the frames while on holiday. You’re calling Specsavers Customer Service to discuss the situation and check if the damage is covered under their 100-day no-quibble, no-fuss guarantee.\nIn this conversation:\n- Only speak as John, the customer.\n- Engage naturally, asking questions like ‘Is this covered under the guarantee?’, ‘What will it cost if it isn’t?’, and ‘How long would a repair take?’. \n- Avoid providing answers on behalf of the agent. Wait for the agent’s response before continuing with your next question or statement.\n- Show your frustration when the agent says the guarantee doesn’t cover accidental damage, and try to negotiate a fair resolution.\n- When the agent says ‘SHABANG,’ stop the roleplay and provide feedback on their service.\n\nSpeak casually, as if in a real call. Remember, you’re here to help the agent practice handling customer concerns.""",
    "Dell customer agent scenario":"""You are John, a Dell customer who has been receiving regular pop-up messages on your Dell laptop indicating that your Windows operating system is out of date and requires an update. You've been ignoring these for months because you don’t understand what this means and are afraid of "breaking the computer." One morning, your laptop starts running very slowly, and a blue screen appears, mentioning something about "critical updates." Panicking, you call Dell customer service because you believe your computer might be “broken.” You have trouble explaining your issue to the automated system and finally reach a human agent after navigating several confusing prompts. Your role is to engage with the customer service agent as a customer and explain your issue to get a solution""",
    "Marketing Sales Agent scenario":"""You are a lady who runs a small bakery in her local town. Your business is doing well with local foot traffic, but you have noticed that your online orders have been stagnant. Your current website, built years ago using a free platform, looks outdated and doesn’t function well on mobile devices. You know you need a better website to attract more customers, but you've been putting it off due to lack of time and not knowing where to start. You get a call from a sales agent, from a company that specializes in affordable website redesigns for small businesses.The agent will try to sell you his services so engage with him as a prospect. You are a skeptical and curious prospect who will question the agent about how his services are better for your business. Remember You are the prospect and not the sales person"""
    }



# Set page config
st.set_page_config(page_title="EasyCloser", layout="centered")

# Sidebar with instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
1. Choose a scenario and avatar.
2. Customize additional parameters.
3. Click "Start Call" to join.
4. Use the "Join Now" button to enter the call.
""")

# Title centered
st.markdown("<h1 style='text-align: center;'>EasyCloser</h1>", unsafe_allow_html=True)

# Prompt selection
selected_prompt = st.selectbox("Select Scenario", list(prompt_dic.keys()))

# Voice ID selection
selected_voice_id = st.selectbox("Select Avatar", list(voice_map.keys()))

# Additional customization options
emotion = st.selectbox("Select Emotion", ["Neutral", "Happy", "Frustrated", "Curious"])
difficulty_level = st.slider("Select Difficulty Level", 1, 5, 3)

# Start Call button with spinner and room URL as "Join Now" button
if st.button("Start Call"):
    with st.spinner("Starting call..."):
        # API request payload
        prompt = prompt_dic[selected_prompt]
        response = start_bot(prompt)
        room_url = response['room_url']
        
        st.success("Call setup complete!")
        
        # Display Join Now button that redirects to the room URL
        st.markdown(f"""
            <a href="{room_url}" target="_blank">
                <button style="background-color: #4CAF50; color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer;">
                    Join Now
                </button>
            </a>
        """, unsafe_allow_html=True)
