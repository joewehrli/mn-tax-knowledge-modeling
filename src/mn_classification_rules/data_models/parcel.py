# --------------------------
# File: data_models/parcel.py
# --------------------------
from typing import Optional
from pydantic import BaseModel

class Parcel(BaseModel):
    parcel_id: str
    acreage: float
    land_use_code: Optional[str]
    structure_present: bool
    emv: float  # Estimated Market Value
    use_description: Optional[str] = None
    zoning: Optional[str] = None
    contiguous_to_other_homestead: Optional[bool] = False

