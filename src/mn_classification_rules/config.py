# File: config.py

CLASS_RATES = {
    "1a": [
        {"limit": 500_000, "rate": 0.01},
        {"limit": float("inf"), "rate": 0.0125}
    ],
    "1b": [
        {"limit": 50_000, "rate": 0.0045},
        {"limit": float("inf"), "rate": 0.01}
    ],
    "1c": [
        {"limit": 600_000, "rate": 0.005},
        {"limit": 2_300_000, "rate": 0.01},
        {"limit": float("inf"), "rate": 0.0125}
    ],
    "1d": [
        {"limit": 500_000, "rate": 0.01},
        {"limit": float("inf"), "rate": 0.0125}
    ]
}
