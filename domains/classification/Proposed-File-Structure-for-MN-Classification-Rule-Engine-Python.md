```
mn_classification_rules/
│
├── __init__.py
├── config.py                        # Global constants (class codes, cutoffs, dates)
├── enums.py                         # Enum definitions for class codes, statuses, etc.
├── utils.py                         # Shared utility functions (date parsing, contiguity checks)
│
├── rules/
│   ├── __init__.py
│   ├── base_rule.py                # Base class for classification rules
│   ├── residential.py             # Class 1a, 1b, 1c, 1d
│   ├── agricultural.py            # Class 2a, 2b, 2c, 2d, 2e
│   ├── commercial.py              # Class 3a
│   ├── rental_housing.py          # Class 4a, 4b, 4bb, 4d
│   ├── seasonal.py                # Class 4c(1)-(12)
│   ├── special_use.py             # Class 5(1), 5(2), airports, mineral, etc.
│   └── split_classification.py    # Split use resolution logic
│
├── data_models/
│   ├── __init__.py
│   ├── parcel.py                  # Parcel data model with schema validation
│   ├── ownership.py              # Ownership, residency, and affidavit data
│   ├── land_use.py               # Land use categories and program participation
│   ├── valuation.py              # EMV, tax capacity, tiered class rate computations
│   └── declarations.py           # Homestead, affidavit, and program declarations
│
├── engine/
│   ├── __init__.py
│   ├── rule_engine.py            # Applies rules to parcel records
│   ├── classification_result.py  # Data structure for output results
│   └── evaluation_context.py     # Tracks context (date, program rules, exemptions)
│
├── examples/
│   ├── sample_input.csv
│   └── demo_run.py               # CLI or script to run the engine on sample data
│
└── tests/
    ├── test_residential.py
    ├── test_agricultural.py
    ├── test_split_class.py
    └── ...
```

```
Component	Purpose
rules/	One file per classification grouping; contains logic to test eligibility for each class
data_models/	Typed representations of parcels and their subcomponents (ownership, land use, declarations, etc.)
engine/	Combines rules and data models to compute final classifications
config.py	Holds global parameters like class rate tiers, acreage cutoffs, deadlines
tests/	Unit tests per classification type and edge case
```