import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("🎥I Youtube Video Anayzer")

# cache- fast access , temp storage=> most freq. accessed
# cache fucntion
@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# input box
video_url = st.text_input("Enter youtube video link") # stored as string(str)

button = st.button("Analyze Video") # stored as True/false

print(video_url)
print(button)

# We want to analyze the video when textbox not empty and analyze video button is clicked(true)

if video_url and button:
    with st.spinner("Analyzing video..."):  # spinner-> when agent runs in between show message to user
        response = agent.run(
        f"Analyze this video: {video_url}"
        )
    st.markdown("Analysis Report of Video")
    st.markdown(response.content)
    

