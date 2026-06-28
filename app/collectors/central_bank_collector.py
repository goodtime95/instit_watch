from typing import Any


def collect_central_bank_data() -> dict[str, Any]:
    """
    Temporary mock central bank collector.
    Will be replaced later by Fed/ECB RSS sources.
    """

    return {
        "fed": "No major Fed decision in the mock dataset.",
        "ecb": "No major ECB decision in the mock dataset.",
        "is_mock": True,
    }