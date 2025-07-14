
# MN Tax Classification

| Component     | Purpose                                                                 |
|---------------|-------------------------------------------------------------------------|
| `rules/`      | One file per classification grouping; contains logic to test eligibility for each class |
| `data_models/`| Typed representations of parcels and their subcomponents (ownership, land use, declarations,etc.) |
| `engine/`     | Combines rules and data models to compute final classifications         |
| `config.py`   | Holds global parameters like class rate tiers, acreage cutoffs, deadlines |
| `tests/`      | Unit tests per classification type and edge case                        |
