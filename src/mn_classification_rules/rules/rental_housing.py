# -----------------------------
# File: rules/rental_housing.py
# -----------------------------
from mn_classification_rules.data_models.parcel import Parcel
from mn_classification_rules.data_models.ownership import Ownership

def classify_4a(parcel: Parcel, owner: Ownership) -> bool:
    """4a – Apartment property with >4 units used for residential rental."""
    return (
        parcel.structure_present and
        parcel.use_description == "apartment" and
        parcel.num_units is not None and parcel.num_units >= 4
    )

def classify_4b(parcel: Parcel, owner: Ownership) -> bool:
    """4b – Non-homestead residential property with 1–3 units."""
    return (
        parcel.structure_present and
        parcel.num_units is not None and 1 <= parcel.num_units <= 3 and
        not owner.owner_resides_on_parcel
    )

def classify_4bb(parcel: Parcel, owner: Ownership) -> bool:
    """4bb – Certain low-income housing qualifying under federal/state program."""
    return (
        parcel.structure_present and
        parcel.affordable_housing_program in {"section42", "other_low_income"}
    )

def classify_4d1(parcel: Parcel, owner: Ownership) -> bool:
    """4d(1) – Low-income rental housing qualifying for first-tier tax capacity rate."""
    return (
        classify_4bb(parcel, owner) and
        parcel.percent_low_income_units is not None and
        parcel.percent_low_income_units >= 20
    )

def classify_4d2(parcel: Parcel, owner: Ownership) -> bool:
    """4d(2) – Low-income rental housing above first-tier cutoff (excess units)."""
    return (
        classify_4bb(parcel, owner) and
        parcel.percent_low_income_units is not None and
        parcel.percent_low_income_units < 20
    )

def classify_rental_housing(parcel: Parcel, owner: Ownership) -> str:
    if classify_4d1(parcel, owner):
        return "4d(1)"
    elif classify_4d2(parcel, owner):
        return "4d(2)"
    elif classify_4bb(parcel, owner):
        return "4bb"
    elif classify_4a(parcel, owner):
        return "4a"
    elif classify_4b(parcel, owner):
        return "4b"
    else:
        return "unclassified"
