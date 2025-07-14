# -----------------------------
# File: rules/residential.py
# -----------------------------

from mn_classification_rules.data_models.parcel import Parcel
from mn_classification_rules.data_models.ownership import Ownership

def classify_1a(parcel: Parcel, owner: Ownership) -> bool:
    return (
        owner.owner_resides_on_parcel and
        parcel.structure_present and
        owner.mn_primary_residence
    )

def classify_1b(parcel: Parcel, owner: Ownership) -> bool:
    if not classify_1a(parcel, owner):
        return False
    return owner.disability_status in {"blind", "disabled"} and not owner.surviving_spouse_of_veteran

def classify_1c(parcel: Parcel, owner: Ownership) -> bool:
    return (
        parcel.use_description == "resort" and
        parcel.structure_present and
        owner.owner_resides_on_parcel
    )

def classify_1d(parcel: Parcel, owner: Ownership) -> bool:
    return (
        parcel.structure_present and
        parcel.use_description == "seasonal_worker_housing"
    )


def classify_residential(parcel: Parcel, owner: Ownership) -> str:
    if classify_1b(parcel, owner):
        return "1b"
    elif classify_1a(parcel, owner):
        return "1a"
    elif classify_1c(parcel, owner):
        return "1c"
    elif classify_1d(parcel, owner):
        return "1d"
    else:
        return "unclassified"

