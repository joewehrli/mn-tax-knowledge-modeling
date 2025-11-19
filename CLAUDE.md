# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research project for knowledge management of Minnesota tax law, specifically focused on property tax classification. It implements a rule engine for classifying properties based on MN tax statutes and calculating tax capacity using tiered rate structures.

The project contains dual implementations:
- **Python implementation**: Production-grade rule engine using Pydantic data models
- **Prolog implementation**: Alternative logic programming approach for comparison

## Development Environment

### Container Setup

The project uses a custom dev container. To build the container image:

```bash
cd container-build
source build-buildah.conf
source build-buildah.sh
make_instance
make_runtime
buildah commit $cname $cname-devcon:0002
```

The dev container is defined in `.devcontainer/devcontainer.json` and references the local image `localhost/mn-tax-knowledge-modeling-devcon:0002`.

### Jupyter Notebook

From inside the VS Code dev container, start Jupyter Lab:

```bash
source /root/ocipy/bin/activate
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

Interactive notebooks are in `notebooks/`:
- `py_classify.ipynb` - Python implementation examples
- `pro_classify.ipynb` - Prolog implementation examples

### Python Package Installation

Install the package in development mode:

```bash
pip install -e .
```

## Python Architecture

### Core Data Models (`src/mn_classification_rules/data_models/`)

Uses Pydantic for validation:

- **`parcel.py`**: `Parcel` model with property characteristics (EMV, structure, units, zoning, affordable housing programs)
- **`ownership.py`**: `Ownership` model with owner attributes (residence status, disability, veteran status)
- **`assessment_context.py`**: Context for assessment calculations (appears minimal/stub)

### Rule Engine (`src/mn_classification_rules/engine/`)

**`rule_engine.py`** contains the core classification logic:

1. `classify_parcel(parcel, ownership)` - Main entry point
2. Dispatches to rule modules (e.g., `rules/residential.py`)
3. Retrieves tiered rate segments from `config.py`
4. Computes tax capacity using `compute_tiered_tax_capacity()`
5. Returns `ClassificationResult` with classification code, reason, and calculated tax capacity

The engine applies MN's tiered tax rate structure where different EMV ranges are taxed at different rates.

### Classification Rules (`src/mn_classification_rules/rules/`)

Rules are organized by property category:

- **`residential.py`**: Homestead classifications (1a, 1b, 1c, 1d)
  - Class 1a: Owner-occupied primary residence with structure
  - Class 1b: Same as 1a but owner has disability (blind/disabled) and is not surviving spouse of veteran
  - Class 1c: Resort property with owner residing on parcel
  - Class 1d: Seasonal worker housing

- **`rental_housing.py`**: Non-homestead rental classifications (4a, 4b, 4bb, 4d)
  - Class 4a: Apartment with 4+ units
  - Class 4b: Non-homestead residential with 1-3 units
  - Class 4bb: Affordable housing under federal/state programs
  - Class 4d(1): Low-income rental with ≥20% low-income units
  - Class 4d(2): Low-income rental with <20% low-income units

Each rule module exports a `classify_*` function that returns the classification string or "unclassified".

### Configuration (`src/mn_classification_rules/config.py`)

`CLASS_RATES` dictionary defines tiered tax capacity rates for each classification. Structure:

```python
"classification_code": [
    {"limit": <threshold_emv>, "rate": <rate>},
    {"limit": float("inf"), "rate": <rate>}
]
```

### Testing

Tests use Python's `unittest` framework and are in `src/mn_classification_rules/test/`:

Run all tests:
```bash
python -m unittest discover -s src/mn_classification_rules/test
```

Run a specific test module:
```bash
python -m unittest src.mn_classification_rules.test.test_residential
python -m unittest src.mn_classification_rules.test.test_rental_housing
```

Run a single test:
```bash
python -m unittest src.mn_classification_rules.test.test_residential.TestResidentialClassification.test_class_1a
```

## Prolog Implementation

The Prolog implementation is in `src_prolog/` with a parallel structure:

- `facts/`: Property facts (parsed or asserted)
- `rules/`: Logic modules for property classification
- `utils/`: General utilities (dates, contiguity, formatting)
- `main.pl`: Loads facts, applies rules, prints classification
- `test/`: Unit tests for classification accuracy

To run Prolog code, ensure SWI-Prolog is installed:
```bash
sudo apt-get update && sudo apt-get install swi-prolog
```

## Key Implementation Notes

- Rule evaluation follows **priority order**: More specific classifications (e.g., 1b) are checked before general ones (e.g., 1a)
- Classification functions use boolean logic to determine eligibility based on Parcel and Ownership attributes
- The tax capacity calculation applies tiered rates progressively, similar to income tax brackets
- All monetary values use EMV (Estimated Market Value) as the base
- The package name is `mn_classification_rules` but repo name is `mn-tax-knowledge-modeling`
