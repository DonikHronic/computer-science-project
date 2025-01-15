import json
from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from config import OPENAI_API_KEY
from impact_analysis.prompts import PROMPT, OUTPUT_FORMAT
from utils.data_loader import load_initial_architecture


async def execute_impact_analysis(event: str) -> dict[str, Any]:
    initial_architecture = load_initial_architecture()
    prompt = PromptTemplate.from_template(PROMPT)
    prompt = prompt.partial(company_business_process=json.dumps(initial_architecture, indent=2), external_event=event)
    model = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)
    chain = prompt | model | StrOutputParser()
    result = await chain.ainvoke({"output_format": OUTPUT_FORMAT})
    print(result)

    return result
