from dotenv import load_dotenv
import os 
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise KeyError

base_url = os.getenv("BASE_URL")
model = os.getenv("GEMINI_MODEL")

client = AsyncOpenAI(api_key=api_key, base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model=model, openai_client=client)