from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY


async def get_llm_model() -> ChatOpenAI:
    return ChatOpenAI(
        model_name="gpt-4o-mini",
        openai_api_key=OPENAI_API_KEY,
        temperature=0.5,
    )
