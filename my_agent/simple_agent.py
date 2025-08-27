from agents import Agent
from my_confg.gemini_confg import MODEL
from my_tool.web_search_tool import web_search_tool


assistant = Agent(
    name="Assistant",
    instructions="""
    You are helpful assistant.
    You always use web_search_tool for real-time web searches.
    """,
    model=MODEL,
    tools=[web_search_tool]
)