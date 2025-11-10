
# --------------------------
# File: test/test_residential.py
# --------------------------
import unittest
from mn_classification_rules.data_models.parcel import Parcel
from mn_classification_rules.data_models.ownership import Ownership
from mn_classification_rules.rules.residential import classify_residential

class TestResidentialClassification(unittest.TestCase):
    def test_class_1a(self):
        parcel = Parcel(parcel_id="A1", acreage=0.25, land_use_code="111", structure_present=True, emv=250000)
        owner = Ownership(owner_name="John Doe", owner_resides_on_parcel=True, mn_primary_residence=True)
        self.assertEqual(classify_residential(parcel, owner), "1a")

    def test_class_1b(self):
        parcel = Parcel(parcel_id="A2", acreage=0.25, land_use_code="111", structure_present=True, emv=180760)
        owner = Ownership(owner_name="Jane Doe", owner_resides_on_parcel=True, mn_primary_residence=True, disability_status="blind")
        self.assertEqual(classify_residential(parcel, owner), "1b")

    def test_class_1c(self):
        parcel = Parcel(parcel_id="A3", acreage=1.0, land_use_code="resort", structure_present=True, emv=750000, use_description="resort")
        owner = Ownership(owner_name="Tom & Katie", owner_resides_on_parcel=True, mn_primary_residence=True)
        self.assertEqual(classify_residential(parcel, owner), "1c")

    def test_class_1d(self):
        parcel = Parcel(parcel_id="A4", acreage=0.5, land_use_code="housing", structure_present=True, emv=130000, use_description="seasonal_worker_housing")
        owner = Ownership(owner_name="Farmer McDonald", owner_resides_on_parcel=False, mn_primary_residence=False)
        self.assertEqual(classify_residential(parcel, owner), "1d")

    def test_unclassified(self):
        parcel = Parcel(parcel_id="A5", acreage=5, land_use_code="vacant", structure_present=False, emv=50000)
        owner = Ownership(owner_name="No One", owner_resides_on_parcel=False, mn_primary_residence=False)
        self.assertEqual(classify_residential(parcel, owner), "unclassified")

if __name__ == '__main__':
    unittest.main()
