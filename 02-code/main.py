import asyncio

from impact_analysis.impact_analysis import execute_impact_analysis
from solution_modelling.solution_modeling import generate_solution_for_business_process
from utils.data_loader import load_initial_architecture, EVENTS
from utils.visualize_business_process import visualize_business_process

INTRODUCTION_MESSAGE = """
Welcome to the Solution Architect Assistant!

Here you can analyze the negative impact of an external events to your company's business process
 and generate high level solutions that help you to mitigate the impact.
"""


async def main():
    print(INTRODUCTION_MESSAGE)
    formatted_events = "\n\t".join([f"{i + 1}. {event}" for i, event in enumerate(EVENTS)])
    print(f"To start please select an event from the list below:\n\t{formatted_events}")

    await visualize_business_process(load_initial_architecture())

    while True:
        try:
            event_number = int(input("Enter the event number: ")) - 1
            if 0 <= event_number < len(EVENTS):
                break
            else:
                print("Invalid event number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You have selected the following event:\n\t{EVENTS[event_number]}")
    print("Now we are starting Impact analysis process...")
    print("Please wait...")
    result = await execute_impact_analysis(EVENTS[event_number])
    await visualize_business_process(result)
    print("Impact analysis process is completed.")
    print("You can find the impacted architecture in 'impacted_architecture.json' file.")

    print("Now, we are generating solutions to mitigate the impact...")
    print("Please wait...")
    result = await generate_solution_for_business_process(EVENTS[event_number], result)
    await visualize_business_process(result)
    print("Solution generation process is completed.")
    print("You can find the generated solution in 'generated_solution.json' file.")
    print(f"Below is the Detailed Remediation Plan:\n{result['improvement_recommendations']}")

    print("Thank you for using Solution Architect Assistant!")


if __name__ == "__main__":
    asyncio.run(main())
