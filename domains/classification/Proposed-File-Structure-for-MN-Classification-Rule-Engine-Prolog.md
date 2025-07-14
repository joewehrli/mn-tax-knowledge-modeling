```
mn_classification_engine_prolog/
│
├── main.pl                         % Entry point
├── facts/
│   ├── parcels.pl                  % Parcel facts: id, size, use, owner, emv, etc.
│   ├── ownership.pl               % Owner attributes (resident, blind, etc.)
│   ├── land_use.pl                % Land use facts and use codes
│   ├── programs.pl                % Program enrollment (Green Acres, 2c, etc.)
│   ├── declarations.pl            % Homestead, disability, affidavit filings
│   └── valuation.pl               % Estimated market value, tax capacity
│
├── rules/
│   ├── base_rules.pl              % Shared predicates (contiguity, acreage check, etc.)
│   ├── residential.pl            % Rules for Class 1a, 1b, 1c, 1d
│   ├── agricultural.pl           % Rules for Class 2a, 2b, 2c, 2d, 2e
│   ├── commercial.pl             % Rules for Class 3a
│   ├── rental.pl                 % Rules for Class 4a, 4b, 4bb, 4d
│   ├── seasonal.pl               % Rules for Class 4c(1)-(12)
│   ├── special.pl                % Rules for Class 5(1), 5(2), airport, minerals
│   └── split_class.pl            % Logic for multi-class parcels (e.g., 2a/2b, 1a/3a)
│
├── utils/
│   ├── geo_utils.pl              % Parcel contiguity and spatial checks
│   ├── date_utils.pl             % Timepoint assertions (Jan 2 use, May 1 filings, etc.)
│   └── output.pl                 % Pretty-printing classification results
│
├── data/
│   └── sample_parcels.pl         % Example dataset for testing
│
├── test/
│   ├── test_agricultural.pl
│   ├── test_residential.pl
│   └── ...
│
└── README.md

```

```
Folder	Purpose
facts/	Stores domain-specific property facts (parsed or asserted)
rules/	Logic modules grouped by property class categories
utils/	General utilities (dates, contiguity, formatting)
main.pl	Loads facts, applies rules, prints classification outcome
test/	Unit tests for classification inference accuracy
```

```
:- consult(facts/parcels).
:- consult(rules/residential).
:- consult(rules/agricultural).
:- consult(rules/split_class).

classify_parcel(ParcelID) :-
    classify_residential(ParcelID, Class); 
    classify_agricultural(ParcelID, Class); 
    classify_split(ParcelID, Class),
    format('Parcel ~w is classified as ~w~n', [ParcelID, Class]).
```