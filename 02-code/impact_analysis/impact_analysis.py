import json
from typing import Any

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

from impact_analysis.prompts import PROMPT, OUTPUT_FORMAT
from utils.data_loader import load_initial_architecture, save_impacted_architecture
from utils.get_model import get_llm_model


async def execute_impact_analysis(event: str) -> dict[str, Any]:
    initial_architecture = load_initial_architecture()
    prompt = PromptTemplate.from_template(PROMPT)
    prompt = prompt.partial(company_business_process=json.dumps(initial_architecture, indent=2), external_event=event)
    chain = prompt | await get_llm_model() | JsonOutputParser()
    result = await chain.ainvoke({"output_format": OUTPUT_FORMAT})

    save_impacted_architecture(result, "impacted_architecture.json")

    return result
