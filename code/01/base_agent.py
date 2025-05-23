"""01 Introducción a agentes"""

from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel

load_dotenv()

llm = GeminiModel(model_name="gemini-2.0-flash")

base_agent = Agent(model=llm)
