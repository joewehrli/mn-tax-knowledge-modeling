
# ----------------------------
# File: data_models/ownership.py
# ----------------------------
from typing import Optional
from pydantic import BaseModel
from datetime import date

class Ownership(BaseModel):
    owner_name: str
    owner_resides_on_parcel: bool
    mn_primary_residence: bool
    disability_status: Optional[str] = None  # e.g., 'blind', 'disabled'
    surviving_spouse_of_veteran: bool = False
    declaration_date: Optional[date] = None
    spouse_on_title: Optional[bool] = None
