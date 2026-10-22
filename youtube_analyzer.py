from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv  # to load api key
load_dotenv()

def build_youtube_agent():
    return Agent(
    name="Youtube Agent",
    tools=[YouTubeTools()],
    model=OpenAIResponses(id="gpt-5-mini"),
    #model=Groq(id="openai/gpt-oss-120b"),
    add_datetime_to_context=True,
    markdown=True,
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    instructions="Video Overview,Timestamp Creation,Content organization,verify timestamp accuracy, avoid timestamp hallucination"
)

#agent.print_response("Summarize this video https://www.youtube.com/watch?v=xRLfv3ZqdT0 and give  timestamps for each segment", stream=True)