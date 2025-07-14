```
mn-classification-engine/
│
├── src/
│   ├── index.ts                      # Entry point to run the engine
│   ├── config.ts                     # Class codes, rate tables, deadlines
│   ├── types/
│   │   ├── enums.ts                  # Enums for class codes, use types, statuses
│   │   ├── models/
│   │   │   ├── Parcel.ts             # Parcel schema
│   │   │   ├── Ownership.ts          # Ownership, residency, affidavits
│   │   │   ├── LandUse.ts            # Agricultural, seasonal, vacant, etc.
│   │   │   ├── Valuation.ts          # EMV, tax capacity, rates
│   │   │   └── Declaration.ts        # Homestead and affidavit structures
│   │   └── index.ts                  # Exports all types for external use
│   │
│   ├── rules/
│   │   ├── RuleEngine.ts             # Orchestrator for applying classification rules
│   │   ├── BaseRule.ts               # Base interface or class for rules
│   │   ├── ResidentialRules.ts       # Rules for Class 1a, 1b, 1c, 1d
│   │   ├── AgriculturalRules.ts      # Rules for Class 2a, 2b, 2c, 2d, 2e
│   │   ├── CommercialRules.ts        # Rules for Class 3a
│   │   ├── RentalRules.ts            # Rules for Class 4a, 4b, 4bb, 4d
│   │   ├── SeasonalRules.ts          # Rules for Class 4c(1)-(12)
│   │   ├── SpecialRules.ts           # Rules for Class 5(1), 5(2)
│   │   └── SplitClassification.ts    # Handles multi-use/split classification logic
│   │
│   ├── utils/
│   │   ├── dateUtils.ts              # January 2 checks, deadline evaluation
│   │   ├── parcelUtils.ts            # Contiguity, zoning lookup, spatial joins
│   │   └── validation.ts             # Input validation and coercion
│   │
│   ├── examples/
│   │   ├── sample-parcels.csv
│   │   └── run-demo.ts               # Script to evaluate example parcels
│   │
│   └── tests/
│       ├── rules/
│       │   ├── ResidentialRules.test.ts
│       │   ├── AgriculturalRules.test.ts
│       │   └── ...
│       └── engine/
│           ├── RuleEngine.test.ts
│           └── SplitClassification.test.ts
│
├── package.json
├── tsconfig.json
└── README.md

```

```
Folder	Description
types/models/	Typed schema definitions for inputs and internal use (parcel, ownership, use, etc.)
rules/	Classification logic, broken down by class group
utils/	Common helpers for dates, spatial contiguity, etc.
RuleEngine.ts	Main logic that applies relevant rules to a parcel and generates classification results
SplitClassification.ts	Handles multi-class scenarios like 2a/2b, 1a/3a, etc.
```