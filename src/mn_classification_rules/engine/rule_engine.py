# File: engine/rule_engine.py

from data_models.parcel import Parcel
from data_models.ownership import Ownership
from engine.classification_result import ClassificationResult
from rules.residential import classify_residential
from config import CLASS_RATES

def get_class_rate_segments(classification: str):
    return CLASS_RATES.get(classification, [])

def compute_tiered_tax_capacity(emv: float, rate_segments: list) -> float:
    remaining_value = emv
    tax_capacity = 0.0
    previous_limit = 0.0

    for tier in rate_segments:
        tier_limit = tier["limit"]
        tier_rate = tier["rate"]
        taxable_amount = min(remaining_value, tier_limit - previous_limit)

        if taxable_amount <= 0:
            break

        tax_capacity += taxable_amount * tier_rate
        remaining_value -= taxable_amount
        previous_limit = tier_limit

    return tax_capacity

def classify_parcel(parcel: Parcel, ownership: Ownership) -> ClassificationResult:
    """
    Control Flow Summary
        Rule engine receives Parcel + Ownership.
        Dispatches to residential.py → determines class (e.g., 1b).
        Loads applicable class rate tiers from config.py.
        Applies EMV to tiered rates → calculates tax capacity.
        Returns populated ClassificationResult.
    """
    classification = classify_residential(parcel, ownership)
    segments = get_class_rate_segments(classification)
    tax_capacity = compute_tiered_tax_capacity(parcel.emv, segments)

    return ClassificationResult(
        parcel_id=parcel.parcel_id,
        classification=classification,
        reason="matched residential rules",
        is_homestead=classification.startswith("1"),
        emv=parcel.emv,
        class_rate=segments[0]["rate"] if segments else 0.0,
        tax_capacity=round(tax_capacity, 2)
    )
