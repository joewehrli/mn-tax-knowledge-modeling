# --------------------------
# File: tests/test_rental_housing.py
# --------------------------
import unittest
from mn_classification_rules.data_models.parcel import Parcel
from mn_classification_rules.data_models.ownership import Ownership
from mn_classification_rules.rules.rental_housing import classify_rental_housing

class TestRentalHousingClassification(unittest.TestCase):
    def test_class_4a(self):
        parcel = Parcel(parcel_id="R1", acreage=0.5, land_use_code="apartment",
                        structure_present=True, emv=2000000, use_description="apartment", num_units=12)
        owner = Ownership(owner_name="Corp LLC", owner_resides_on_parcel=False)
        self.assertEqual(classify_rental_housing(parcel, owner), "4a")

    def test_class_4b(self):
        parcel = Parcel(parcel_id="R2", acreage=0.2, land_use_code="duplex",
                        structure_present=True, emv=300000, use_description="duplex", num_units=2)
        owner = Ownership(owner_name="Investor", owner_resides_on_parcel=False)
        self.assertEqual(classify_rental_housing(parcel, owner), "4b")

    def test_class_4bb(self):
        parcel = Parcel(parcel_id="R3", acreage=1.0, land_use_code="apt",
                        structure_present=True, emv=500000, use_description="apartment",
                        num_units=10, affordable_housing_program="section42")
        owner = Ownership(owner_name="Housing Assoc", owner_resides_on_parcel=False)
        self.assertEqual(classify_rental_housing(parcel, owner), "4bb")

    def test_class_4d1(self):
        parcel = Parcel(parcel_id="R4", acreage=1.0, land_use_code="apt",
                        structure_present=True, emv=1200000, use_description="apartment",
                        num_units=50, affordable_housing_program="section42", percent_low_income_units=40)
        owner = Ownership(owner_name="Nonprofit Housing", owner_resides_on_parcel=False)
        self.assertEqual(classify_rental_housing(parcel, owner), "4d(1)")

    def test_class_4d2(self):
        parcel = Parcel(parcel_id="R5", acreage=1.0, land_use_code="apt",
                        structure_present=True, emv=1200000, use_description="apartment",
                        num_units=50, affordable_housing_program="section42", percent_low_income_units=10)
        owner = Ownership(owner_name="Nonprofit Housing", owner_resides_on_parcel=False)
        self.assertEqual(classify_rental_housing(parcel, owner), "4d(2)")

    def test_unclassified(self):
        parcel = Parcel(parcel_id="R6", acreage=1.0, land_use_code="vacant",
                        structure_present=False, emv=80000, num_units=None)
        owner = Ownership(owner_name="Vacant Lot Owner", owner_resides_on_parcel=False)
        self.assertEqual(classify_rental_housing(parcel, owner), "unclassified")

if __name__ == '__main__':
    unittest.main()

