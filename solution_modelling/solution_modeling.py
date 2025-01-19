import json
from typing import Any

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from solution_modelling.prompts import PROMPT, OUTPUT_FORMAT
from utils.data_loader import save_generated_solution


async def generate_solution_for_business_process(event: str, impacted_architecture: dict[str, Any]) -> dict[str, Any]:
    prompt_template = PromptTemplate.from_template(PROMPT)
    prompt = prompt_template.partial(
        company_business_process=json.dumps(impacted_architecture, indent=2),
        external_event=event,
    )
    model = ChatOpenAI(model_name="gpt-4o-mini")
    chain = prompt | model | JsonOutputParser()

    result = await chain.ainvoke({"output_format": OUTPUT_FORMAT})

    save_generated_solution(result, "generated_solution.json")

    return result
