import json
from pathlib import Path
from typing import Any

MOCK_DATA_PATH = Path(__file__).parent.parent / "mock_data"

EVENTS = [
    "Payment Gateway Downtime: Disruption in payment verification due to financial institution outages,"
    " delaying reservations",
    "Service Provider Strikes or Shortages: Inability of service providers to fulfill reservations due to"
    " labor disputes or resource shortages",
    "Cybersecurity Breaches: Compromised client data and transaction security from cyber attacks,"
    " eroding trust and causing operational disruptions",
    "Regulatory Changes: Necessary system updates and process modifications due to new or altered legal requirements,"
    " causing delays",
    "Natural Disasters or Pandemics: Service interruptions and high cancellation rates triggered by environmental or"
    " health crises",
]


def load_initial_architecture() -> dict[str, Any]:
    with open(MOCK_DATA_PATH / "service_reservation_e2e_process.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_impacted_architecture(impacted_architecture: dict[str, Any], filename: str) -> None:
    with open(MOCK_DATA_PATH / filename, "w", encoding="utf-8") as file:
        json.dump(impacted_architecture, file, indent=2)


def save_generated_solution(remediated_architecture: dict[str, Any], filename: str) -> None:
    with open(MOCK_DATA_PATH / filename, "w", encoding="utf-8") as file:
        json.dump(remediated_architecture, file, indent=2)
