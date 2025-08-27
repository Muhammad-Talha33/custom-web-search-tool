from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

tavily_key= os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(tavily_key)
